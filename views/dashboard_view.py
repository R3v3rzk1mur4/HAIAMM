"""
Dashboard View

This module provides the dashboard interface for viewing maturity scores
and visualizations using matplotlib.
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTabWidget, QMessageBox, QComboBox, QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from typing import Dict

from models.assessment_model import Assessment
from models.opensamm_model import OpenSAMMModel
from models.haiamm_model import HAIAMMModel
from models.scoring_model import ScoringEngine, PracticeScore

# Import matplotlib for PyQt6
try:
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    FigureCanvas = None
    NavigationToolbar = None

# Import VisualizationService
try:
    from services.visualization_service import VisualizationService
    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False
    VisualizationService = None


class DashboardView(QWidget):
    """
    Widget for displaying maturity dashboards and visualizations.

    Shows interactive matplotlib charts including radar charts, bar charts,
    and heatmaps of HAIAMM maturity scores across multiple domains.
    """

    def __init__(
        self,
        assessment: Assessment,
        samm_model,  # Can be OpenSAMMModel or HAIAMMModel
        parent=None
    ):
        """
        Initialize dashboard view.

        Args:
            assessment: Assessment with responses
            samm_model: OpenSAMM or HAIAMM model instance
            parent: Parent widget
        """
        super().__init__(parent)

        self.assessment = assessment
        self.samm_model = samm_model
        self.is_multi_domain = isinstance(samm_model, HAIAMMModel)
        self.current_domain_id = None  # For domain filtering
        self.practice_scores: Dict[str, PracticeScore] = {}
        self.domain_scores: Dict[str, Dict[str, PracticeScore]] = {}
        self.overall_maturity = 0.0

        # Calculate scores
        self._calculate_scores()

        # Setup UI
        self._setup_ui()

        # Load initial visualization
        self._load_dashboard()

    def _calculate_scores(self):
        """Calculate maturity scores from assessment responses."""
        try:
            engine = ScoringEngine(self.samm_model)

            if self.is_multi_domain:
                # Calculate scores for all domains
                self.domain_scores = engine.calculate_domain_scores(self.assessment)
                # Calculate overall scores across all domains
                self.practice_scores = engine.calculate_all_scores(self.assessment)
            else:
                # OpenSAMM - single domain
                self.practice_scores = engine.calculate_all_scores(self.assessment)

            self.overall_maturity = engine.calculate_overall_maturity(self.practice_scores)
        except Exception as e:
            print(f"Error calculating scores: {e}")
            import traceback
            traceback.print_exc()
            self.practice_scores = {}
            self.domain_scores = {}
            self.overall_maturity = 0.0

    def _setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)

        # Header with metrics
        self.header_widget = self._create_header()
        layout.addWidget(self.header_widget)

        # Domain selector (for HAIAMM multi-domain)
        if self.is_multi_domain:
            domain_selector_widget = self._create_domain_selector()
            layout.addWidget(domain_selector_widget)

        # Tab widget for different visualizations
        self.tab_widget = QTabWidget()

        # Radar chart tab
        self.radar_scroll = QScrollArea()
        self.radar_scroll.setWidgetResizable(True)
        self.tab_widget.addTab(self.radar_scroll, "🎯 Radar Chart")

        # Bar chart tab
        self.bar_scroll = QScrollArea()
        self.bar_scroll.setWidgetResizable(True)
        self.tab_widget.addTab(self.bar_scroll, "📈 Bar Chart")

        # Heatmap tab
        self.heatmap_scroll = QScrollArea()
        self.heatmap_scroll.setWidgetResizable(True)
        self.tab_widget.addTab(self.heatmap_scroll, "🔥 Heatmap")

        layout.addWidget(self.tab_widget)

        # Footer with actions
        footer = self._create_footer()
        layout.addWidget(footer)

    def _create_domain_selector(self) -> QWidget:
        """Create domain selection widget for HAIAMM."""
        widget = QWidget()
        layout = QHBoxLayout(widget)

        label = QLabel("Select Domain:")
        label_font = QFont()
        label_font.setBold(True)
        label.setFont(label_font)
        layout.addWidget(label)

        self.domain_combo = QComboBox()
        self.domain_combo.addItem("All Domains", None)

        if self.is_multi_domain:
            for domain in self.samm_model.domains:
                self.domain_combo.addItem(domain.name, domain.id)

        self.domain_combo.currentIndexChanged.connect(self._on_domain_changed)
        layout.addWidget(self.domain_combo)
        layout.addStretch()

        return widget

    def _on_domain_changed(self, index):
        """Handle domain selection change."""
        self.current_domain_id = self.domain_combo.itemData(index)
        self._load_dashboard()

    def _create_header(self) -> QWidget:
        """Create header with summary metrics."""
        header = QWidget()
        layout = QHBoxLayout(header)

        # Title
        title = QLabel(f"Dashboard: {self.assessment.name}")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(14)
        title.setFont(title_font)
        layout.addWidget(title, 1)

        # Metrics
        metrics_layout = QHBoxLayout()

        # Overall maturity
        maturity_label = QLabel(
            f"<div style='text-align: center;'>"
            f"<div style='font-size: 24px; font-weight: bold; color: #2196F3;'>"
            f"{self.overall_maturity:.2f}</div>"
            f"<div style='font-size: 11px; color: #666;'>Overall Maturity</div>"
            f"</div>"
        )
        metrics_layout.addWidget(maturity_label)

        # Practices with maturity
        practices_scored = len([s for s in self.practice_scores.values() if s.achieved_level > 0])
        total_practices = len(self.practice_scores)
        practices_label = QLabel(
            f"<div style='text-align: center;'>"
            f"<div style='font-size: 24px; font-weight: bold; color: #4CAF50;'>"
            f"{practices_scored}/{total_practices}</div>"
            f"<div style='font-size: 11px; color: #666;'>Practices Scored</div>"
            f"</div>"
        )
        metrics_layout.addWidget(practices_label)

        # Responses
        responses_label = QLabel(
            f"<div style='text-align: center;'>"
            f"<div style='font-size: 24px; font-weight: bold; color: #FF9800;'>"
            f"{self.assessment.get_response_count()}</div>"
            f"<div style='font-size: 11px; color: #666;'>Total Responses</div>"
            f"</div>"
        )
        metrics_layout.addWidget(responses_label)

        layout.addLayout(metrics_layout)

        return header

    def _create_footer(self) -> QWidget:
        """Create footer with action buttons."""
        footer = QWidget()
        layout = QHBoxLayout(footer)

        # Refresh button
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.clicked.connect(self.refresh)
        layout.addWidget(refresh_btn)

        layout.addStretch()

        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        return footer

    def _load_dashboard(self):
        """Load all visualizations."""
        if not MATPLOTLIB_AVAILABLE or not VISUALIZATION_AVAILABLE:
            error_widget = QLabel(
                "Matplotlib is required for visualizations.\n"
                "Install with: pip install matplotlib numpy"
            )
            error_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.radar_scroll.setWidget(error_widget)
            self.bar_scroll.setWidget(error_widget)
            self.heatmap_scroll.setWidget(error_widget)
            return

        try:
            viz = VisualizationService(self.samm_model)

            # Get scores for current domain or all domains
            if self.current_domain_id and self.is_multi_domain:
                display_scores = self.domain_scores.get(self.current_domain_id, {})
            else:
                display_scores = self.practice_scores

            # Load radar chart
            radar_fig = viz.create_maturity_radar_chart(display_scores, domain_id=self.current_domain_id)
            radar_widget = self._create_chart_widget(radar_fig)
            self.radar_scroll.setWidget(radar_widget)

            # Load bar chart
            bar_fig = viz.create_function_bar_chart(display_scores, domain_id=self.current_domain_id)
            bar_widget = self._create_chart_widget(bar_fig)
            self.bar_scroll.setWidget(bar_widget)

            # Load heatmap - use domain_scores for multi-domain view
            if self.is_multi_domain and not self.current_domain_id:
                heatmap_fig = viz.create_maturity_heatmap(display_scores, domain_scores=self.domain_scores)
            else:
                heatmap_fig = viz.create_maturity_heatmap(display_scores)
            heatmap_widget = self._create_chart_widget(heatmap_fig)
            self.heatmap_scroll.setWidget(heatmap_widget)

        except Exception as e:
            error_msg = f"Error loading visualizations: {e}"
            print(error_msg)
            import traceback
            traceback.print_exc()

            # Show error message
            error_widget = QLabel(
                f"Error loading dashboard:\n{error_msg}\n\n"
                "Make sure matplotlib is installed:\n"
                "pip install matplotlib numpy"
            )
            error_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            error_widget.setWordWrap(True)
            self.radar_scroll.setWidget(error_widget)
            self.bar_scroll.setWidget(error_widget)
            self.heatmap_scroll.setWidget(error_widget)

    def _create_chart_widget(self, fig) -> QWidget:
        """Create a widget containing a matplotlib figure with navigation toolbar."""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Create canvas for the figure
        canvas = FigureCanvas(fig)
        canvas.setMinimumSize(800, 600)

        # Create navigation toolbar
        toolbar = NavigationToolbar(canvas, widget)

        # Add toolbar and canvas to layout
        layout.addWidget(toolbar)
        layout.addWidget(canvas)

        return widget

    def refresh(self):
        """Refresh dashboard with latest data."""
        self._calculate_scores()
        self._load_dashboard()

        # Update header metrics
        if hasattr(self, 'header_widget') and self.header_widget:
            self.header_widget.deleteLater()
        self.header_widget = self._create_header()
        self.layout().insertWidget(0, self.header_widget)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    from models.haiamm_model import load_haiamm_model
    from models.assessment_model import AssessmentResponse, ResponseType

    app = QApplication(sys.argv)

    # Load model
    samm_model = load_haiamm_model()

    # Create test assessment
    assessment = Assessment(
        name="Test Dashboard",
        organization="Test Org"
    )

    # Add some test responses
    test_responses = [
        ("sm", "software", 1, "sm_software_l1_q1", ResponseType.YES),
        ("sm", "software", 1, "sm_software_l1_q2", ResponseType.YES),
        ("sm", "software", 1, "sm_software_l1_q3", ResponseType.YES),
        ("pc", "software", 1, "pc_software_l1_q1", ResponseType.YES),
        ("pc", "software", 1, "pc_software_l1_q2", ResponseType.PARTIAL),
        ("eg", "software", 1, "eg_software_l1_q1", ResponseType.YES),
        ("eg", "software", 1, "eg_software_l1_q2", ResponseType.YES),
        ("eg", "software", 1, "eg_software_l1_q3", ResponseType.YES),
        ("eg", "software", 2, "eg_software_l2_q1", ResponseType.YES),
    ]

    for practice_id, domain_id, level, qid, response_type in test_responses:
        assessment.add_response(AssessmentResponse(
            practice_id=practice_id,
            domain_id=domain_id,
            level=level,
            question_id=qid,
            response=response_type
        ))

    # Create and show dashboard
    dashboard = DashboardView(assessment, samm_model)
    dashboard.setWindowTitle("HAIAMM - Dashboard")
    dashboard.resize(1200, 800)
    dashboard.show()

    sys.exit(app.exec())
