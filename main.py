#!/usr/bin/env python3
"""
HAIAMM - Human-Assisted Intelligence Assurance Maturity Model

Main entry point for the application.

This desktop application helps organizations track and assess AI system security maturity
using the Human-Assisted Intelligence Assurance Maturity Model (HAIAMM), which extends
OpenSAMM with multi-domain support for comprehensive HAI security assessment.
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from views.main_window import MainWindow


def main():
    """Main application entry point."""
    # Create application
    app = QApplication(sys.argv)

    # Set application metadata
    app.setApplicationName("HAIAMM")
    app.setApplicationDisplayName("HAIAMM - Human-Assisted Intelligence Assurance Maturity Model")
    app.setOrganizationName("HAIAMM")
    app.setOrganizationDomain("haiamm.local")

    # TODO: Set application icon when available
    # icon_path = project_root / "resources" / "icons" / "app.png"
    # if icon_path.exists():
    #     app.setWindowIcon(QIcon(str(icon_path)))

    # Create and show main window
    window = MainWindow()
    window.show()

    # Run application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
