"""
Assessment Wizard

This module provides a wizard dialog for creating new assessments
with questionnaire customization options.
"""

from PyQt6.QtWidgets import (
    QWizard, QWizardPage, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QTextEdit, QRadioButton, QButtonGroup,
    QCheckBox, QGroupBox, QMessageBox
)
from PyQt6.QtCore import Qt

from models.assessment_model import Assessment
from models.opensamm_model import OpenSAMMModel
from models.questionnaire_model import (
    Questionnaire, create_full_questionnaire,
    create_level1_questionnaire
)


class AssessmentInfoPage(QWizardPage):
    """First page: Assessment metadata."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Assessment Information")
        self.setSubTitle("Enter basic information about this assessment.")

        layout = QFormLayout(self)

        # Name
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("e.g., Q4 2025 Security Assessment")
        layout.addRow("Assessment Name *:", self.name_edit)
        self.registerField("name*", self.name_edit)

        # Organization
        self.org_edit = QLineEdit()
        self.org_edit.setPlaceholderText("e.g., Acme Corporation")
        layout.addRow("Organization:", self.org_edit)
        self.registerField("organization", self.org_edit)

        # Assessor
        self.assessor_edit = QLineEdit()
        self.assessor_edit.setPlaceholderText("e.g., Security Team")
        layout.addRow("Assessor:", self.assessor_edit)
        self.registerField("assessor", self.assessor_edit)

        # Description
        self.desc_edit = QTextEdit()
        self.desc_edit.setPlaceholderText("Optional description...")
        self.desc_edit.setMaximumHeight(100)
        layout.addRow("Description:", self.desc_edit)


class QuestionnaireTypePage(QWizardPage):
    """Second page: Questionnaire type selection."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Questionnaire Type")
        self.setSubTitle("Choose the type of assessment questionnaire.")

        layout = QVBoxLayout(self)

        # Radio buttons for questionnaire types
        self.button_group = QButtonGroup(self)

        # Full assessment
        self.full_radio = QRadioButton("Full Assessment (All Practices, All Levels)")
        self.full_radio.setChecked(True)
        desc_label1 = QLabel(
            "   Comprehensive assessment covering all 12 security practices "
            "across 3 maturity levels (108 questions)."
        )
        desc_label1.setWordWrap(True)
        desc_label1.setStyleSheet("color: #555; font-size: 10pt;")

        # Level 1 only
        self.level1_radio = QRadioButton("Level 1 Assessment (Initial Maturity)")
        desc_label2 = QLabel(
            "   Focused assessment covering Level 1 maturity for all 12 practices "
            "(36 questions). Good for initial baseline."
        )
        desc_label2.setWordWrap(True)
        desc_label2.setStyleSheet("color: #555; font-size: 10pt;")

        # Custom (future)
        self.custom_radio = QRadioButton("Custom Assessment (Select Specific Practices)")
        self.custom_radio.setEnabled(False)  # TODO: Implement in Phase 2+
        desc_label3 = QLabel(
            "   Create a customized questionnaire by selecting specific practices "
            "and levels (Coming soon)."
        )
        desc_label3.setWordWrap(True)
        desc_label3.setStyleSheet("color: #999; font-size: 10pt;")

        self.button_group.addButton(self.full_radio, 0)
        self.button_group.addButton(self.level1_radio, 1)
        self.button_group.addButton(self.custom_radio, 2)

        layout.addWidget(self.full_radio)
        layout.addWidget(desc_label1)
        layout.addSpacing(10)
        layout.addWidget(self.level1_radio)
        layout.addWidget(desc_label2)
        layout.addSpacing(10)
        layout.addWidget(self.custom_radio)
        layout.addWidget(desc_label3)
        layout.addStretch()


class SummaryPage(QWizardPage):
    """Final page: Summary and confirmation."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Summary")
        self.setSubTitle("Review your assessment configuration.")

        layout = QVBoxLayout(self)

        self.summary_label = QLabel()
        self.summary_label.setWordWrap(True)
        layout.addWidget(self.summary_label)

        layout.addStretch()

    def initializePage(self):
        """Update summary when page is shown."""
        wizard = self.wizard()

        name = wizard.field("name")
        org = wizard.field("organization") or "N/A"
        assessor = wizard.field("assessor") or "N/A"

        # Get questionnaire type
        type_page = wizard.page(1)
        if type_page.full_radio.isChecked():
            q_type = "Full Assessment"
            q_desc = "All 12 practices, 3 maturity levels (108 questions)"
        elif type_page.level1_radio.isChecked():
            q_type = "Level 1 Assessment"
            q_desc = "All 12 practices, Level 1 only (36 questions)"
        else:
            q_type = "Custom Assessment"
            q_desc = "Custom selection"

        summary = f"""
        <h3>Assessment Details:</h3>
        <ul>
        <li><b>Name:</b> {name}</li>
        <li><b>Organization:</b> {org}</li>
        <li><b>Assessor:</b> {assessor}</li>
        </ul>

        <h3>Questionnaire:</h3>
        <ul>
        <li><b>Type:</b> {q_type}</li>
        <li><b>Details:</b> {q_desc}</li>
        </ul>

        <p>Click <b>Finish</b> to create the assessment and open the questionnaire.</p>
        """

        self.summary_label.setText(summary)


class AssessmentWizard(QWizard):
    """
    Wizard for creating new assessments.

    Guides users through:
    1. Basic assessment information
    2. Questionnaire type selection
    3. Summary and confirmation

    Returns the created Assessment and Questionnaire objects.
    """

    def __init__(self, samm_model: OpenSAMMModel, parent=None):
        super().__init__(parent)

        self.samm_model = samm_model
        self.assessment: Assessment = None
        self.questionnaire: Questionnaire = None

        self.setWindowTitle("New Assessment Wizard")
        self.setWizardStyle(QWizard.WizardStyle.ModernStyle)

        # Add pages
        self.addPage(AssessmentInfoPage(self))
        self.addPage(QuestionnaireTypePage(self))
        self.addPage(SummaryPage(self))

        # Connect finished signal
        self.finished.connect(self._on_finished)

    def _on_finished(self, result):
        """Handle wizard completion."""
        if result == QWizard.DialogCode.Accepted:
            # Create assessment
            self.assessment = Assessment(
                name=self.field("name"),
                organization=self.field("organization") or "",
                assessor=self.field("assessor") or "",
                description=self.page(0).desc_edit.toPlainText()
            )

            # Create questionnaire
            type_page = self.page(1)
            if type_page.full_radio.isChecked():
                self.questionnaire = create_full_questionnaire(self.samm_model)
            elif type_page.level1_radio.isChecked():
                self.questionnaire = create_level1_questionnaire(self.samm_model)
            else:
                # Custom - not yet implemented
                self.questionnaire = create_full_questionnaire(self.samm_model)

    def get_assessment(self) -> Assessment:
        """Get the created assessment."""
        return self.assessment

    def get_questionnaire(self) -> Questionnaire:
        """Get the created questionnaire."""
        return self.questionnaire


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    from models.opensamm_model import load_opensamm_model

    app = QApplication(sys.argv)

    # Load model
    samm_model = load_opensamm_model()

    # Show wizard
    wizard = AssessmentWizard(samm_model)
    result = wizard.exec()

    if result == QWizard.DialogCode.Accepted:
        assessment = wizard.get_assessment()
        questionnaire = wizard.get_questionnaire()

        print(f"✓ Created assessment: {assessment}")
        print(f"✓ Questionnaire: {questionnaire}")
        print(f"  Questions: {questionnaire.get_total_questions()}")
    else:
        print("Wizard cancelled")

    sys.exit(0)
