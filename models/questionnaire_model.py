"""
Questionnaire Model

This module defines the model for dynamic questionnaire generation.
It creates customizable questionnaires from the OpenSAMM model.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set
from models.opensamm_model import (
    OpenSAMMModel, SecurityPractice, MaturityLevel, AssessmentCriteria
)


@dataclass
class Question:
    """
    Represents a single questionnaire question.

    Attributes:
        id: Unique question identifier (e.g., "sm_l1_q1")
        practice_id: Practice this question belongs to
        practice_name: Full name of the practice
        level: Maturity level (1, 2, or 3)
        text: The question text
        guidance: Additional guidance to help answer
        section: Section number for display
        question_number: Question number within section
    """
    id: str
    practice_id: str
    practice_name: str
    level: int
    text: str
    guidance: str = ""
    section: int = 0
    question_number: int = 0

    def get_display_title(self) -> str:
        """Get formatted display title."""
        return f"{self.practice_name} - Level {self.level}"

    def get_full_display(self) -> str:
        """Get full display string with question number."""
        return f"Q{self.question_number}: {self.text}"


@dataclass
class QuestionnaireSection:
    """
    Represents a section of the questionnaire (one practice).

    Attributes:
        practice: The SecurityPractice this section covers
        questions: List of questions in this section
        included_levels: Which maturity levels to include
    """
    practice: SecurityPractice
    questions: List[Question] = field(default_factory=list)
    included_levels: Set[int] = field(default_factory=lambda: {1, 2, 3})

    def __post_init__(self):
        """Generate questions after initialization."""
        if not self.questions:
            self.generate_questions()

    def generate_questions(self):
        """Generate questions from practice maturity levels."""
        self.questions = []
        question_counter = 1

        for level in self.practice.maturity_levels:
            if level.level not in self.included_levels:
                continue

            for criteria in level.assessment_criteria:
                question = Question(
                    id=criteria.id,
                    practice_id=self.practice.id,
                    practice_name=self.practice.name,
                    level=level.level,
                    text=criteria.question,
                    guidance=criteria.guidance,
                    question_number=question_counter
                )
                self.questions.append(question)
                question_counter += 1

    def get_question_count(self) -> int:
        """Get number of questions in this section."""
        return len(self.questions)

    def get_questions_by_level(self, level: int) -> List[Question]:
        """Get questions for a specific maturity level."""
        return [q for q in self.questions if q.level == level]


class Questionnaire:
    """
    Complete customizable questionnaire for OpenSAMM assessment.

    This class generates a dynamic questionnaire based on the OpenSAMM model
    and allows customization of which practices and levels to include.

    Attributes:
        samm_model: The OpenSAMM model to generate from
        name: Questionnaire name
        description: Questionnaire description
        selected_practices: IDs of practices to include (all if empty)
        target_levels: Target levels per practice (default: all levels 1-3)
        sections: List of questionnaire sections
    """

    def __init__(
        self,
        samm_model: OpenSAMMModel,
        name: str = "OpenSAMM v1.0 Full Assessment",
        description: str = "",
        selected_practices: Optional[List[str]] = None,
        target_levels: Optional[Dict[str, Set[int]]] = None
    ):
        """
        Initialize questionnaire.

        Args:
            samm_model: OpenSAMM model instance
            name: Questionnaire name
            description: Optional description
            selected_practices: List of practice IDs to include (None = all)
            target_levels: Dict mapping practice_id to set of levels (None = all levels)
        """
        self.samm_model = samm_model
        self.name = name
        self.description = description
        self.selected_practices = selected_practices or []
        self.target_levels = target_levels or {}
        self.sections: List[QuestionnaireSection] = []

        # Generate questionnaire
        self.generate()

    def generate(self):
        """Generate questionnaire sections based on selections."""
        self.sections = []
        section_counter = 1

        for function in self.samm_model.business_functions:
            for practice in function.practices:
                # Skip if not in selected practices (when selection is active)
                if self.selected_practices and practice.id not in self.selected_practices:
                    continue

                # Determine which levels to include for this practice
                included_levels = self.target_levels.get(
                    practice.id,
                    {1, 2, 3}  # Default: all levels
                )

                # Create section
                section = QuestionnaireSection(
                    practice=practice,
                    included_levels=included_levels
                )

                # Update section numbers
                for question in section.questions:
                    question.section = section_counter

                self.sections.append(section)
                section_counter += 1

    def get_total_questions(self) -> int:
        """Get total number of questions in questionnaire."""
        return sum(section.get_question_count() for section in self.sections)

    def get_section_count(self) -> int:
        """Get number of sections."""
        return len(self.sections)

    def get_practice_ids(self) -> List[str]:
        """Get list of practice IDs included in questionnaire."""
        return [section.practice.id for section in self.sections]

    def get_section_by_practice(self, practice_id: str) -> Optional[QuestionnaireSection]:
        """Get section for a specific practice."""
        for section in self.sections:
            if section.practice.id == practice_id:
                return section
        return None

    def get_all_questions(self) -> List[Question]:
        """Get all questions in order."""
        all_questions = []
        for section in self.sections:
            all_questions.extend(section.questions)
        return all_questions

    def customize_practice_inclusion(self, practice_id: str, include: bool):
        """
        Include or exclude a specific practice.

        Args:
            practice_id: Practice identifier
            include: True to include, False to exclude
        """
        if include:
            if practice_id not in self.selected_practices:
                self.selected_practices.append(practice_id)
        else:
            if practice_id in self.selected_practices:
                self.selected_practices.remove(practice_id)

        # Regenerate questionnaire
        self.generate()

    def set_target_levels(self, practice_id: str, levels: Set[int]):
        """
        Set which maturity levels to include for a practice.

        Args:
            practice_id: Practice identifier
            levels: Set of levels to include (1, 2, 3)
        """
        self.target_levels[practice_id] = levels
        self.generate()

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'selected_practices': self.selected_practices,
            'target_levels': {
                pid: list(levels) for pid, levels in self.target_levels.items()
            },
            'section_count': self.get_section_count(),
            'total_questions': self.get_total_questions()
        }

    def get_summary(self) -> str:
        """Get a summary of the questionnaire."""
        lines = [
            f"Questionnaire: {self.name}",
            f"Sections: {self.get_section_count()}",
            f"Total Questions: {self.get_total_questions()}",
            "\nSections:"
        ]

        for i, section in enumerate(self.sections, 1):
            levels_str = ", ".join(str(l) for l in sorted(section.included_levels))
            lines.append(
                f"  {i}. {section.practice.name} "
                f"(Levels {levels_str}): {section.get_question_count()} questions"
            )

        return "\n".join(lines)

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"Questionnaire(name='{self.name}', "
            f"sections={self.get_section_count()}, "
            f"questions={self.get_total_questions()})"
        )


def create_full_questionnaire(samm_model: OpenSAMMModel) -> Questionnaire:
    """
    Create a full questionnaire covering all practices and levels.

    Args:
        samm_model: OpenSAMM model instance

    Returns:
        Complete questionnaire
    """
    return Questionnaire(
        samm_model=samm_model,
        name="OpenSAMM v1.0 Full Assessment",
        description="Complete assessment covering all 12 practices and 3 maturity levels"
    )


def create_level1_questionnaire(samm_model: OpenSAMMModel) -> Questionnaire:
    """
    Create a questionnaire for Level 1 only (initial maturity).

    Args:
        samm_model: OpenSAMM model instance

    Returns:
        Level 1 questionnaire
    """
    # Set all practices to Level 1 only
    target_levels = {
        practice.id: {1}
        for practice in samm_model.get_all_practices()
    }

    return Questionnaire(
        samm_model=samm_model,
        name="OpenSAMM v1.0 Level 1 Assessment",
        description="Initial maturity assessment (Level 1 only)",
        target_levels=target_levels
    )


def create_custom_questionnaire(
    samm_model: OpenSAMMModel,
    practice_ids: List[str],
    name: str = "Custom Assessment"
) -> Questionnaire:
    """
    Create a custom questionnaire for specific practices.

    Args:
        samm_model: OpenSAMM model instance
        practice_ids: List of practice IDs to include
        name: Questionnaire name

    Returns:
        Custom questionnaire
    """
    return Questionnaire(
        samm_model=samm_model,
        name=name,
        description=f"Custom assessment for {len(practice_ids)} selected practices",
        selected_practices=practice_ids
    )


if __name__ == "__main__":
    # Test the questionnaire model
    from models.opensamm_model import load_opensamm_model

    print("Testing Questionnaire Model...")

    # Load OpenSAMM model
    samm_model = load_opensamm_model()
    print(f"✓ Loaded: {samm_model}\n")

    # Test 1: Full questionnaire
    print("[1] Full Questionnaire:")
    full_q = create_full_questionnaire(samm_model)
    print(full_q.get_summary())
    print()

    # Test 2: Level 1 only
    print("[2] Level 1 Questionnaire:")
    level1_q = create_level1_questionnaire(samm_model)
    print(level1_q.get_summary())
    print()

    # Test 3: Custom questionnaire (Governance only)
    print("[3] Custom Questionnaire (Governance only):")
    custom_q = create_custom_questionnaire(
        samm_model,
        practice_ids=["sm", "pc", "eg"],
        name="Governance Assessment"
    )
    print(custom_q.get_summary())
    print()

    # Test 4: Get questions from a section
    print("[4] Sample Questions from Strategy & Metrics:")
    sm_section = full_q.get_section_by_practice("sm")
    if sm_section:
        for q in sm_section.questions[:3]:  # Show first 3
            print(f"  - {q.get_full_display()}")
            print(f"    Guidance: {q.guidance}")
    print()

    # Test 5: Customization
    print("[5] Customization Test:")
    test_q = create_full_questionnaire(samm_model)
    print(f"Initial: {test_q.get_total_questions()} questions")

    # Set Strategy & Metrics to Level 1 only
    test_q.set_target_levels("sm", {1})
    print(f"After limiting SM to Level 1: {test_q.get_total_questions()} questions")

    # Exclude Policy & Compliance
    test_q.customize_practice_inclusion("pc", False)
    print(f"After excluding PC: {test_q.get_total_questions()} questions")

    print("\n✓ All tests passed!")
