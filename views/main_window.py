"""
Main Window

This module defines the main application window for HAIAMM.
It provides the primary user interface with menus, toolbars, and navigation.
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QMessageBox, QInputDialog,
    QListWidget, QListWidgetItem, QSplitter, QTextEdit,
    QMenuBar, QMenu, QStatusBar
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction, QFont
from typing import Optional, List

from models.assessment_model import Assessment
from models.opensamm_model import OpenSAMMModel, load_opensamm_model
from models.haiamm_model import HAIAMMModel, load_haiamm_model
from models.questionnaire_model import Questionnaire, create_full_questionnaire
from services.database_service import DatabaseService
from controllers.questionnaire_controller import QuestionnaireController
from views.assessment_wizard import AssessmentWizard
from views.questionnaire_view import QuestionnaireView
from views.scoring_view import ScoringView

# Dashboard requires plotly - import conditionally
try:
    from views.dashboard_view import DashboardView
    DASHBOARD_AVAILABLE = True
except ImportError:
    DASHBOARD_AVAILABLE = False
    DashboardView = None


class MainWindow(QMainWindow):
    """
    Main application window for HAIAMM.

    Provides the primary interface for managing assessments, viewing dashboards,
    and accessing all application features.
    """

    def __init__(self):
        """Initialize the main window."""
        super().__init__()

        self.setWindowTitle("HAIAMM - Human-Assisted Intelligence Assurance Maturity Model")
        self.setGeometry(100, 100, 1200, 800)

        # Initialize services and models
        self.db_service = DatabaseService()
        self.samm_model = None
        self.model_load_status = ""

        try:
            # Load HAIAMM multi-domain model
            self.samm_model = load_haiamm_model()
            print(f"✓ HAIAMM model loaded successfully: {self.samm_model}")
            self.model_load_status = (
                f"Loaded HAIAMM v{self.samm_model.version} - "
                f"{self.samm_model.get_domain_count()} domains, "
                f"{self.samm_model.get_total_practices()} practices, "
                f"{self.samm_model.get_total_questions()} questions"
            )
        except Exception as e:
            self.samm_model = None
            print(f"✗ Failed to load HAIAMM model: {e}")
            import traceback
            traceback.print_exc()
            self.model_load_status = f"Error: Failed to load HAIAMM model"
            QMessageBox.critical(
                self,
                "Error Loading Model",
                f"Failed to load HAIAMM model: {e}\n\n"
                f"Please check that config/haiamm_multi_domain_data.json exists."
            )

        self.current_assessment: Optional[Assessment] = None
        self.questionnaire_window: Optional[QuestionnaireView] = None
        self.dashboard_window: Optional[DashboardView] = None
        self.scoring_window: Optional[ScoringView] = None

        # Setup UI
        self._setup_menu_bar()
        self._setup_central_widget()
        self._setup_status_bar()

        # Show model load status
        if self.model_load_status:
            self.status_message(self.model_load_status)

        # Load assessments
        self.refresh_assessment_list()

    def _setup_menu_bar(self):
        """Create the menu bar."""
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("&File")

        new_action = QAction("&New Assessment...", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_assessment)
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Assessment menu
        assessment_menu = menubar.addMenu("&Assessment")

        load_action = QAction("&Load Assessment", self)
        load_action.setShortcut("Ctrl+L")
        load_action.triggered.connect(self.load_selected_assessment)
        assessment_menu.addAction(load_action)

        assessment_menu.addSeparator()

        questionnaire_action = QAction("Start &Questionnaire...", self)
        questionnaire_action.setShortcut("Ctrl+Q")
        questionnaire_action.triggered.connect(self.start_questionnaire)
        assessment_menu.addAction(questionnaire_action)

        assessment_menu.addSeparator()

        dashboard_action = QAction("View &Dashboard...", self)
        dashboard_action.setShortcut("Ctrl+B")
        dashboard_action.triggered.connect(self.show_dashboard)
        assessment_menu.addAction(dashboard_action)

        scoring_action = QAction("View &Scoring Report...", self)
        scoring_action.setShortcut("Ctrl+R")
        scoring_action.triggered.connect(self.show_scoring)
        assessment_menu.addAction(scoring_action)

        assessment_menu.addSeparator()

        delete_action = QAction("&Delete Assessment", self)
        delete_action.setShortcut("Ctrl+D")
        delete_action.triggered.connect(self.delete_selected_assessment)
        assessment_menu.addAction(delete_action)

        # Help menu
        help_menu = menubar.addMenu("&Help")

        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def _setup_central_widget(self):
        """Create the central widget layout."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        # Left panel: Assessment list
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # Title
        title_label = QLabel("Assessments")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(12)
        title_label.setFont(title_font)
        left_layout.addWidget(title_label)

        # New assessment button
        new_btn = QPushButton("New Assessment")
        new_btn.clicked.connect(self.new_assessment)
        left_layout.addWidget(new_btn)

        # Assessment list
        self.assessment_list = QListWidget()
        self.assessment_list.itemDoubleClicked.connect(
            lambda: self.load_selected_assessment()
        )
        left_layout.addWidget(self.assessment_list)

        # Action buttons
        button_layout = QHBoxLayout()

        load_btn = QPushButton("Load")
        load_btn.clicked.connect(self.load_selected_assessment)
        button_layout.addWidget(load_btn)

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(self.delete_selected_assessment)
        button_layout.addWidget(delete_btn)

        left_layout.addLayout(button_layout)

        # Right panel: Assessment details
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        # Info label
        self.info_label = QLabel("No assessment loaded")
        info_font = QFont()
        info_font.setBold(True)
        info_font.setPointSize(11)
        self.info_label.setFont(info_font)
        right_layout.addWidget(self.info_label)

        # Details text
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setPlaceholderText(
            "Select or create an assessment to view details..."
        )
        right_layout.addWidget(self.details_text)

        # Action buttons layout
        buttons_layout = QHBoxLayout()

        # Start Questionnaire button
        self.start_q_btn = QPushButton("📝 Questionnaire")
        self.start_q_btn.setEnabled(False)
        self.start_q_btn.clicked.connect(self.start_questionnaire)
        self.start_q_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                padding: 10px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        buttons_layout.addWidget(self.start_q_btn)

        # Dashboard button
        self.dashboard_btn = QPushButton("📊 Dashboard")
        self.dashboard_btn.setEnabled(False)
        self.dashboard_btn.clicked.connect(self.show_dashboard)
        self.dashboard_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                padding: 10px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        buttons_layout.addWidget(self.dashboard_btn)

        # Scoring button
        self.scoring_btn = QPushButton("📋 Scoring")
        self.scoring_btn.setEnabled(False)
        self.scoring_btn.clicked.connect(self.show_scoring)
        self.scoring_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-weight: bold;
                padding: 10px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        buttons_layout.addWidget(self.scoring_btn)

        right_layout.addLayout(buttons_layout)

        # Add panels to splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)

        layout.addWidget(splitter)

    def _setup_status_bar(self):
        """Create the status bar."""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_message("Ready")

    def status_message(self, message: str, timeout: int = 5000):
        """
        Display a status message.

        Args:
            message: Message to display
            timeout: How long to show the message (milliseconds)
        """
        self.statusBar().showMessage(message, timeout)

    def refresh_assessment_list(self):
        """Refresh the list of assessments from the database."""
        self.assessment_list.clear()

        try:
            assessments = self.db_service.list_assessments()
            for assessment_data in assessments:
                item_text = (
                    f"{assessment_data['name']} - "
                    f"{assessment_data['organization']} "
                    f"({assessment_data['response_count']} responses)"
                )
                item = QListWidgetItem(item_text)
                item.setData(Qt.ItemDataRole.UserRole, assessment_data['id'])
                self.assessment_list.addItem(item)

            self.status_message(f"Loaded {len(assessments)} assessment(s)")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to load assessments: {e}"
            )

    def new_assessment(self):
        """Create a new assessment using the wizard."""
        if not self.samm_model:
            QMessageBox.warning(
                self,
                "Model Not Loaded",
                "HAIAMM model failed to load. Cannot create assessment."
            )
            return

        # Show wizard
        wizard = AssessmentWizard(self.samm_model, self)
        result = wizard.exec()

        if result == wizard.DialogCode.Accepted:
            assessment = wizard.get_assessment()
            questionnaire = wizard.get_questionnaire()

            try:
                # Save assessment
                assessment_id = self.db_service.save_assessment(assessment)
                self.status_message(f"Created assessment: {assessment.name}")
                self.refresh_assessment_list()

                # Load the new assessment
                self.current_assessment = self.db_service.load_assessment(assessment_id)
                self.display_assessment_details()

                # Ask if user wants to start questionnaire now
                reply = QMessageBox.question(
                    self,
                    "Start Questionnaire?",
                    f"Assessment '{assessment.name}' created successfully.\n\n"
                    f"Would you like to start the questionnaire now?\n"
                    f"({questionnaire.get_total_questions()} questions)",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )

                if reply == QMessageBox.StandardButton.Yes:
                    self.start_questionnaire()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Failed to create assessment: {e}"
                )

    def load_selected_assessment(self):
        """Load the selected assessment."""
        current_item = self.assessment_list.currentItem()
        if not current_item:
            QMessageBox.warning(
                self,
                "No Selection",
                "Please select an assessment to load."
            )
            return

        assessment_id = current_item.data(Qt.ItemDataRole.UserRole)

        try:
            self.current_assessment = self.db_service.load_assessment(assessment_id)
            if self.current_assessment:
                self.display_assessment_details()
                self.status_message(
                    f"Loaded assessment: {self.current_assessment.name}"
                )
            else:
                QMessageBox.warning(
                    self,
                    "Not Found",
                    f"Assessment {assessment_id} not found."
                )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to load assessment: {e}"
            )

    def delete_selected_assessment(self):
        """Delete the selected assessment."""
        current_item = self.assessment_list.currentItem()
        if not current_item:
            QMessageBox.warning(
                self,
                "No Selection",
                "Please select an assessment to delete."
            )
            return

        assessment_id = current_item.data(Qt.ItemDataRole.UserRole)
        assessment_name = current_item.text().split(" - ")[0]

        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete '{assessment_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                if self.db_service.delete_assessment(assessment_id):
                    self.status_message(f"Deleted assessment: {assessment_name}")
                    self.refresh_assessment_list()

                    # Clear current assessment if it was deleted
                    if (self.current_assessment and
                        self.current_assessment.id == assessment_id):
                        self.current_assessment = None
                        self.display_assessment_details()
                else:
                    QMessageBox.warning(
                        self,
                        "Not Found",
                        f"Assessment {assessment_id} not found."
                    )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Failed to delete assessment: {e}"
                )

    def display_assessment_details(self):
        """Display details of the current assessment."""
        if not self.current_assessment:
            self.info_label.setText("No assessment loaded")
            self.details_text.setPlainText("")
            self.start_q_btn.setEnabled(False)
            self.dashboard_btn.setEnabled(False)
            self.scoring_btn.setEnabled(False)
            return

        # Enable all buttons
        self.start_q_btn.setEnabled(True)
        self.dashboard_btn.setEnabled(True)
        self.scoring_btn.setEnabled(True)

        a = self.current_assessment

        # Update info label
        self.info_label.setText(
            f"Assessment: {a.name} (ID: {a.id})"
        )

        # Build details text
        details = []
        details.append(f"Name: {a.name}")
        details.append(f"Organization: {a.organization}")
        details.append(f"Assessor: {a.assessor}")
        details.append(f"Description: {a.description}")
        details.append(f"Created: {a.created_at.strftime('%Y-%m-%d %H:%M')}")
        details.append(f"Updated: {a.updated_at.strftime('%Y-%m-%d %H:%M')}")
        details.append(f"\nResponses: {a.get_response_count()}")

        if self.samm_model:
            total_q = self.samm_model.get_total_questions()
            completion = a.get_completion_percentage(total_q)
            details.append(f"Completion: {completion:.1f}% ({a.get_response_count()}/{total_q})")

        if a.has_responses():
            details.append("\n--- Sample Responses ---")
            for i, (qid, response) in enumerate(list(a.responses.items())[:5]):
                details.append(
                    f"{response.practice_id.upper()} L{response.level} - "
                    f"{qid}: {response.response.value}"
                )
                if i >= 4:
                    break
            if len(a.responses) > 5:
                details.append(f"... and {len(a.responses) - 5} more")

        self.details_text.setPlainText("\n".join(details))

    def start_questionnaire(self):
        """Start the questionnaire for the current assessment."""
        if not self.current_assessment:
            QMessageBox.warning(
                self,
                "No Assessment",
                "Please create or load an assessment first."
            )
            return

        if not self.samm_model:
            QMessageBox.warning(
                self,
                "Model Not Loaded",
                "HAIAMM model not available."
            )
            return

        # Check if questionnaire window is already open
        if self.questionnaire_window and self.questionnaire_window.isVisible():
            self.questionnaire_window.raise_()
            self.questionnaire_window.activateWindow()
            return

        # Create questionnaire (full assessment by default)
        # TEMPORARY: For multi-domain HAIAMM, use Software domain as default
        try:
            if isinstance(self.samm_model, HAIAMMModel):
                # Get Software domain and create OpenSAMM-compatible wrapper
                software_domain = self.samm_model.get_domain('software')
                if not software_domain:
                    raise ValueError("Software domain not found")

                # Create temporary wrapper for compatibility
                from models.opensamm_model import OpenSAMMModel
                temp_model = OpenSAMMModel()
                temp_model.version = "1.0"
                temp_model.model_name = "HAIAMM - Software Domain"
                temp_model.description = software_domain.description
                temp_model.business_functions = software_domain.business_functions
                temp_model._build_practice_index()

                questionnaire = create_full_questionnaire(temp_model)
            else:
                questionnaire = create_full_questionnaire(self.samm_model)
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error Creating Questionnaire",
                f"Failed to create questionnaire: {str(e)}\n\n"
                f"Note: Multi-domain questionnaire selection is in development.\n"
                f"Currently showing Software domain by default."
            )
            return

        # Create controller
        controller = QuestionnaireController(
            self.current_assessment,
            questionnaire,
            self.db_service
        )

        # Create and show questionnaire window
        self.questionnaire_window = QuestionnaireView(controller)
        domain_note = " (Software Domain)" if isinstance(self.samm_model, HAIAMMModel) else ""
        self.questionnaire_window.setWindowTitle(
            f"HAIAMM - {self.current_assessment.name}{domain_note}"
        )
        self.questionnaire_window.resize(900, 700)

        # Connect signals
        self.questionnaire_window.questionnaire_closed.connect(self._on_questionnaire_closed)
        self.questionnaire_window.questionnaire_completed.connect(self._on_questionnaire_completed)

        self.questionnaire_window.show()
        self.status_message(f"Opened questionnaire: {questionnaire.name}")

    def _on_questionnaire_closed(self):
        """Handle questionnaire window closed."""
        # Reload assessment to get updates
        if self.current_assessment and self.current_assessment.id:
            self.current_assessment = self.db_service.load_assessment(
                self.current_assessment.id
            )
            self.display_assessment_details()
            self.refresh_assessment_list()

        self.status_message("Questionnaire closed")

    def _on_questionnaire_completed(self):
        """Handle questionnaire completion."""
        QMessageBox.information(
            self,
            "Questionnaire Complete!",
            f"Congratulations! You have completed all questions in the questionnaire.\n\n"
            f"Assessment: {self.current_assessment.name}\n"
            f"Total responses: {self.current_assessment.get_response_count()}"
        )

    def show_dashboard(self):
        """Show the dashboard for the current assessment."""
        # Check if dashboard is available (requires plotly)
        if not DASHBOARD_AVAILABLE:
            QMessageBox.warning(
                self,
                "Plotly Not Installed",
                "Dashboard visualizations require plotly.\n\n"
                "Install with: pip install plotly\n\n"
                "You can still use the Scoring view for detailed score tables."
            )
            return

        if not self.current_assessment:
            QMessageBox.warning(
                self,
                "No Assessment",
                "Please create or load an assessment first."
            )
            return

        if not self.samm_model:
            QMessageBox.warning(
                self,
                "Model Not Loaded",
                "HAIAMM model not available."
            )
            return

        # Check if responses exist
        if self.current_assessment.get_response_count() == 0:
            reply = QMessageBox.question(
                self,
                "No Responses",
                "This assessment has no responses yet. The dashboard will show empty scores.\n\n"
                "Do you want to start the questionnaire first?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.start_questionnaire()
                return

        # Check if dashboard window is already open
        if self.dashboard_window and self.dashboard_window.isVisible():
            self.dashboard_window.raise_()
            self.dashboard_window.activateWindow()
            return

        # Create and show dashboard
        try:
            self.dashboard_window = DashboardView(
                self.current_assessment,
                self.samm_model
            )
            self.dashboard_window.setWindowTitle(
                f"HAIAMM - Dashboard: {self.current_assessment.name}"
            )
            self.dashboard_window.resize(1000, 700)
            self.dashboard_window.show()
            self.status_message("Dashboard opened")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to open dashboard: {e}\n\n"
                f"Make sure plotly is installed: pip install plotly"
            )

    def show_scoring(self):
        """Show the scoring report for the current assessment."""
        if not self.current_assessment:
            QMessageBox.warning(
                self,
                "No Assessment",
                "Please create or load an assessment first."
            )
            return

        if not self.samm_model:
            QMessageBox.warning(
                self,
                "Model Not Loaded",
                "HAIAMM model not available."
            )
            return

        # Check if responses exist
        if self.current_assessment.get_response_count() == 0:
            reply = QMessageBox.question(
                self,
                "No Responses",
                "This assessment has no responses yet. The scoring report will show zeros.\n\n"
                "Do you want to start the questionnaire first?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.start_questionnaire()
                return

        # Check if scoring window is already open
        if self.scoring_window and self.scoring_window.isVisible():
            self.scoring_window.raise_()
            self.scoring_window.activateWindow()
            return

        # Create and show scoring view
        try:
            self.scoring_window = ScoringView(
                self.current_assessment,
                self.samm_model
            )
            self.scoring_window.setWindowTitle(
                f"HAIAMM - Scoring Report: {self.current_assessment.name}"
            )
            self.scoring_window.resize(1000, 600)
            self.scoring_window.show()
            self.status_message("Scoring report opened")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to open scoring report: {e}"
            )

    def show_about(self):
        """Show the About dialog."""
        about_text = """
        <h2>HAIAMM</h2>
        <p><b>Human-Assisted Intelligence Assurance Maturity Model</b></p>
        <p>Version 1.0.0</p>
        <p>A desktop application for tracking and assessing AI system security maturity
        using the Human-Assisted Intelligence Assurance Maturity Model (HAIAMM), which extends
        OpenSAMM with multi-domain support for comprehensive HAI security assessment.</p>
        <p><b>HAIAMM v1.0 Coverage:</b></p>
        <ul>
        <li>6 Security Domains (Software, Infrastructure, Endpoints, Data, Processes, Vendors)</li>
        <li>4 Business Functions per Domain</li>
        <li>78 Security Practices (13 per domain)</li>
        <li>234 Maturity Levels (3 per practice)</li>
        <li>702 Assessment Criteria</li>
        </ul>
        <p>Built with PyQt6, Python, and based on OpenSAMM v1.0.</p>
        """
        QMessageBox.about(self, "About HAIAMM", about_text)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setApplicationName("HAIAMM")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
