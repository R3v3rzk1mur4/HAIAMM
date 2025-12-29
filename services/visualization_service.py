"""
Visualization Service

This module generates matplotlib charts for HAIAMM multi-domain maturity data.
Charts are returned as matplotlib figures that can be displayed in PyQt6 widgets.
Supports both OpenSAMM (single domain) and HAIAMM (multi-domain) visualizations.
"""

from typing import Dict, List, Optional, Union
import io
import base64
from models.scoring_model import PracticeScore
from models.opensamm_model import OpenSAMMModel

# Import HAIAMMModel for multi-domain support
try:
    from models.haiamm_model import HAIAMMModel
    HAIAMM_AVAILABLE = True
except ImportError:
    HAIAMM_AVAILABLE = False
    HAIAMMModel = None

# Matplotlib imports
try:
    import matplotlib
    matplotlib.use('Qt5Agg')  # Use Qt backend for PyQt6 integration
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
    import numpy as np
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    plt = None
    Figure = None
    FigureCanvasQTAgg = None
    np = None


class VisualizationService:
    """
    Generate matplotlib visualizations for HAIAMM multi-domain assessments.

    Creates interactive charts including:
    - Radar charts (spider charts) for all practices (12 for OpenSAMM, 78 for HAIAMM)
    - Bar charts grouped by business function
    - Heatmaps showing maturity grid (domains × practices for HAIAMM)
    - Progress/comparison charts
    """

    def __init__(self, samm_model: Union[OpenSAMMModel, 'HAIAMMModel']):
        """
        Initialize visualization service.

        Args:
            samm_model: OpenSAMM or HAIAMM model instance

        Raises:
            ImportError: If matplotlib is not installed
        """
        if not MATPLOTLIB_AVAILABLE:
            raise ImportError(
                "Matplotlib is required for visualization features. "
                "Install with: pip install matplotlib numpy"
            )

        self.samm_model = samm_model
        self.is_multi_domain = HAIAMM_AVAILABLE and isinstance(samm_model, HAIAMMModel)

        # Color schemes
        self.level_colors = {
            0: '#e0e0e0',  # Gray - no maturity
            1: '#ffeb3b',  # Yellow - initial
            2: '#ff9800',  # Orange - intermediate
            3: '#4caf50'   # Green - advanced
        }

        self.function_colors = {
            'governance': '#2196F3',     # Blue
            'engineering': '#4CAF50',    # Green (updated from construction)
            'verification': '#FF9800',   # Orange
            'operations': '#9C27B0'      # Purple (updated from deployment)
        }

        # Set matplotlib style
        plt.style.use('seaborn-v0_8-darkgrid')

    def create_maturity_radar_chart(
        self,
        practice_scores: Dict[str, PracticeScore],
        title: str = None,
        domain_id: Optional[str] = None
    ) -> Figure:
        """
        Create radar/spider chart showing maturity across practices.

        Args:
            practice_scores: Dictionary of practice scores
            title: Chart title (auto-generated if None)
            domain_id: Optional domain ID for multi-domain models

        Returns:
            Matplotlib Figure object
        """
        if title is None:
            if self.is_multi_domain and domain_id:
                domain = self.samm_model.get_domain(domain_id)
                title = f"HAIAMM Maturity Radar - {domain.name if domain else domain_id}"
            elif self.is_multi_domain:
                title = "HAIAMM Maturity Radar - All Domains"
            else:
                title = "OpenSAMM Maturity Radar"

        # Prepare data
        practices = []
        achieved_levels = []
        practice_names = []

        if self.is_multi_domain and domain_id:
            # Get practices for specific domain
            all_practices = self.samm_model.get_all_practices_for_domain(domain_id)
        elif self.is_multi_domain:
            # Get all practices across all domains
            all_practices = []
            for domain in self.samm_model.domains:
                all_practices.extend(domain.get_all_practices())
        else:
            # OpenSAMM - get all practices
            all_practices = self.samm_model.get_all_practices()

        for practice in all_practices:
            score = practice_scores.get(practice.id, PracticeScore(practice.id, practice.name))
            practices.append(practice.short_name)
            practice_names.append(practice.name)
            achieved_levels.append(score.achieved_level)

        if not practices:
            # Return empty figure
            fig = Figure(figsize=(8, 6))
            ax = fig.add_subplot(111)
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', fontsize=14)
            ax.set_title(title)
            ax.axis('off')
            return fig

        # Number of variables
        num_vars = len(practices)

        # Compute angle for each axis
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

        # Complete the circle
        achieved_levels += achieved_levels[:1]
        angles += angles[:1]

        # Create figure
        fig = Figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='polar')

        # Plot data
        ax.plot(angles, achieved_levels, 'o-', linewidth=2, color='#2196F3', label='Achieved Level')
        ax.fill(angles, achieved_levels, alpha=0.25, color='#2196F3')

        # Set labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(practices, size=8)
        ax.set_ylim(0, 3)
        ax.set_yticks([0, 1, 2, 3])
        ax.set_yticklabels(['0', '1', '2', '3'])
        ax.set_title(title, size=14, weight='bold', pad=20)
        ax.grid(True)

        return fig

    def create_function_bar_chart(
        self,
        practice_scores: Dict[str, PracticeScore],
        title: str = "Maturity by Business Function",
        domain_id: Optional[str] = None
    ) -> Figure:
        """
        Create grouped bar chart showing business functions with practices.

        Args:
            practice_scores: Dictionary of practice scores
            title: Chart title
            domain_id: Optional domain ID for multi-domain models

        Returns:
            Matplotlib Figure object
        """
        # Get business functions
        if self.is_multi_domain and domain_id:
            domain = self.samm_model.get_domain(domain_id)
            business_functions = domain.business_functions if domain else []
        elif self.is_multi_domain:
            # Use first domain or all domains
            business_functions = self.samm_model.domains[0].business_functions if self.samm_model.domains else []
        else:
            business_functions = self.samm_model.business_functions

        if not business_functions:
            # Return empty figure
            fig = Figure(figsize=(10, 6))
            ax = fig.add_subplot(111)
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', fontsize=14)
            ax.set_title(title)
            ax.axis('off')
            return fig

        # Create figure
        fig = Figure(figsize=(12, 6))
        ax = fig.add_subplot(111)

        # Prepare data
        x_pos = 0
        x_ticks = []
        x_labels = []

        for function in business_functions:
            practice_names = []
            levels = []

            for practice in function.practices:
                score = practice_scores.get(practice.id, PracticeScore(practice.id, practice.name))
                practice_names.append(practice.short_name)
                levels.append(score.achieved_level)

            # Plot bars for this function
            num_practices = len(practice_names)
            positions = np.arange(x_pos, x_pos + num_practices)

            color = self.function_colors.get(function.id, '#757575')
            ax.bar(positions, levels, width=0.8, label=function.name, color=color, alpha=0.8)

            # Add practice labels
            for i, pos in enumerate(positions):
                x_ticks.append(pos)
                x_labels.append(practice_names[i])

            x_pos += num_practices + 1  # Add spacing between functions

        # Configure axes
        ax.set_xticks(x_ticks)
        ax.set_xticklabels(x_labels, rotation=45, ha='right', size=8)
        ax.set_ylim(0, 3)
        ax.set_yticks([0, 1, 2, 3])
        ax.set_ylabel('Maturity Level', fontsize=11)
        ax.set_xlabel('Security Practice', fontsize=11)
        ax.set_title(title, fontsize=14, weight='bold')
        ax.legend(loc='upper right', fontsize=9)
        ax.grid(axis='y', alpha=0.3)

        fig.tight_layout()
        return fig

    def create_maturity_heatmap(
        self,
        practice_scores: Dict[str, PracticeScore],
        title: str = None,
        domain_scores: Optional[Dict[str, Dict[str, PracticeScore]]] = None
    ) -> Figure:
        """
        Create heatmap showing maturity levels.
        - For OpenSAMM: 4 functions × 3 practices grid
        - For HAIAMM: 6 domains × 13 practices grid

        Args:
            practice_scores: Dictionary of practice scores (for single domain/OpenSAMM)
            title: Chart title (auto-generated if None)
            domain_scores: Dictionary mapping domain_id to practice scores (for HAIAMM multi-domain)

        Returns:
            Matplotlib Figure object
        """
        if title is None:
            title = "HAIAMM Maturity Heatmap" if self.is_multi_domain else "Maturity Heatmap"

        # Prepare data
        z_data = []  # Matrix of maturity levels
        y_labels = []  # Row labels (functions or domains)
        x_labels = []  # Column labels (practices)

        if self.is_multi_domain and domain_scores:
            # HAIAMM multi-domain: Show domains as rows
            for domain in self.samm_model.domains:
                row_data = []
                scores = domain_scores.get(domain.id, {})

                practices = domain.get_all_practices()
                for practice in practices:
                    score = scores.get(practice.id, PracticeScore(practice.id, practice.name))
                    row_data.append(score.achieved_level)

                    # Collect x labels only once (from first domain)
                    if len(y_labels) == 0:
                        x_labels.append(practice.short_name)

                z_data.append(row_data)
                y_labels.append(domain.name)

        else:
            # OpenSAMM or single domain: Show business functions as rows
            if self.is_multi_domain:
                # For HAIAMM single domain view, use first domain or default
                business_functions = self.samm_model.domains[0].business_functions if self.samm_model.domains else []
            else:
                business_functions = self.samm_model.business_functions

            for function in business_functions:
                row_data = []

                # Get practices for this function
                for i, practice in enumerate(function.practices):
                    score = practice_scores.get(practice.id, PracticeScore(practice.id, practice.name))
                    row_data.append(score.achieved_level)

                    # Collect x labels only once (from first function)
                    if len(y_labels) == 0:
                        x_labels.append(practice.short_name)

                z_data.append(row_data)
                y_labels.append(function.name)

        if not z_data:
            # Return empty figure
            fig = Figure(figsize=(10, 6))
            ax = fig.add_subplot(111)
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', fontsize=14)
            ax.set_title(title)
            ax.axis('off')
            return fig

        # Create heatmap
        z_array = np.array(z_data)

        fig = Figure(figsize=(14, 8) if self.is_multi_domain else (12, 6))
        ax = fig.add_subplot(111)

        # Create custom colormap
        from matplotlib.colors import ListedColormap
        colors = [self.level_colors[i] for i in range(4)]
        cmap = ListedColormap(colors)

        im = ax.imshow(z_array, cmap=cmap, vmin=0, vmax=3, aspect='auto')

        # Set ticks and labels
        ax.set_xticks(np.arange(len(x_labels)))
        ax.set_yticks(np.arange(len(y_labels)))
        ax.set_xticklabels(x_labels, rotation=45, ha='right', size=8)
        ax.set_yticklabels(y_labels, size=9)

        # Add colorbar
        cbar = fig.colorbar(im, ax=ax, ticks=[0, 1, 2, 3])
        cbar.set_label('Maturity Level', rotation=270, labelpad=15)

        # Add text annotations
        for i in range(len(y_labels)):
            for j in range(len(x_labels)):
                if j < len(z_data[i]):
                    text = ax.text(j, i, int(z_data[i][j]),
                                 ha="center", va="center", color="black", fontsize=9)

        ylabel = "Domain" if (self.is_multi_domain and domain_scores) else "Business Function"
        ax.set_xlabel('Security Practice', fontsize=11)
        ax.set_ylabel(ylabel, fontsize=11)
        ax.set_title(title, fontsize=14, weight='bold')

        fig.tight_layout()
        return fig

    def create_progress_comparison_chart(
        self,
        historical_scores: List[Dict],
        title: str = "Maturity Progress Over Time"
    ) -> Figure:
        """
        Create line chart comparing maturity over time.

        Args:
            historical_scores: List of score dictionaries with dates
            title: Chart title

        Returns:
            Matplotlib Figure object
        """
        if not historical_scores:
            # Return empty chart
            fig = Figure(figsize=(10, 6))
            ax = fig.add_subplot(111)
            ax.text(0.5, 0.5, "No historical data available yet",
                   ha='center', va='center', fontsize=14, color='gray')
            ax.set_title(title)
            ax.axis('off')
            return fig

        # Prepare data for each practice
        fig = Figure(figsize=(12, 6))
        ax = fig.add_subplot(111)

        practices = self.samm_model.get_all_practices()

        for practice in practices:
            dates = []
            levels = []

            for snapshot in historical_scores:
                dates.append(snapshot.get('date', ''))
                practice_score = snapshot.get('scores', {}).get(practice.id, {})
                levels.append(practice_score.get('achieved_level', 0))

            ax.plot(dates, levels, marker='o', label=practice.short_name, linewidth=2)

        ax.set_ylim(0, 3)
        ax.set_yticks([0, 1, 2, 3])
        ax.set_xlabel('Date', fontsize=11)
        ax.set_ylabel('Maturity Level', fontsize=11)
        ax.set_title(title, fontsize=14, weight='bold')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
        ax.grid(axis='both', alpha=0.3)

        fig.tight_layout()
        return fig


