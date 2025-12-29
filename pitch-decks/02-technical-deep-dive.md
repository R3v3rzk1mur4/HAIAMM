# HAIAMM - Technical Deep Dive
## Architecture, Implementation, and Technical Excellence

---

## Slide 1: Technical Overview

### HAIAMM System Architecture

**Framework Type:** Desktop HAI Maturity Assessment Application
**Foundation:** OWASP OpenSAMM v1.0 extended for Human Assisted Intelligence
**Architecture Pattern:** Enhanced MVC with Service Layer

**Core Technology Stack:**
```
Language:      Python 3.10+
UI Framework:  PyQt6 (6.6.0+)
Database:      SQLite3
Visualization: Matplotlib, Plotly
Data:          Pandas, NumPy
Security:      python-gnupg (PGP encryption)
Testing:       pytest, pytest-qt
Packaging:     PyInstaller
```

**Scale:**
- 6 HAI Domains
- 72 Practice Instances (12 practices × 6 domains)
- 216 Maturity Levels (3 per practice instance)
- 432 Assessment Criteria
- Structured JSON configuration

---

## Slide 2: System Architecture Diagram

### Enhanced MVC with Service Layer

```
┌─────────────────────────────────────────────────────┐
│                   UI Layer (PyQt6)                   │
├─────────────────────────────────────────────────────┤
│  MainWindow  │ Questionnaire │ Dashboard │ Scoring  │
│              │     View      │   View    │   View   │
└──────┬───────┴───────┬───────┴─────┬─────┴──────────┘
       │               │             │
       ▼               ▼             ▼
┌─────────────────────────────────────────────────────┐
│                 Controller Layer                     │
├─────────────────────────────────────────────────────┤
│  Questionnaire Controller  │  Assessment Controller │
└──────┬─────────────────────┴────────────────┬───────┘
       │                                      │
       ▼                                      ▼
┌─────────────────────────────────────────────────────┐
│                   Service Layer                      │
├─────────────────────────────────────────────────────┤
│  Database    │  Visualization │  Export  │  Scoring │
│  Service     │    Service     │ Service  │  Service │
└──────┬───────┴───────┬────────┴─────┬────┴──────────┘
       │               │              │
       ▼               ▼              ▼
┌─────────────────────────────────────────────────────┐
│                    Model Layer                       │
├─────────────────────────────────────────────────────┤
│  HAIAMM     │ Assessment │ Questionnaire │  Scoring │
│  Model      │   Model    │    Model      │  Model   │
└──────┬──────┴────┬───────┴───────┬───────┴──────────┘
       │           │               │
       ▼           ▼               ▼
┌─────────────────────────────────────────────────────┐
│                 Persistence Layer                    │
├─────────────────────────────────────────────────────┤
│  SQLite Database  │  JSON Config  │  Export Files   │
└─────────────────────────────────────────────────────┘
```

**Design Principles:**
- **Separation of Concerns:** Each layer has a single responsibility
- **Testability:** Service layer enables unit testing without UI
- **Extensibility:** New domains/practices added via JSON config
- **Offline-First:** Complete functionality without network dependency

---

## Slide 3: Data Model Architecture

### HAIAMM Multi-Domain Model

**Model Hierarchy:**

```python
HAIAMM Model
├── Domain (6x)
│   ├── Software
│   ├── Infrastructure
│   ├── Endpoints
│   ├── Data
│   ├── Processes
│   └── Vendors
│
Each Domain contains:
├── Business Functions (4x)
│   ├── Governance
│   ├── Engineering
│   ├── Verification
│   └── Operations
│
Each Business Function contains:
├── Security Practices (3-4x, 78 total)
│   └── Practice
│       ├── Maturity Level 1
│       │   ├── Activity (what to do)
│       │   ├── Results (outcomes)
│       │   └── Questions (criteria, ~9 per level)
│       ├── Maturity Level 2
│       │   └── [same structure]
│       └── Maturity Level 3
│           └── [same structure]
```

**Key Model Files:**

| File | Purpose | LOC |
|------|---------|-----|
| `haiamm_model.py` | 6-domain HAIAMM structure | ~500 |
| `assessment_model.py` | Assessment responses & tracking | ~300 |
| `scoring_model.py` | Maturity calculation engine | ~400 |
| `questionnaire_model.py` | Dynamic question generation | ~250 |
| `opensamm_model.py` | Base OpenSAMM v1.0 model | ~400 |

