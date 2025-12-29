"""
Questionnaire View

This module provides the UI for completing OpenSAMM questionnaires.
It displays questions, collects responses, and shows progress.
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QRadioButton, QButtonGroup, QTextEdit, QLineEdit, QProgressBar,
    QGroupBox, QScrollArea, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

from models.assessment_model import ResponseType
from models.questionnaire_model import Question
from controllers.questionnaire_controller import QuestionnaireController


class QuestionnaireView(QWidget):
    """
    Widget for displaying and completing questionnaires.

    Provides a user-friendly interface for answering assessment questions
    with navigation, response options, and progress tracking.

    Signals:
        questionnaire_completed: Emitted when all questions are answered
        questionnaire_closed: Emitted when view is closed
    """

    questionnaire_completed = pyqtSignal()
    questionnaire_closed = pyqtSignal()

    def __init__(self, controller: QuestionnaireController, parent=None):
        """
        Initialize questionnaire view.

        Args:
            controller: QuestionnaireController instance
            parent: Parent widget
        """
        super().__init__(parent)

        self.controller = controller

        # Connect controller signals
        self.controller.response_added.connect(self._on_response_added)
        self.controller.progress_updated.connect(self._on_progress_updated)
        self.controller.questionnaire_completed.connect(self._on_completed)

        self._setup_ui()
        self._display_current_question()

    def _setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)

        # Header section
        header_layout = self._create_header()
        layout.addLayout(header_layout)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        layout.addWidget(self.progress_bar)

        # Progress label
        self.progress_label = QLabel()
        layout.addWidget(self.progress_label)

        # Question section (scrollable)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        question_widget = QWidget()
        self.question_layout = QVBoxLayout(question_widget)
        scroll.setWidget(question_widget)

        layout.addWidget(scroll, 1)  # Takes remaining space

        # Navigation section
        nav_layout = self._create_navigation()
        layout.addLayout(nav_layout)

        # Update initial progress
        self._update_progress_display()

    def _create_header(self) -> QHBoxLayout:
        """Create the header section."""
        layout = QHBoxLayout()

        # Title
        self.title_label = QLabel()
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(14)
        self.title_label.setFont(title_font)
        layout.addWidget(self.title_label, 1)

        # Close button
        close_btn = QPushButton("Close Questionnaire")
        close_btn.clicked.connect(self._on_close_clicked)
        layout.addWidget(close_btn)

        return layout

    def _create_navigation(self) -> QHBoxLayout:
        """Create navigation buttons."""
        layout = QHBoxLayout()

        # Previous button
        self.prev_btn = QPushButton("← Previous")
        self.prev_btn.clicked.connect(self._on_previous_clicked)
        layout.addWidget(self.prev_btn)

        # Question position label
        self.position_label = QLabel()
        layout.addWidget(self.position_label, 1)  # Center align

        # Next button
        self.next_btn = QPushButton("Next →")
        self.next_btn.clicked.connect(self._on_next_clicked)
        layout.addWidget(self.next_btn)

        # Save button
        save_btn = QPushButton("💾 Save")
        save_btn.clicked.connect(self._on_save_clicked)
        layout.addWidget(save_btn)

        return layout

    def _clear_question_layout(self):
        """Clear the question layout."""
        while self.question_layout.count():
            item = self.question_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def _display_current_question(self):
        """Display the current question."""
        self._clear_question_layout()

        question = self.controller.get_current_question()
        if not question:
            self._display_no_questions()
            return

        # Update title
        self.title_label.setText(question.get_display_title())

        # Section and practice info
        info_label = QLabel(
            f"<b>Practice:</b> {question.practice_name} | "
            f"<b>Maturity Level:</b> {question.level}"
        )
        self.question_layout.addWidget(info_label)

        # Question text
        q_label = QLabel(f"<h3>{question.get_full_display()}</h3>")
        q_label.setWordWrap(True)
        self.question_layout.addWidget(q_label)

        # Guidance
        if question.guidance:
            guidance_box = QGroupBox("Guidance")
            guidance_layout = QVBoxLayout()
            guidance_text = QLabel(question.guidance)
            guidance_text.setWordWrap(True)
            guidance_text.setStyleSheet("color: #555;")
            guidance_layout.addWidget(guidance_text)
            guidance_box.setLayout(guidance_layout)
            self.question_layout.addWidget(guidance_box)

        # Response options
        response_group = self._create_response_group(question)
        self.question_layout.addWidget(response_group)

        # Notes section
        notes_group = self._create_notes_group(question)
        self.question_layout.addWidget(notes_group)

        # Evidence section
        evidence_group = self._create_evidence_group(question)
        self.question_layout.addWidget(evidence_group)

        # Spacer
        self.question_layout.addStretch()

        # Update navigation
        self._update_navigation()

    def _create_response_group(self, question: Question) -> QGroupBox:
        """Create response radio buttons."""
        group_box = QGroupBox("Response *")
        layout = QVBoxLayout()

        # Create button group
        self.response_button_group = QButtonGroup(self)

        # Response options
        responses = [
            (ResponseType.YES, "Yes - Fully implemented"),
            (ResponseType.PARTIAL, "Partial - Partially implemented"),
            (ResponseType.NO, "No - Not implemented"),
            (ResponseType.NOT_APPLICABLE, "N/A - Not applicable")
        ]

        for response_type, label in responses:
            radio = QRadioButton(label)
            radio.setProperty("response_type", response_type)
            self.response_button_group.addButton(radio)
            layout.addWidget(radio)

        # Load existing response
        existing_response = self.controller.get_response(question)
        if existing_response:
            for button in self.response_button_group.buttons():
                if button.property("response_type") == existing_response.response:
                    button.setChecked(True)
                    break

        # Connect signal
        self.response_button_group.buttonClicked.connect(
            lambda: self._on_response_changed(question)
        )

        group_box.setLayout(layout)
        return group_box

    def _create_notes_group(self, question: Question) -> QGroupBox:
        """Create notes input."""
        group_box = QGroupBox("Notes (Optional)")
        layout = QVBoxLayout()

        self.notes_text = QTextEdit()
        self.notes_text.setPlaceholderText("Add any additional notes or context...")
        self.notes_text.setMaximumHeight(100)

        # Load existing notes
        existing_response = self.controller.get_response(question)
        if existing_response:
            self.notes_text.setPlainText(existing_response.notes)

        # Connect signal
        self.notes_text.textChanged.connect(
            lambda: self._on_notes_changed(question)
        )

        layout.addWidget(self.notes_text)
        group_box.setLayout(layout)
        return group_box

    def _create_evidence_group(self, question: Question) -> QGroupBox:
        """Create evidence input."""
        group_box = QGroupBox("Evidence (Optional)")
        layout = QVBoxLayout()

        self.evidence_edit = QLineEdit()
        self.evidence_edit.setPlaceholderText("Reference to supporting documentation or evidence...")

        # Load existing evidence
        existing_response = self.controller.get_response(question)
        if existing_response:
            self.evidence_edit.setText(existing_response.evidence)

        # Connect signal
        self.evidence_edit.textChanged.connect(
            lambda: self._on_evidence_changed(question)
        )

        layout.addWidget(self.evidence_edit)
        group_box.setLayout(layout)
        return group_box

    def _display_no_questions(self):
        """Display message when no questions available."""
        label = QLabel("No questions available.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_layout.addWidget(label)

    def _update_navigation(self):
        """Update navigation button states."""
        self.prev_btn.setEnabled(self.controller.has_previous_question())
        self.next_btn.setEnabled(self.controller.has_next_question())

        # Update position label
        section = self.controller.get_current_section()
        if section:
            section_idx = self.controller.current_section_index + 1
            total_sections = len(self.controller.questionnaire.sections)
            q_idx = self.controller.current_question_index + 1
            total_q = section.get_question_count()

            self.position_label.setText(
                f"Section {section_idx}/{total_sections} | "
                f"Question {q_idx}/{total_q}"
            )

    def _update_progress_display(self):
        """Update progress bar and label."""
        progress = self.controller.get_progress()

        self.progress_bar.setValue(int(progress['percentage']))
        self.progress_label.setText(
            f"Progress: {progress['completed']} of {progress['total']} questions "
            f"({progress['percentage']:.1f}%)"
        )

    def _on_response_changed(self, question: Question):
        """Handle response selection change."""
        checked_button = self.response_button_group.checkedButton()
        if checked_button:
            response_type = checked_button.property("response_type")

            # Get current notes and evidence
            notes = self.notes_text.toPlainText()
            evidence = self.evidence_edit.text()

            # Add/update response
            self.controller.add_response(
                question,
                response_type,
                notes=notes,
                evidence=evidence
            )

    def _on_notes_changed(self, question: Question):
        """Handle notes text change."""
        # Only update if there's already a response
        existing_response = self.controller.get_response(question)
        if existing_response:
            existing_response.notes = self.notes_text.toPlainText()
            self.controller.assessment.updated_at = self.controller.assessment.updated_at
            self.controller._auto_save()

    def _on_evidence_changed(self, question: Question):
        """Handle evidence text change."""
        # Only update if there's already a response
        existing_response = self.controller.get_response(question)
        if existing_response:
            existing_response.evidence = self.evidence_edit.text()
            self.controller.assessment.updated_at = self.controller.assessment.updated_at
            self.controller._auto_save()

    def _on_previous_clicked(self):
        """Handle previous button click."""
        self.controller.previous_question()
        self._display_current_question()

    def _on_next_clicked(self):
        """Handle next button click."""
        self.controller.next_question()
        self._display_current_question()

    def _on_save_clicked(self):
        """Handle save button click."""
        if self.controller.save():
            self.progress_label.setText(
                self.progress_label.text() + " ✓ Saved"
            )

    def _on_close_clicked(self):
        """Handle close button click."""
        # Save before closing
        self.controller.save()
        self.questionnaire_closed.emit()
        # Close the window
        self.close()

    def _on_response_added(self, question_id: str, response_type: str):
        """Handle response added signal from controller."""
        # Progress will be updated automatically via progress_updated signal
        pass

    def _on_progress_updated(self, completed: int, total: int, percentage: float):
        """Handle progress update from controller."""
        self._update_progress_display()

    def _on_completed(self):
        """Handle questionnaire completion."""
        self.questionnaire_completed.emit()


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    from models.opensamm_model import load_opensamm_model
    from models.questionnaire_model import create_level1_questionnaire
    from models.assessment_model import Assessment
    from services.database_service import DatabaseService

    app = QApplication(sys.argv)

    # Setup
    samm_model = load_opensamm_model()
    questionnaire = create_level1_questionnaire(samm_model)
    assessment = Assessment(name="Test Assessment", organization="Test Org")
    db = DatabaseService(":memory:")

    # Save assessment first
    assessment.id = db.save_assessment(assessment)

    # Create controller
    controller = QuestionnaireController(assessment, questionnaire, db)

    # Create view
    view = QuestionnaireView(controller)
    view.setWindowTitle("HAIAMM - Questionnaire Test")
    view.resize(800, 600)
    view.show()

    sys.exit(app.exec())
