#!/usr/bin/env python3
"""
Phase 1 Test Script

Tests core functionality:
1. OpenSAMM model loading
2. Assessment creation
3. Database persistence
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from models.opensamm_model import load_opensamm_model
from models.assessment_model import Assessment, AssessmentResponse, ResponseType
from services.database_service import DatabaseService


def test_phase1():
    """Test Phase 1: Foundation (MVP)."""
    print("=" * 60)
    print("HAIAMM Phase 1 Test - Foundation (MVP)")
    print("=" * 60)

    # Test 1: Load OpenSAMM Model
    print("\n[1/5] Loading OpenSAMM v1.0 Model...")
    try:
        samm_model = load_opensamm_model()
        print(f"✓ {samm_model}")
        print(f"  - Business Functions: {len(samm_model.business_functions)}")
        print(f"  - Security Practices: {samm_model.get_practice_count()}")
        print(f"  - Total Questions: {samm_model.get_total_questions()}")

        # Show business functions
        for func in samm_model.business_functions:
            print(f"\n  {func.name}:")
            for practice in func.practices:
                print(f"    - {practice.short_name}: {practice.name}")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 2: Create Assessment
    print("\n[2/5] Creating Assessment...")
    try:
        assessment = Assessment(
            name="Phase 1 Test Assessment",
            organization="Test Organization",
            assessor="Test User",
            description="Testing Phase 1 functionality"
        )
        print(f"✓ Created: {assessment}")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 3: Add Responses
    print("\n[3/5] Adding Assessment Responses...")
    try:
        # Add responses for Strategy & Metrics Level 1
        responses_to_add = [
            ("sm", 1, "sm_l1_q1", ResponseType.YES, "Risk assessment completed"),
            ("sm", 1, "sm_l1_q2", ResponseType.YES, "Strategic plan exists"),
            ("sm", 1, "sm_l1_q3", ResponseType.PARTIAL, "Working on management buy-in"),
            # Add responses for Policy & Compliance Level 1
            ("pc", 1, "pc_l1_q1", ResponseType.YES, "Requirements identified"),
            ("pc", 1, "pc_l1_q2", ResponseType.YES, "Documentation maintained"),
            ("pc", 1, "pc_l1_q3", ResponseType.PARTIAL, "Monitoring in progress"),
        ]

        for practice_id, level, question_id, response_type, notes in responses_to_add:
            response = AssessmentResponse(
                practice_id=practice_id,
                level=level,
                question_id=question_id,
                response=response_type,
                notes=notes
            )
            assessment.add_response(response)

        print(f"✓ Added {assessment.get_response_count()} responses")
        total_questions = samm_model.get_total_questions()
        completion = assessment.get_completion_percentage(total_questions)
        print(f"  Completion: {completion:.1f}% ({assessment.get_response_count()}/{total_questions})")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 4: Save to Database
    print("\n[4/5] Saving to Database...")
    try:
        db = DatabaseService()
        assessment_id = db.save_assessment(assessment)
        print(f"✓ Assessment saved with ID: {assessment_id}")

        # Create a version snapshot
        version_id = db.save_version_snapshot(
            assessment_id,
            description="Initial version",
            created_by="test_script"
        )
        print(f"✓ Version snapshot created: {version_id}")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 5: Load from Database
    print("\n[5/5] Loading from Database...")
    try:
        loaded_assessment = db.load_assessment(assessment_id)
        if loaded_assessment:
            print(f"✓ Assessment loaded: {loaded_assessment}")
            print(f"  Responses: {loaded_assessment.get_response_count()}")

            # Verify responses match
            if loaded_assessment.get_response_count() == assessment.get_response_count():
                print("✓ Response count matches original")
            else:
                print("✗ Response count mismatch!")
                return False

            # List all assessments
            all_assessments = db.list_assessments()
            print(f"\n✓ Total assessments in database: {len(all_assessments)}")
            for a in all_assessments[:5]:  # Show first 5
                print(f"  - {a['name']} ({a['response_count']} responses)")

            # Get statistics
            stats = db.get_statistics()
            print(f"\n✓ Database Statistics:")
            print(f"  - Active assessments: {stats['active_assessments']}")
            print(f"  - Total responses: {stats['total_responses']}")
            print(f"  - Total versions: {stats['total_versions']}")
        else:
            print(f"✗ Failed to load assessment {assessment_id}")
            return False
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Success!
    print("\n" + "=" * 60)
    print("✓ Phase 1 Test PASSED - All core functionality working!")
    print("=" * 60)
    print("\nPhase 1 Deliverables:")
    print("✓ Application can load OpenSAMM v1.0 model")
    print("✓ Can create new assessments")
    print("✓ Can add assessment responses")
    print("✓ Can save assessments to SQLite database")
    print("✓ Can load assessments from database")
    print("✓ Version control snapshots work")
    print("\nNext Steps: Phase 2 - Questionnaire Engine")
    return True


if __name__ == "__main__":
    success = test_phase1()
    sys.exit(0 if success else 1)