---

## Slide 4: Database Schema

### SQLite Persistence Design

**Schema Structure:**

```sql
-- Assessments table
CREATE TABLE assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_date TEXT NOT NULL,
    last_modified TEXT NOT NULL,
    version TEXT DEFAULT '1.0',
    status TEXT DEFAULT 'in_progress'
);

-- Responses table (stores all answers)
CREATE TABLE responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id INTEGER NOT NULL,
    domain TEXT NOT NULL,
    business_function TEXT NOT NULL,
    practice TEXT NOT NULL,
    maturity_level INTEGER NOT NULL,
    question_id TEXT NOT NULL,
    answer BOOLEAN NOT NULL,
    notes TEXT,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (assessment_id) REFERENCES assessments(id)
        ON DELETE CASCADE
);

-- Scores table (calculated maturity scores)
CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id INTEGER NOT NULL,
    domain TEXT NOT NULL,
    business_function TEXT,
    practice TEXT,
    maturity_level INTEGER,
    score REAL NOT NULL,
    achieved BOOLEAN,
    calculated_date TEXT NOT NULL,
    FOREIGN KEY (assessment_id) REFERENCES assessments(id)
        ON DELETE CASCADE
);

-- Roadmaps table (planned improvements)
CREATE TABLE roadmaps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id INTEGER NOT NULL,
    domain TEXT NOT NULL,
    practice TEXT NOT NULL,
    target_level INTEGER NOT NULL,
    priority TEXT DEFAULT 'medium',
    estimated_effort TEXT,
    notes TEXT,
    status TEXT DEFAULT 'planned',
    created_date TEXT NOT NULL,
    FOREIGN KEY (assessment_id) REFERENCES assessments(id)
        ON DELETE CASCADE
);
```

**Database Features:**
- **Normalized Schema:** 3NF, minimal redundancy
- **Referential Integrity:** CASCADE deletes maintain consistency
- **Indexing:** Foreign keys indexed for fast joins
- **Versioning:** Assessment version tracking for migrations
- **Audit Trail:** Timestamps on all modifications

---

## Slide 5: Scoring Algorithm

### OpenSAMM Maturity Calculation

**Scoring Logic:**

```python
def calculate_practice_score(responses: List[Response]) -> float:
    """
    Calculate maturity score for a security practice.

    OpenSAMM Rule: ≥80% of questions answered 'Yes' = level achieved
    Score: Highest achieved level (0-3)
    """
    level_scores = {1: 0.0, 2: 0.0, 3: 0.0}

    for level in [1, 2, 3]:
        level_responses = [r for r in responses if r.maturity_level == level]
        if not level_responses:
            continue

        yes_count = sum(1 for r in level_responses if r.answer)
        total_count = len(level_responses)

        # Calculate percentage
        percentage = (yes_count / total_count) * 100

        # Apply 80% threshold
        level_scores[level] = 1.0 if percentage >= 80 else 0.0

    # Score is cumulative: L3 requires L2 and L1
    if level_scores[3] == 1.0 and level_scores[2] == 1.0 and level_scores[1] == 1.0:
        return 3.0
    elif level_scores[2] == 1.0 and level_scores[1] == 1.0:
        return 2.0
    elif level_scores[1] == 1.0:
        return 1.0
    else:
        return 0.0

def calculate_domain_score(practice_scores: List[float]) -> float:
    """
    Calculate domain-level score (average of practice scores).
    """
    return sum(practice_scores) / len(practice_scores) if practice_scores else 0.0
```

**Scoring Hierarchy:**
1. **Question Level:** Yes/No (Boolean)
2. **Maturity Level:** ≥80% threshold
3. **Practice Level:** Highest achieved level (0-3)
4. **Business Function:** Average of practice scores
5. **Domain Level:** Average of all practice scores in domain
6. **Overall Maturity:** Weighted average of domain scores

---

## Slide 6: Dynamic Questionnaire Engine

### Adaptive Question Generation

**Questionnaire Types:**

