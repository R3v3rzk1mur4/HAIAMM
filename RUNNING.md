# Running HAIAMM

## Quick Start

### Without Visualization (Minimal Installation)

The application can run with core functionality without plotly:

```bash
python3 main.py
```

**Available features:**
- ✅ Create and manage assessments
- ✅ Complete OpenSAMM questionnaires
- ✅ Calculate maturity scores
- ✅ View detailed scoring tables
- ⚠️ Dashboard visualizations (requires plotly)

### With Full Visualization Support

Install plotly for dashboard charts:

```bash
pip install plotly
python3 main.py
```

**Additional features with plotly:**
- ✅ Interactive radar charts (12 practices)
- ✅ Business function bar charts
- ✅ Maturity heatmaps
- ✅ Comprehensive dashboard

## Testing

### Run Phase Tests

```bash
# Phase 1: Foundation
python3 test_phase1.py

# Phase 2: Questionnaire Engine
python3 test_phase2.py

# Phase 3: Scoring & Visualization (requires plotly for full test)
python3 test_phase3.py

# Import test (works without plotly)
python3 test_imports.py
```

## Application Features

### Current Status (Phase 1-3 Complete)

1. **Assessment Management**
   - Create new assessments
   - Load existing assessments
   - Delete assessments
   - SQLite database persistence

2. **Questionnaire Engine**
   - Dynamic questionnaire generation
   - Full questionnaire (108 questions, all 12 practices)
   - Level 1 only questionnaire (36 questions)
   - Custom questionnaires (select practices and levels)
   - Progress tracking
   - Auto-save responses

3. **Scoring & Analysis**
   - OpenSAMM maturity scoring (≥80% = level achieved)
   - Per-practice scores (0-3 scale)
   - Business function averages
   - Overall organizational maturity
   - Detailed scoring tables

4. **Visualization** (optional, requires plotly)
   - Radar chart (all 12 practices)
   - Bar chart (4 business functions)
   - Heatmap (4×3 maturity grid)
   - Interactive dashboard

## User Interface

### Main Window
- Assessment list
- Create/Load/Delete buttons
- Start Questionnaire
- View Dashboard (requires plotly)
- View Scoring Report

### Keyboard Shortcuts
- `Ctrl+N` - New Assessment
- `Ctrl+O` - Open Assessment
- `Ctrl+Q` - Start Questionnaire
- `Ctrl+B` - View Dashboard
- `Ctrl+R` - View Scoring Report

## Error Handling

If you try to use Dashboard without plotly installed, you'll see:
> "Dashboard visualizations require plotly.
>
> Install with: pip install plotly
>
> You can still use the Scoring view for detailed score tables."

## Next Phases (Not Yet Implemented)

- Phase 4: Export & Encryption (JSON/CSV, PGP)
- Phase 5: Version Control & Undo/Redo
- Phase 6: Roadmap Planning
- Phase 7: Comparison & History
- Phase 8: Polish & Packaging
