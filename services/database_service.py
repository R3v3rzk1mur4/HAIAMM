"""
Database Service

This module provides SQLite database operations for the HAIAMM application.
It handles persistence of assessments, responses, version control, and history.
"""

import sqlite3
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Tuple
from contextlib import contextmanager

from models.assessment_model import Assessment, AssessmentResponse, ResponseType


class DatabaseService:
    """
    Manages SQLite database operations for HAIAMM.

    Handles:
    - Assessment CRUD operations
    - Response persistence
    - Version control snapshots
    - Assessment history
    """

    def __init__(self, db_path: Optional[str] = None):
        """
        Initialize database service.

        Args:
            db_path: Path to SQLite database file. If None, uses default location.
        """
        if db_path is None:
            # Default to data/assessments.db
            project_root = Path(__file__).parent.parent
            data_dir = project_root / "data"
            data_dir.mkdir(exist_ok=True)
            db_path = str(data_dir / "assessments.db")

        self.db_path = db_path
        self.is_memory_db = (db_path == ":memory:")
        self._persistent_connection: Optional[sqlite3.Connection] = None

        # For in-memory databases, maintain a persistent connection
        if self.is_memory_db:
            self._persistent_connection = sqlite3.connect(self.db_path)
            self._persistent_connection.row_factory = sqlite3.Row

        self.initialize_database()

    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        if self.is_memory_db and self._persistent_connection:
            # For in-memory DB, reuse the persistent connection
            yield self._persistent_connection
            self._persistent_connection.commit()
        else:
            # For file-based DB, create new connection
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row  # Enable dict-like access
            try:
                yield conn
                conn.commit()
            except Exception:
                conn.rollback()
                raise
            finally:
                conn.close()

    def initialize_database(self):
        """Create database tables if they don't exist."""
        # Use persistent connection for in-memory DB, otherwise create new connection
        if self.is_memory_db and self._persistent_connection:
            conn = self._persistent_connection
            should_close = False
        else:
            conn = sqlite3.connect(self.db_path)
            should_close = True

        schema = """
        -- Assessments table
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            organization TEXT,
            assessor TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT 1
        );

        -- Assessment responses table
        CREATE TABLE IF NOT EXISTS assessment_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            practice_id TEXT NOT NULL,
            maturity_level INTEGER NOT NULL,
            question_id TEXT NOT NULL,
            response TEXT NOT NULL,
            notes TEXT,
            evidence TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (assessment_id) REFERENCES assessments(id) ON DELETE CASCADE,
            UNIQUE(assessment_id, question_id)
        );

        -- Assessment scores table (for future use)
        CREATE TABLE IF NOT EXISTS assessment_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            practice_id TEXT NOT NULL,
            achieved_level INTEGER NOT NULL,
            score_percentage REAL,
            calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (assessment_id) REFERENCES assessments(id) ON DELETE CASCADE,
            UNIQUE(assessment_id, practice_id)
        );

        -- Assessment versions table (snapshots for version control)
        CREATE TABLE IF NOT EXISTS assessment_versions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            version_number INTEGER NOT NULL,
            snapshot_data TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_by TEXT,
            FOREIGN KEY (assessment_id) REFERENCES assessments(id) ON DELETE CASCADE
        );

        -- Undo/redo actions table
        CREATE TABLE IF NOT EXISTS undo_actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            action_type TEXT NOT NULL,
            action_data TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (assessment_id) REFERENCES assessments(id) ON DELETE CASCADE
        );

        -- Roadmap plans table (for future use)
        CREATE TABLE IF NOT EXISTS roadmap_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            target_date DATE,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (assessment_id) REFERENCES assessments(id) ON DELETE CASCADE
        );

        -- Roadmap milestones table (for future use)
        CREATE TABLE IF NOT EXISTS roadmap_milestones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roadmap_id INTEGER NOT NULL,
            practice_id TEXT NOT NULL,
            current_level INTEGER NOT NULL,
            target_level INTEGER NOT NULL,
            target_date DATE,
            priority TEXT,
            status TEXT DEFAULT 'planned',
            notes TEXT,
            FOREIGN KEY (roadmap_id) REFERENCES roadmap_plans(id) ON DELETE CASCADE
        );

        -- Comparison snapshots table (for future use)
        CREATE TABLE IF NOT EXISTS comparison_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            snapshot_date DATE NOT NULL,
            scores_data TEXT NOT NULL,
            notes TEXT,
            FOREIGN KEY (assessment_id) REFERENCES assessments(id) ON DELETE CASCADE
        );

        -- Indexes for performance
        CREATE INDEX IF NOT EXISTS idx_assessment_responses_assessment
            ON assessment_responses(assessment_id);
        CREATE INDEX IF NOT EXISTS idx_assessment_responses_practice
            ON assessment_responses(practice_id);
        CREATE INDEX IF NOT EXISTS idx_assessment_scores_assessment
            ON assessment_scores(assessment_id);
        CREATE INDEX IF NOT EXISTS idx_assessment_versions_assessment
            ON assessment_versions(assessment_id);
        CREATE INDEX IF NOT EXISTS idx_roadmap_milestones_roadmap
            ON roadmap_milestones(roadmap_id);
        """

        try:
            conn.executescript(schema)
            conn.commit()
        finally:
            if should_close:
                conn.close()

    # ===== Assessment CRUD Operations =====

    def save_assessment(self, assessment: Assessment) -> int:
        """
        Save or update an assessment.

        Args:
            assessment: Assessment object to save

        Returns:
            Assessment ID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            if assessment.id is None:
                # Insert new assessment
                cursor.execute("""
                    INSERT INTO assessments (name, description, organization, assessor,
                                            created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    assessment.name,
                    assessment.description,
                    assessment.organization,
                    assessment.assessor,
                    assessment.created_at.isoformat(),
                    assessment.updated_at.isoformat()
                ))
                assessment_id = cursor.lastrowid
                assessment.id = assessment_id
            else:
                # Update existing assessment
                cursor.execute("""
                    UPDATE assessments
                    SET name = ?, description = ?, organization = ?, assessor = ?,
                        updated_at = ?
                    WHERE id = ?
                """, (
                    assessment.name,
                    assessment.description,
                    assessment.organization,
                    assessment.assessor,
                    assessment.updated_at.isoformat(),
                    assessment.id
                ))
                assessment_id = assessment.id

            # Save responses
            self._save_responses(conn, assessment_id, assessment.responses)

            return assessment_id

    def _save_responses(
        self,
        conn: sqlite3.Connection,
        assessment_id: int,
        responses: Dict[str, AssessmentResponse]
    ):
        """Save assessment responses to database."""
        cursor = conn.cursor()

        for question_id, response in responses.items():
            cursor.execute("""
                INSERT OR REPLACE INTO assessment_responses
                (assessment_id, practice_id, maturity_level, question_id, response,
                 notes, evidence)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                assessment_id,
                response.practice_id,
                response.level,
                response.question_id,
                response.response.value,
                response.notes,
                response.evidence
            ))

    def load_assessment(self, assessment_id: int) -> Optional[Assessment]:
        """
        Load an assessment by ID.

        Args:
            assessment_id: Assessment ID

        Returns:
            Assessment object if found, None otherwise
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # Load assessment metadata
            cursor.execute("""
                SELECT id, name, description, organization, assessor,
                       created_at, updated_at
                FROM assessments
                WHERE id = ? AND is_active = 1
            """, (assessment_id,))

            row = cursor.fetchone()
            if not row:
                return None

            assessment = Assessment(
                name=row['name'],
                organization=row['organization'] or '',
                assessor=row['assessor'] or '',
                description=row['description'] or '',
                id=row['id']
            )
            assessment.created_at = datetime.fromisoformat(row['created_at'])
            assessment.updated_at = datetime.fromisoformat(row['updated_at'])

            # Load responses
            cursor.execute("""
                SELECT practice_id, maturity_level, question_id, response,
                       notes, evidence
                FROM assessment_responses
                WHERE assessment_id = ?
            """, (assessment_id,))

            for row in cursor.fetchall():
                response = AssessmentResponse(
                    practice_id=row['practice_id'],
                    level=row['maturity_level'],
                    question_id=row['question_id'],
                    response=ResponseType.from_string(row['response']),
                    notes=row['notes'] or '',
                    evidence=row['evidence'] or ''
                )
                assessment.responses[response.question_id] = response

            return assessment

    def list_assessments(self) -> List[Dict]:
        """
        List all active assessments.

        Returns:
            List of assessment metadata dictionaries
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT a.id, a.name, a.organization, a.assessor, a.created_at,
                       a.updated_at, COUNT(r.id) as response_count
                FROM assessments a
                LEFT JOIN assessment_responses r ON a.id = r.assessment_id
                WHERE a.is_active = 1
                GROUP BY a.id
                ORDER BY a.updated_at DESC
            """)

            assessments = []
            for row in cursor.fetchall():
                assessments.append({
                    'id': row['id'],
                    'name': row['name'],
                    'organization': row['organization'],
                    'assessor': row['assessor'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at'],
                    'response_count': row['response_count']
                })

            return assessments

    def delete_assessment(self, assessment_id: int) -> bool:
        """
        Soft delete an assessment (mark as inactive).

        Args:
            assessment_id: Assessment ID

        Returns:
            True if deleted, False if not found
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE assessments
                SET is_active = 0, updated_at = ?
                WHERE id = ?
            """, (datetime.now().isoformat(), assessment_id))

            return cursor.rowcount > 0

    # ===== Version Control =====

    def save_version_snapshot(
        self,
        assessment_id: int,
        description: str = "",
        created_by: str = ""
    ) -> int:
        """
        Create a version snapshot of an assessment.

        Args:
            assessment_id: Assessment ID
            description: Snapshot description
            created_by: Username who created the snapshot

        Returns:
            Version ID
        """
        assessment = self.load_assessment(assessment_id)
        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        with self.get_connection() as conn:
            cursor = conn.cursor()

            # Get next version number
            cursor.execute("""
                SELECT COALESCE(MAX(version_number), 0) + 1
                FROM assessment_versions
                WHERE assessment_id = ?
            """, (assessment_id,))
            version_number = cursor.fetchone()[0]

            # Serialize assessment to JSON
            snapshot_data = json.dumps(assessment.to_dict())

            # Insert version
            cursor.execute("""
                INSERT INTO assessment_versions
                (assessment_id, version_number, snapshot_data, description, created_by)
                VALUES (?, ?, ?, ?, ?)
            """, (
                assessment_id,
                version_number,
                snapshot_data,
                description,
                created_by
            ))

            return cursor.lastrowid

    def load_version_snapshot(self, version_id: int) -> Optional[Assessment]:
        """
        Load an assessment from a version snapshot.

        Args:
            version_id: Version ID

        Returns:
            Assessment object if found, None otherwise
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT snapshot_data
                FROM assessment_versions
                WHERE id = ?
            """, (version_id,))

            row = cursor.fetchone()
            if not row:
                return None

            data = json.loads(row['snapshot_data'])
            return Assessment.from_dict(data)

    def get_version_history(self, assessment_id: int) -> List[Dict]:
        """
        Get version history for an assessment.

        Args:
            assessment_id: Assessment ID

        Returns:
            List of version metadata dictionaries
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id, version_number, description, created_at, created_by
                FROM assessment_versions
                WHERE assessment_id = ?
                ORDER BY version_number DESC
            """, (assessment_id,))

            versions = []
            for row in cursor.fetchall():
                versions.append({
                    'id': row['id'],
                    'version_number': row['version_number'],
                    'description': row['description'],
                    'created_at': row['created_at'],
                    'created_by': row['created_by']
                })

            return versions

    # ===== Utility Methods =====

    def get_statistics(self) -> Dict:
        """
        Get database statistics.

        Returns:
            Dictionary with statistics
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            stats = {}

            # Count assessments
            cursor.execute("SELECT COUNT(*) FROM assessments WHERE is_active = 1")
            stats['active_assessments'] = cursor.fetchone()[0]

            # Count total responses
            cursor.execute("""
                SELECT COUNT(*)
                FROM assessment_responses r
                JOIN assessments a ON r.assessment_id = a.id
                WHERE a.is_active = 1
            """)
            stats['total_responses'] = cursor.fetchone()[0]

            # Count versions
            cursor.execute("SELECT COUNT(*) FROM assessment_versions")
            stats['total_versions'] = cursor.fetchone()[0]

            return stats


if __name__ == "__main__":
    # Test the database service
    print("Testing Database Service...")

    # Create test database in memory
    db = DatabaseService(":memory:")
    print("✓ Database initialized")

    # Create a test assessment
    assessment = Assessment(
        name="Test Assessment",
        organization="Test Org",
        assessor="Test User"
    )

    # Add some responses
    assessment.add_response(AssessmentResponse(
        practice_id="sm",
        level=1,
        question_id="sm_l1_q1",
        response=ResponseType.YES,
        notes="Test note"
    ))

    assessment.add_response(AssessmentResponse(
        practice_id="sm",
        level=1,
        question_id="sm_l1_q2",
        response=ResponseType.PARTIAL
    ))

    # Save assessment
    assessment_id = db.save_assessment(assessment)
    print(f"✓ Assessment saved with ID: {assessment_id}")

    # Load assessment
    loaded = db.load_assessment(assessment_id)
    print(f"✓ Assessment loaded: {loaded}")
    print(f"  Responses: {loaded.get_response_count()}")

    # List assessments
    assessments = db.list_assessments()
    print(f"✓ Listed {len(assessments)} assessment(s)")
    for a in assessments:
        print(f"  - {a['name']} ({a['response_count']} responses)")

    # Create version snapshot
    version_id = db.save_version_snapshot(
        assessment_id,
        description="Initial snapshot",
        created_by="test"
    )
    print(f"✓ Version snapshot created: {version_id}")

    # Get version history
    history = db.get_version_history(assessment_id)
    print(f"✓ Version history: {len(history)} version(s)")

    # Get statistics
    stats = db.get_statistics()
    print(f"✓ Statistics: {stats}")

    print("\nAll tests passed!")