```python
class QuestionnaireType(Enum):
    FULL = "full"                    # All 72 practice instances, all 3 levels
    LEVEL_1_ONLY = "level_1_only"   # All 72 practice instances, L1 only
    CUSTOM = "custom"                # User-selected domains/practices/levels

class QuestionnaireGenerator:
    """Generates dynamic questionnaires based on selection criteria."""

    def generate_full_questionnaire(self) -> List[Question]:
        """Generate complete assessment (432 questions for v2.0)."""
        questions = []
        for domain in self.haiamm_model.domains:
            for bf in domain.business_functions:
                for practice in bf.practices:
                    for level in [1, 2, 3]:
                        questions.extend(practice.levels[level].questions)
        return questions

    def generate_level_1_questionnaire(self) -> List[Question]:
        """Generate baseline assessment (~234 questions)."""
        questions = []
        for domain in self.haiamm_model.domains:
            for bf in domain.business_functions:
                for practice in bf.practices:
                    questions.extend(practice.levels[1].questions)
        return questions

    def generate_custom_questionnaire(
        self,
        selected_domains: List[str],
        selected_practices: List[str],
        selected_levels: List[int]
    ) -> List[Question]:
        """Generate custom assessment based on criteria."""
        questions = []
        for domain in self.haiamm_model.domains:
            if domain.name not in selected_domains:
                continue
            for bf in domain.business_functions:
                for practice in bf.practices:
                    if practice.name not in selected_practices:
                        continue
                    for level in selected_levels:
                        questions.extend(practice.levels[level].questions)
        return questions
```

**Features:**
- **Progress Tracking:** Real-time completion percentage
- **Auto-Save:** Responses saved after each answer
- **Resume Capability:** Continue incomplete assessments
- **Validation:** Ensures all required questions answered before scoring

---

## Slide 7: Visualization Architecture

### Matplotlib + PyQt6 Integration

**Visualization Service:**

```python
class VisualizationService:
    """Generates interactive visualizations for dashboards."""

    def generate_radar_chart(
        self,
        domain_scores: Dict[str, float]
    ) -> Figure:
        """
        Multi-domain radar chart.

        Args:
            domain_scores: {"Software": 2.1, "Infrastructure": 2.5, ...}

        Returns:
            Matplotlib Figure embedded in PyQt6 widget
        """
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='polar')

        # Prepare data
        domains = list(domain_scores.keys())
        scores = list(domain_scores.values())

        # Close the polygon
        domains.append(domains[0])
        scores.append(scores[0])

        # Calculate angles
        angles = np.linspace(0, 2 * np.pi, len(domains), endpoint=True)

        # Plot
        ax.plot(angles, scores, 'o-', linewidth=2, label='Current')
        ax.fill(angles, scores, alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(domains[:-1])
        ax.set_ylim(0, 3)
        ax.set_yticks([0, 1, 2, 3])
        ax.grid(True)

        return fig

    def generate_heatmap(
        self,
        domain_level_scores: Dict[str, Dict[int, float]]
    ) -> Figure:
        """
        Maturity heatmap showing L1/L2/L3 achievement by domain.

        Args:
            domain_level_scores: {
                "Software": {1: 1.0, 2: 0.85, 3: 0.4},
                ...
            }
        """
        # Implementation using matplotlib imshow
        # Color scale: 0-0.79 (red), 0.8-1.0 (green)
        ...
```

**Chart Types:**
1. **Radar Chart:** 6-domain overview
2. **Heatmap:** Maturity level achievement matrix
3. **Bar Chart:** Business function comparisons
4. **Line Chart:** Trend analysis over time
5. **Scatter Plot:** Practice-level detail

---

## Slide 8: Configuration Management

### JSON-Driven Extensibility

**Configuration Structure:**

