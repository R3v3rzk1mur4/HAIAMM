"""
Questionnaire Controller

This module coordinates questionnaire workflow between the model, view, and database.
It manages questionnaire state, response collection, and validation.
"""

from typing import Optional, List, Dict
from PyQt6.QtCore import QObject, pyqtSignal

from models.opensamm_model import OpenSAMMModel
from models.assessment_model import Assessment, AssessmentResponse, ResponseType
from models.questionnaire_model import Questionnaire, Question
from services.database_service import DatabaseService


class QuestionnaireController(QObject):
    """
    Controller for questionnaire workflow.

    Manages the flow of completing a questionnaire, validates responses,
    and coordinates persistence with the database.

    Signals:
        response_added: Emitted when a response is added (question_id, response_type)
        response_removed: Emitted when a response is removed (question_id)
        progress_updated: Emitted when progress changes (completed, total, percentage)
        questionnaire_completed: Emitted when all questions are answered
    """

    # Signals
    response_added = pyqtSignal(str, str)  # question_id, response_type
    response_removed = pyqtSignal(str)  # question_id
    progress_updated = pyqtSignal(int, int, float)  # completed, total, percentage
    questionnaire_completed = pyqtSignal()

    def __init__(
        self,
        assessment: Assessment,
        questionnaire: Questionnaire,
        db_service: DatabaseService
    ):
        """
        Initialize controller.

        Args:
            assessment: The assessment being worked on
            questionnaire: The questionnaire to complete
            db_service: Database service for persistence
        """
        super().__init__()

        self.assessment = assessment
        self.questionnaire = questionnaire
        self.db_service = db_service

        # Track current position
        self.current_section_index = 0
        self.current_question_index = 0

    def get_current_section(self):
        """Get the current questionnaire section."""
        if 0 <= self.current_section_index < len(self.questionnaire.sections):
            return self.questionnaire.sections[self.current_section_index]
        return None

    def get_current_question(self) -> Optional[Question]:
        """Get the current question."""
        section = self.get_current_section()
        if section and 0 <= self.current_question_index < len(section.questions):
            return section.questions[self.current_question_index]
        return None

    def has_next_question(self) -> bool:
        """Check if there's a next question."""
        section = self.get_current_section()
        if not section:
            return False

        # Check if there's another question in current section
        if self.current_question_index < len(section.questions) - 1:
            return True

        # Check if there's another section
        return self.current_section_index < len(self.questionnaire.sections) - 1

    def has_previous_question(self) -> bool:
        """Check if there's a previous question."""
        # Check if we're not at the very beginning
        return self.current_section_index > 0 or self.current_question_index > 0

    def next_question(self) -> Optional[Question]:
        """
        Move to the next question.

        Returns:
            Next question, or None if at end
        """
        section = self.get_current_section()
        if not section:
            return None

        # Try to move to next question in current section
        if self.current_question_index < len(section.questions) - 1:
            self.current_question_index += 1
            return self.get_current_question()

        # Move to next section
        if self.current_section_index < len(self.questionnaire.sections) - 1:
            self.current_section_index += 1
            self.current_question_index = 0
            return self.get_current_question()

        # At the end
        return None

    def previous_question(self) -> Optional[Question]:
        """
        Move to the previous question.

        Returns:
            Previous question, or None if at beginning
        """
        # Try to move to previous question in current section
        if self.current_question_index > 0:
            self.current_question_index -= 1
            return self.get_current_question()

        # Move to previous section
        if self.current_section_index > 0:
            self.current_section_index -= 1
            section = self.get_current_section()
            if section:
                self.current_question_index = len(section.questions) - 1
                return self.get_current_question()

        # At the beginning
        return None

    def go_to_question(self, section_index: int, question_index: int) -> bool:
        """
        Jump to a specific question.

        Args:
            section_index: Section index
            question_index: Question index within section

        Returns:
            True if successful, False if invalid indices
        """
        if 0 <= section_index < len(self.questionnaire.sections):
            section = self.questionnaire.sections[section_index]
            if 0 <= question_index < len(section.questions):
                self.current_section_index = section_index
                self.current_question_index = question_index
                return True
        return False

    def add_response(
        self,
        question: Question,
        response_type: ResponseType,
        notes: str = "",
        evidence: str = ""
    ):
        """
        Add a response to the assessment.

        Args:
            question: The question being answered
            response_type: Response type (yes/no/partial/na)
            notes: Optional notes
            evidence: Optional evidence reference
        """
        response = AssessmentResponse(
            practice_id=question.practice_id,
            level=question.level,
            question_id=question.id,
            response=response_type,
            notes=notes,
            evidence=evidence
        )

        self.assessment.add_response(response)
        self.response_added.emit(question.id, response_type.value)
        self._update_progress()

        # Auto-save
        self._auto_save()

    def get_response(self, question: Question) -> Optional[AssessmentResponse]:
        """
        Get the current response for a question.

        Args:
            question: The question

        Returns:
            AssessmentResponse if exists, None otherwise
        """
        return self.assessment.get_response(
            question.practice_id,
            question.level,
            question.id
        )

    def remove_response(self, question: Question):
        """
        Remove a response.

        Args:
            question: The question
        """
        if self.assessment.delete_response(question.id):
            self.response_removed.emit(question.id)
            self._update_progress()
            self._auto_save()

    def get_progress(self) -> Dict:
        """
        Get completion progress.

        Returns:
            Dictionary with progress information
        """
        total = self.questionnaire.get_total_questions()
        completed = self.assessment.get_response_count()
        percentage = (completed / total * 100) if total > 0 else 0.0

        return {
            'completed': completed,
            'total': total,
            'percentage': percentage,
            'remaining': total - completed
        }

    def get_section_progress(self, section_index: int) -> Dict:
        """
        Get progress for a specific section.

        Args:
            section_index: Section index

        Returns:
            Dictionary with section progress
        """
        if 0 <= section_index < len(self.questionnaire.sections):
            section = self.questionnaire.sections[section_index]
            practice_id = section.practice.id

            # Count responses for this practice
            practice_responses = self.assessment.get_responses_for_practice(practice_id)
            total = section.get_question_count()
            completed = len([r for r in practice_responses if r.question_id in
                           [q.id for q in section.questions]])
            percentage = (completed / total * 100) if total > 0 else 0.0

            return {
                'completed': completed,
                'total': total,
                'percentage': percentage,
                'practice_name': section.practice.name
            }

        return {'completed': 0, 'total': 0, 'percentage': 0.0, 'practice_name': ''}

    def _update_progress(self):
        """Update and emit progress signal."""
        progress = self.get_progress()
        self.progress_updated.emit(
            progress['completed'],
            progress['total'],
            progress['percentage']
        )

        # Check if completed
        if progress['completed'] == progress['total'] and progress['total'] > 0:
            self.questionnaire_completed.emit()

    def _auto_save(self):
        """Auto-save assessment to database."""
        try:
            self.db_service.save_assessment(self.assessment)
        except Exception as e:
            print(f"Auto-save failed: {e}")

    def save(self) -> bool:
        """
        Explicitly save assessment.

        Returns:
            True if successful, False otherwise
        """
        try:
            self.db_service.save_assessment(self.assessment)
            return True
        except Exception as e:
            print(f"Save failed: {e}")
            return False

    def create_snapshot(self, description: str = "") -> Optional[int]:
        """
        Create a version snapshot.

        Args:
            description: Snapshot description

        Returns:
            Version ID if successful, None otherwise
        """
        if self.assessment.id is None:
            # Save first if not yet saved
            self.save()

        if self.assessment.id:
            try:
                version_id = self.db_service.save_version_snapshot(
                    self.assessment.id,
                    description=description
                )
                return version_id
            except Exception as e:
                print(f"Snapshot creation failed: {e}")

        return None

    def get_unanswered_questions(self) -> List[Question]:
        """
        Get list of unanswered questions.

        Returns:
            List of Question objects that haven't been answered
        """
        unanswered = []
        answered_ids = set(self.assessment.responses.keys())

        for question in self.questionnaire.get_all_questions():
            if question.id not in answered_ids:
                unanswered.append(question)

        return unanswered

    def is_complete(self) -> bool:
        """Check if questionnaire is complete."""
        progress = self.get_progress()
        return progress['completed'] == progress['total']

    def get_summary(self) -> Dict:
        """
        Get a summary of the questionnaire state.

        Returns:
            Dictionary with summary information
        """
        progress = self.get_progress()

        # Count by response type
        response_counts = {
            'yes': 0,
            'no': 0,
            'partial': 0,
            'na': 0
        }

        for response in self.assessment.responses.values():
            response_counts[response.response.value] += 1

        return {
            'assessment_name': self.assessment.name,
            'questionnaire_name': self.questionnaire.name,
            'progress': progress,
            'response_counts': response_counts,
            'sections': len(self.questionnaire.sections),
            'is_complete': self.is_complete()
        }