if __name__ == "__main__":
    # Test the visualization service
    from models.haiamm_model import load_haiamm_model
    from models.assessment_model import Assessment, AssessmentResponse, ResponseType
    from models.scoring_model import ScoringEngine

    print("Testing Visualization Service with matplotlib...")

    # Load model
    samm_model = load_haiamm_model()
    print("✓ Loaded HAIAMM model\n")

    # Create test assessment with varied scores
    assessment = Assessment(name="Test Dashboard", organization="Test Org")

    # Add responses to create some maturity scores
    test_data = [
        ("sm", "software", 1, ["sm_software_l1_q1", "sm_software_l1_q2", "sm_software_l1_q3"], ResponseType.YES),
        ("sm", "software", 2, ["sm_software_l2_q1", "sm_software_l2_q2"], ResponseType.PARTIAL),
        ("pc", "software", 1, ["pc_software_l1_q1", "pc_software_l1_q2"], ResponseType.YES),
    ]

    for practice_id, domain_id, level, qids, response_type in test_data:
        for qid in qids:
            assessment.add_response(AssessmentResponse(
                practice_id=practice_id,
                domain_id=domain_id,
                level=level,
                question_id=qid,
                response=response_type
            ))

    # Calculate scores
    engine = ScoringEngine(samm_model)
    scores = engine.calculate_all_scores(assessment)
    overall = engine.calculate_overall_maturity(scores)

    print(f"Created test data: {assessment.get_response_count()} responses")
    print(f"Overall maturity: {overall:.2f}\n")

    # Test visualizations
    viz = VisualizationService(samm_model)

    print("[1] Testing Radar Chart...")
    radar_fig = viz.create_maturity_radar_chart(scores)
    print(f"✓ Generated radar chart")

    print("\n[2] Testing Bar Chart...")
    bar_fig = viz.create_function_bar_chart(scores)
    print(f"✓ Generated bar chart")

    print("\n[3] Testing Heatmap...")
    heatmap_fig = viz.create_maturity_heatmap(scores)
    print(f"✓ Generated heatmap")

    print("\n✓ All visualization tests passed!")
    print("Note: Figures are matplotlib Figure objects, not HTML")