```json
{
  "haiamm_version": "1.0",
  "domains": [
    {
      "name": "Software",
      "description": "Security practices for AI software development",
      "business_functions": [
        {
          "name": "Governance",
          "practices": [
            {
              "name": "Strategy & Metrics",
              "shortcode": "SM",
              "levels": {
                "1": {
                  "activity": "Establish unified strategic roadmap...",
                  "results": "Document security goals...",
                  "questions": [
                    {
                      "id": "SM-L1-Q1",
                      "text": "Does the organization have documented...",
                      "type": "boolean"
                    }
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

**Benefits:**
- **No Code Changes:** Add domains/practices via JSON
- **Version Control:** Track config changes over time
- **Organization-Specific:** Custom practices for unique needs
- **Validation:** JSON schema ensures consistency

---

## Slide 9: Export & Integration

### Data Portability

**Export Formats:**

```python
class ExportService:
    """Export assessments to various formats."""

    def export_to_json(
        self,
        assessment_id: int,
        include_scores: bool = True,
        encrypt: bool = False,
        pgp_recipient: str = None
    ) -> str:
        """
        Export assessment to JSON.

        Returns:
            JSON string or path to encrypted file
        """
        assessment = self.db.get_assessment(assessment_id)
        responses = self.db.get_responses(assessment_id)

        export_data = {
            "assessment": assessment.to_dict(),
            "responses": [r.to_dict() for r in responses],
            "metadata": {
                "export_date": datetime.now().isoformat(),
                "haiamm_version": "1.0"
            }
        }

        if include_scores:
            export_data["scores"] = self.scoring_service.calculate_all_scores(
                assessment_id
            )

        json_str = json.dumps(export_data, indent=2)

        if encrypt and pgp_recipient:
            return self.encrypt_with_pgp(json_str, pgp_recipient)

        return json_str

    def export_to_csv(self, assessment_id: int) -> pd.DataFrame:
        """Export assessment responses to CSV."""
        responses = self.db.get_responses(assessment_id)
        df = pd.DataFrame([r.to_dict() for r in responses])
        return df
```

**Integration Points:**
- REST API (planned) for GRC platform integration
- CSV export for Excel/BI tools
- JSON export for SIEM ingestion
- PGP encryption for secure transmission

---

## Slide 10: Testing Strategy

### Comprehensive Test Coverage

**Test Pyramid:**

```
                 ▲
                / \
               /   \
              / E2E \        PyQt6 UI tests (pytest-qt)
             /       \       ~50 tests, critical paths
            /_________\
           /           \
          / Integration \    Service layer tests
         /     Tests     \   ~100 tests, API contracts
        /_________________\
       /                   \
      /     Unit Tests      \ Model/business logic tests
     /                       \ ~200 tests, full coverage
    /_________________________\
```

**Test Files:**

```python
# Unit Tests
tests/test_models/
  test_haiamm_model.py          # Domain/practice structure
  test_assessment_model.py      # Assessment lifecycle
  test_scoring_model.py         # Scoring algorithm
  test_questionnaire_model.py   # Question generation

# Integration Tests
tests/test_services/
  test_database_service.py      # SQLite CRUD operations
  test_visualization_service.py # Chart generation
  test_export_service.py        # JSON/CSV export

# E2E Tests
tests/test_ui/
  test_main_window.py           # Main UI workflows
  test_questionnaire_view.py    # Assessment completion
  test_dashboard_view.py        # Visualization rendering
```

**Coverage Target:** 85%+ for production release

**CI/CD:**
- GitHub Actions on push/PR
- Automated test execution
- Code quality checks (ruff, mypy)
- PyInstaller build verification

---

## Slide 11: Security Considerations

### Built-In Security Features

**Application Security:**

```python
# 1. PGP Encryption for Exports
class EncryptionService:
    def encrypt_assessment(self, data: str, recipient_key: str) -> bytes:
        """Encrypt sensitive assessment data using GPG."""
        gpg = gnupg.GPG()
        encrypted = gpg.encrypt(
            data,
            recipient_key,
            armor=True,
            always_trust=False,  # Verify key trust
            sign=True            # Sign with user's private key
        )
        return encrypted.data