if __name__ == "__main__":
    # Test the controller
    from models.opensamm_model import load_opensamm_model
    from models.questionnaire_model import create_level1_questionnaire

    print("Testing Questionnaire Controller...")

    # Setup
    samm_model = load_opensamm_model()
    questionnaire = create_level1_questionnaire(samm_model)
    assessment = Assessment(
        name="Controller Test",
        organization="Test Org"
    )
    db = DatabaseService(":memory:")

    # Create controller
    controller = QuestionnaireController(assessment, questionnaire, db)
    print(f"✓ Controller created")
    print(f"  Questionnaire: {questionnaire.get_total_questions()} questions")

    # Get first question
    question = controller.get_current_question()
    print(f"\n✓ First question: {question.text[:50]}...")

    # Add a response
    controller.add_response(
        question,
        ResponseType.YES,
        notes="Test note"
    )
    print(f"✓ Response added")

    # Check progress
    progress = controller.get_progress()
    print(f"✓ Progress: {progress['completed']}/{progress['total']} ({progress['percentage']:.1f}%)")

    # Navigate
    next_q = controller.next_question()
    print(f"\n✓ Next question: {next_q.text[:50]}...")

    controller.add_response(next_q, ResponseType.NO)
    progress = controller.get_progress()
    print(f"✓ Progress: {progress['completed']}/{progress['total']} ({progress['percentage']:.1f}%)")

    # Get summary
    summary = controller.get_summary()
    print(f"\n✓ Summary:")
    print(f"  Complete: {summary['is_complete']}")
    print(f"  Response counts: {summary['response_counts']}")

    print("\n✓ All tests passed!")
