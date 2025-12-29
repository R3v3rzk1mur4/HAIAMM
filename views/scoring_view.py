"""
Scoring View

This module provides a detailed view of maturity scores with breakdowns
by practice and level.
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QHeaderView, QTabWidget,
    QTextEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
from typing import Dict

from models.assessment_model import Assessment
from models.opensamm_model import OpenSAMMModel
from models.haiamm_model import HAIAMMModel
from models.scoring_model import ScoringEngine, PracticeScore


class ScoringView(QWidget):
    """
    Widget for displaying detailed maturity scoring information.

    Shows tabular breakdowns of scores by practice, level, business function, and domain (for HAIAMM).
    """

    def __init__(
        self,
        assessment: Assessment,
        samm_model,  # Can be OpenSAMMModel or HAIAMMModel
        parent=None
    ):
        """
        Initialize scoring view.

        Args:
            assessment: Assessment with responses
            samm_model: OpenSAMM or HAIAMM model instance
            parent: Parent widget
        """
        super().__init__(parent)

        self.assessment = assessment
        self.samm_model = samm_model
        self.is_multi_domain = isinstance(samm_model, HAIAMMModel)
        self.practice_scores: Dict[str, PracticeScore] = {}
        self.domain_scores: Dict[str, Dict[str, PracticeScore]] = {}

        # Calculate scores
        self._calculate_scores()

        # Setup UI
        self._setup_ui()

    def _calculate_scores(self):
        """Calculate maturity scores."""
        engine = ScoringEngine(self.samm_model)

        if self.is_multi_domain:
            # Calculate scores for all domains
            self.domain_scores = engine.calculate_domain_scores(self.assessment)
            # Calculate overall scores across all domains
            self.practice_scores = engine.calculate_all_scores(self.assessment)
        else:
            # OpenSAMM - single domain
            self.practice_scores = engine.calculate_all_scores(self.assessment)

        self.summary = engine.get_summary(self.assessment, self.practice_scores)

    def _setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)

        # Header
        header = self._create_header()
        layout.addWidget(header)

        # Tab widget for different views
        tab_widget = QTabWidget()

        # Practice scores table
        practice_table = self._create_practice_table()
        tab_widget.addTab(practice_table, "📋 Practice Scores")

        # Function summary table
        function_table = self._create_function_table()
        tab_widget.addTab(function_table, "🏢 Business Functions")

        # Detailed breakdown
        detail_view = self._create_detail_view()
        tab_widget.addTab(detail_view, "🔍 Detailed Breakdown")

        layout.addWidget(tab_widget)

        # Footer
        footer = self._create_footer()
        layout.addWidget(footer)

    def _create_header(self) -> QWidget:
        """Create header with summary."""
        header = QWidget()
        layout = QVBoxLayout(header)

        title = QLabel(f"Scoring Report: {self.assessment.name}")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(14)
        title.setFont(title_font)
        layout.addWidget(title)

        summary_text = (
            f"Overall Maturity: <b>{self.summary['overall_maturity']:.2f}</b> | "
            f"Practices Scored: <b>{self.summary['practices_scored']}/{self.summary['practice_count']}</b> | "
            f"Total Responses: <b>{self.summary['total_responses']}</b>"
        )
        summary_label = QLabel(summary_text)
        layout.addWidget(summary_label)

        return header

    def _create_practice_table(self) -> QTableWidget:
        """Create table showing all practice scores."""
        table = QTableWidget()
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "Practice",
            "Achieved Level",
            "Overall Score",
            "Level 1",
            "Level 2",
            "Level 3",
            "Business Function"
        ])

        # Set row count
        table.setRowCount(len(self.practice_scores))

        # Populate table
        row = 0
        for practice in self.samm_model.get_all_practices():
            score = self.practice_scores.get(
                practice.id,
                PracticeScore(practice.id, practice.name)
            )

            # Find business function
            function_name = ""
            for func in self.samm_model.business_functions:
                if any(p.id == practice.id for p in func.practices):
                    function_name = func.name
                    break

            # Practice name
            item = QTableWidgetItem(practice.name)
            item.setFont(QFont("Arial", weight=QFont.Weight.Bold))
            table.setItem(row, 0, item)

            # Achieved level
            level_item = QTableWidgetItem(str(score.achieved_level))
            level_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            # Color code by level
            if score.achieved_level == 3:
                level_item.setBackground(QColor("#4CAF50"))
            elif score.achieved_level == 2:
                level_item.setBackground(QColor("#FF9800"))
            elif score.achieved_level == 1:
                level_item.setBackground(QColor("#FFEB3B"))
            table.setItem(row, 1, level_item)

            # Overall score
            overall_item = QTableWidgetItem(f"{score.overall_score:.1f}%")
            overall_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            table.setItem(row, 2, overall_item)

            # Individual level scores
            for level in [1, 2, 3]:
                level_score = score.level_scores.get(level)
                if level_score:
                    score_text = f"{level_score.score:.1f}%"
                    if level_score.is_achieved:
                        score_text += " ✓"
                else:
                    score_text = "-"

                level_item = QTableWidgetItem(score_text)
                level_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                table.setItem(row, 3 + (level - 1), level_item)

            # Business function
            table.setItem(row, 6, QTableWidgetItem(function_name))

            row += 1

        # Resize columns
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        for i in range(1, 7):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)

        table.setAlternatingRowColors(True)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        return table

    def _create_function_table(self) -> QTableWidget:
        """Create table showing business function summaries."""
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels([
            "Business Function",
            "Average Maturity",
            "Practices"
        ])

        table.setRowCount(len(self.samm_model.business_functions))

        row = 0
        for function in self.samm_model.business_functions:
            # Function name
            table.setItem(row, 0, QTableWidgetItem(function.name))

            # Calculate average
            function_data = self.summary['function_averages'].get(function.id, {})
            avg = function_data.get('average_level', 0.0)

            avg_item = QTableWidgetItem(f"{avg:.2f}")
            avg_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            table.setItem(row, 1, avg_item)

            # Practices summary
            practices_text = ", ".join([
                f"{p['id'].upper()}: L{p['achieved_level']}"
                for p in function_data.get('practices', [])
            ])
            table.setItem(row, 2, QTableWidgetItem(practices_text))

            row += 1

        # Resize columns
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        table.setAlternatingRowColors(True)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        return table

    def _create_detail_view(self) -> QTextEdit:
        """Create detailed text view of all scores."""
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)

        # Build detailed report
        lines = []
        lines.append(f"=== Detailed Scoring Report ===\n")
        lines.append(f"Assessment: {self.assessment.name}")
        lines.append(f"Organization: {self.assessment.organization}")
        lines.append(f"Overall Maturity: {self.summary['overall_maturity']:.2f}\n")

        lines.append(f"\n=== Level Distribution ===")
        dist = self.summary['level_distribution']
        lines.append(f"Level 0: {dist[0]} practices")
        lines.append(f"Level 1: {dist[1]} practices")
        lines.append(f"Level 2: {dist[2]} practices")
        lines.append(f"Level 3: {dist[3]} practices")

        for function in self.samm_model.business_functions:
            lines.append(f"\n=== {function.name} ===")
            function_data = self.summary['function_averages'].get(function.id, {})
            lines.append(f"Average: {function_data.get('average_level', 0):.2f}")

            for practice in function.practices:
                score = self.practice_scores.get(
                    practice.id,
                    PracticeScore(practice.id, practice.name)
                )

                lines.append(f"\n{practice.name} ({practice.short_name}):")
                lines.append(f"  Achieved Level: {score.achieved_level}")
                lines.append(f"  Overall Score: {score.overall_score:.1f}%")

                for level, level_score in sorted(score.level_scores.items()):
                    status = "✓ Achieved" if level_score.is_achieved else "✗ Not Achieved"
                    lines.append(
                        f"  Level {level}: {level_score.score:.1f}% - "
                        f"Yes:{level_score.yes_count} Partial:{level_score.partial_count} "
                        f"No:{level_score.no_count} NA:{level_score.na_count} - {status}"
                    )

        text_edit.setPlainText("\n".join(lines))

        return text_edit

    def _create_footer(self) -> QWidget:
        """Create footer with buttons."""
        footer = QWidget()
        layout = QHBoxLayout(footer)

        # Export button (for future)
        export_btn = QPushButton("📄 Export Report")
        export_btn.setEnabled(False)  # Not implemented yet
        layout.addWidget(export_btn)

        layout.addStretch()

        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        return footer


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    from models.opensamm_model import load_opensamm_model
    from models.assessment_model import AssessmentResponse, ResponseType

    app = QApplication(sys.argv)

    # Load model
    samm_model = load_opensamm_model()

    # Create test assessment
    assessment = Assessment(
        name="Test Scoring View",
        organization="Test Org"
    )

    # Add test responses
    test_responses = [
        ("sm", 1, "sm_l1_q1", ResponseType.YES),
        ("sm", 1, "sm_l1_q2", ResponseType.YES),
        ("sm", 1, "sm_l1_q3", ResponseType.YES),
        ("sm", 2, "sm_l2_q1", ResponseType.PARTIAL),
        ("pc", 1, "pc_l1_q1", ResponseType.YES),
        ("eg", 1, "eg_l1_q1", ResponseType.YES),
        ("eg", 1, "eg_l1_q2", ResponseType.YES),
        ("eg", 1, "eg_l1_q3", ResponseType.YES),
        ("eg", 2, "eg_l2_q1", ResponseType.YES),
        ("eg", 2, "eg_l2_q2", ResponseType.YES),
        ("eg", 2, "eg_l2_q3", ResponseType.YES),
    ]

    for practice_id, level, qid, response_type in test_responses:
        assessment.add_response(AssessmentResponse(
            practice_id=practice_id,
            level=level,
            question_id=qid,
            response=response_type
        ))

    # Create and show scoring view
    scoring_view = ScoringView(assessment, samm_model)
    scoring_view.setWindowTitle("HAIAMM - Scoring Report")
    scoring_view.resize(1000, 600)
    scoring_view.show()

    sys.exit(app.exec())