# 2. SQL Injection Prevention
class DatabaseService:
    def save_response(self, response: Response) -> None:
        """Parameterized queries prevent SQL injection."""
        self.cursor.execute(
            """
            INSERT INTO responses
            (assessment_id, domain, practice, answer, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (response.assessment_id, response.domain,
             response.practice, response.answer, response.notes)
        )

# 3. Input Validation
class AssessmentValidator:
    def validate_assessment_name(self, name: str) -> bool:
        """Validate user inputs to prevent injection attacks."""
        if not name or len(name) > 255:
            raise ValueError("Invalid assessment name length")

        # Whitelist allowed characters
        if not re.match(r'^[a-zA-Z0-9\s\-_]+$', name):
            raise ValueError("Assessment name contains invalid characters")

        return True
```

**Data Protection:**
- Local SQLite database (no cloud exposure by default)
- Optional PGP encryption for exports
- No telemetry or data collection
- User controls all data storage locations

**Code Security:**
- Dependency scanning (pip-audit)
- Static analysis (ruff, bandit)
- Regular security updates
- Minimal attack surface (desktop app, no network by default)

---

## Slide 12: Performance Optimization

### Scaling to Large Assessments

**Performance Targets:**

| Operation | Target | Notes |
|-----------|--------|-------|
| Load assessment | <200ms | SQLite indexed queries |
| Answer question | <50ms | In-memory update + async DB write |
| Calculate scores | <500ms | All 72 practice instances, all levels |
| Render dashboard | <1s | 6-domain radar chart + heatmap |
| Export JSON | <300ms | Full assessment with scores |
| Generate questionnaire | <100ms | 432 questions, full assessment (v2.0) |

**Optimization Techniques:**

```python
# 1. Database Indexing
CREATE INDEX idx_responses_assessment
    ON responses(assessment_id, domain, practice);

CREATE INDEX idx_scores_assessment
    ON scores(assessment_id, domain);

# 2. Lazy Loading
class DashboardView:
    def load_visualizations(self):
        """Load charts only when tab is activated."""
        if not self.charts_loaded:
            self.render_radar_chart()
            self.render_heatmap()
            self.charts_loaded = True

# 3. Caching
class ScoringService:
    @lru_cache(maxsize=128)
    def calculate_practice_score(
        self,
        assessment_id: int,
        practice_id: str
    ) -> float:
        """Cache calculated scores to avoid recomputation."""
        ...

# 4. Async Database Operations
class DatabaseService:
    async def save_response_async(self, response: Response) -> None:
        """Non-blocking database writes."""
        await asyncio.to_thread(self._save_response_sync, response)
```

---

## Slide 13: Deployment Architecture

### Cross-Platform Distribution

**Build Pipeline:**

```bash
# PyInstaller configuration
pyinstaller haiamm.spec \
  --name HAIAMM \
  --windowed \
  --onefile \
  --add-data "config:config" \
  --add-data "assets:assets" \
  --hidden-import PyQt6 \
  --hidden-import matplotlib \
  --icon assets/haiamm.icns

# Platform-specific builds
- macOS: .app bundle (code-signed, notarized)
- Windows: .exe installer (signed with certificate)
- Linux: AppImage (universal binary)
```

**Distribution Channels:**
1. Direct download (GitHub Releases)
2. Homebrew (macOS): `brew install haiamm`
3. Chocolatey (Windows): `choco install haiamm`
4. Snap/Flatpak (Linux)

**Enterprise Deployment:**
- MSI installer for Windows domain deployment
- DMG for macOS enterprise distribution
- Docker container for Linux servers
- Silent install options for IT automation

---

## Slide 14: Extensibility & Customization

### Plugin Architecture (Future)

**Planned Extension Points:**

```python
# Custom Domain Plugin
class CustomDomainPlugin:
    """Add organization-specific security domains."""

    def register_domain(self) -> Domain:
        return Domain(
            name="Compliance",
            description="Regulatory compliance practices",
            business_functions=[...]
        )

# Custom Scoring Algorithm
class CustomScoringPlugin:
    """Override default OpenSAMM scoring logic."""

    def calculate_practice_score(
        self,
        responses: List[Response]
    ) -> float:
        # Custom logic (e.g., weighted questions, risk scoring)
        return custom_score

# Custom Export Format
class CustomExportPlugin:
    """Add new export formats (e.g., PDF, DOCX)."""

    def export(self, assessment: Assessment) -> bytes:
        # Generate custom report format
        return report_bytes

# Integration Connector
class GRCIntegrationPlugin:
    """Sync assessments with GRC platforms."""

    def sync_to_platform(
        self,
        assessment: Assessment,
        platform_url: str,
        api_key: str
    ) -> bool:
        # Push assessment data to external GRC system
        return success
```

**Plugin System Benefits:**
- Organization-specific customization without forking
- Third-party integration ecosystem
- Community contributions
- Enterprise feature additions

---

## Slide 15: Technical Roadmap

### Future Enhancements

**Phase 4-6 (In Progress):**
- ✓ Export service (JSON/CSV/PGP)
- ✓ Version control & undo/redo
- ✓ Roadmap planning interface

**Phase 7-8 (Q1 2025):**
- Assessment comparison engine
- Historical trend analysis
- Polish & UX improvements
- Comprehensive documentation
- Installer packaging

**Future Features (2025+):**

**1. Cloud Sync (Optional)**
- End-to-end encrypted cloud backup
- Multi-device synchronization
- Collaborative assessments
- Team workspace support

**2. Integration APIs**
- REST API for SIEM/GRC platforms
- Webhook notifications
- SSO/SAML authentication
- Role-based access control (RBAC)

**3. AI-Powered Features**
- Recommendation engine for improvements
- Gap analysis with ML insights
- Automated roadmap prioritization
- Natural language query interface

**4. Industry Benchmarking**
- Anonymous aggregate scoring
- Compare against industry peers
- Best practice recommendations
- Maturity trend forecasting

---

## Slide 16: Development Best Practices

### Code Quality & Standards

**Code Style:**
- **Linter:** Ruff (Python 3.10+ compatible)
- **Type Checking:** mypy with strict mode
- **Formatting:** Black (line length 88)
- **Docstrings:** Google style

**Git Workflow:**
```bash
main          # Production-ready releases
├── develop   # Integration branch
├── feature/* # Feature branches
├── hotfix/*  # Critical fixes
└── release/* # Release candidates
```

**Commit Convention:**
```
type(scope): subject

- feat: New feature
- fix: Bug fix
- docs: Documentation
- test: Test additions
- refactor: Code restructuring
- perf: Performance improvement
```

**Code Review Checklist:**
- ✓ All tests passing
- ✓ Type hints on public APIs
- ✓ Documentation updated
- ✓ No security vulnerabilities (bandit scan)
- ✓ Performance regression check
- ✓ UI/UX review (for UI changes)

---

## Slide 17: Technical Challenges & Solutions

### Lessons Learned

**Challenge 1: UI Responsiveness with Large Datasets**
- **Problem:** 702-question questionnaire caused UI lag
- **Solution:** Pagination (20 questions per page) + lazy loading
- **Result:** Sub-50ms response time per question

**Challenge 2: Cross-Platform Visualization Rendering**
- **Problem:** Matplotlib charts rendered differently on macOS/Windows/Linux
- **Solution:** Standardized DPI settings + explicit figure sizing
- **Result:** Consistent visuals across all platforms

**Challenge 3: Database Concurrency**
- **Problem:** SQLite write locks during auto-save
- **Solution:** Write-ahead logging (WAL mode) + async writes
- **Result:** Zero lock contention, smooth UX

**Challenge 4: Config File Validation**
- **Problem:** Invalid JSON caused app crashes
- **Solution:** JSON schema validation + graceful error handling
- **Result:** User-friendly error messages, no crashes

**Challenge 5: Secure Export of Sensitive Data**
- **Problem:** Assessment data contains sensitive security details
- **Solution:** PGP encryption + key management UI
- **Result:** Enterprise-grade export security

---

## Slide 18: System Requirements & Compatibility

### Deployment Specifications

**Minimum Requirements:**
```
OS:       macOS 11+, Windows 10+, Ubuntu 20.04+
CPU:      Dual-core 2.0 GHz
RAM:      4 GB
Storage:  500 MB
Display:  1280x800 minimum resolution
Python:   3.10+ (bundled in standalone executable)
```

**Recommended Requirements:**
```
OS:       macOS 13+, Windows 11, Ubuntu 22.04+
CPU:      Quad-core 3.0 GHz
RAM:      8 GB
Storage:  1 GB
Display:  1920x1080 or higher
Python:   3.11+ (for development)
```

**Tested Platforms:**
- macOS: 11 (Big Sur), 12 (Monterey), 13 (Ventura), 14 (Sonoma)
- Windows: 10 (21H2), 11 (22H2)
- Linux: Ubuntu 20.04, 22.04, Fedora 38, Arch (latest)

**Known Limitations:**
- SQLite database size: Tested up to 1GB (10,000+ assessments)
- Concurrent users: Single-user application (multi-user via future cloud sync)
- Network: Offline-first (no network required for core functionality)

---

## HAIAMM Technical Architecture
### Built for Scale, Security, and Extensibility

**Questions?**

**Technical Documentation:**
- GitHub: [Your repo]
- Developer Docs: [Your docs URL]
- API Reference: [Your API docs]
- Contributing Guide: [Your contributing.md]
