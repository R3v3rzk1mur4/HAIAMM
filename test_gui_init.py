#!/usr/bin/env python3
"""
Test GUI initialization to debug model loading issue.
"""

import sys
from PyQt6.QtWidgets import QApplication

print("Testing GUI initialization...")

# Create QApplication
app = QApplication(sys.argv)
print("✓ QApplication created")

# Test model loading
print("\nTesting model loading...")
from models.opensamm_model import load_opensamm_model

try:
    model = load_opensamm_model()
    print(f"✓ Model loaded: {model}")
except Exception as e:
    print(f"✗ Model loading failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test MainWindow initialization
print("\nTesting MainWindow initialization...")
try:
    from views.main_window import MainWindow
    window = MainWindow()
    print(f"✓ MainWindow created")
    print(f"  - samm_model: {window.samm_model}")
    print(f"  - db_service: {window.db_service}")
except Exception as e:
    print(f"✗ MainWindow initialization failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ All initialization tests passed!")
print("=" * 60)
