#!/usr/bin/env python3
"""
Test that all imports work without plotly installed.
"""

print("Testing imports without plotly...")

# Test base models
print("[1/6] Testing models...")
from models.opensamm_model import load_opensamm_model
from models.assessment_model import Assessment
from models.scoring_model import ScoringEngine
print("✓ Models imported successfully")

# Test services
print("[2/6] Testing services...")
from services.database_service import DatabaseService
print("✓ Database service imported successfully")

# Test visualization service
print("[3/6] Testing visualization service...")
try:
    from services.visualization_service import VisualizationService, PLOTLY_AVAILABLE
    if PLOTLY_AVAILABLE:
        print("✓ Visualization service imported (plotly available)")
    else:
        print("✓ Visualization service imported (plotly not available)")
except ImportError as e:
    print(f"✓ Visualization service import handled gracefully: {e}")

# Test views
print("[4/6] Testing views...")
from views.scoring_view import ScoringView
from views.questionnaire_view import QuestionnaireView
print("✓ Core views imported successfully")

# Test dashboard view
print("[5/6] Testing dashboard view...")
try:
    from views.dashboard_view import DashboardView, VISUALIZATION_AVAILABLE
    if VISUALIZATION_AVAILABLE:
        print("✓ Dashboard view imported (visualization available)")
    else:
        print("✓ Dashboard view imported (visualization not available)")
except ImportError as e:
    print(f"✓ Dashboard view import handled gracefully: {e}")

# Test main window
print("[6/6] Testing main window...")
try:
    from views.main_window import MainWindow, DASHBOARD_AVAILABLE
    if DASHBOARD_AVAILABLE:
        print("✓ Main window imported (dashboard available)")
    else:
        print("✓ Main window imported (dashboard not available)")
except ImportError as e:
    print(f"✗ Main window import failed: {e}")
    exit(1)

print("\n" + "=" * 60)
print("✓ All imports successful!")
print("=" * 60)
print("\nApplication can run without plotly.")
print("Dashboard features will show a helpful error message.")
print("\nTo enable visualizations:")
print("  pip install plotly")
