"""
Assessment Model Classes

This module defines the domain model for security maturity assessments.
It provides classes to represent assessments, responses to questionnaires,
and related metadata.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum


class ResponseType(Enum):
    """Valid response types for assessment questions."""
    YES = "yes"
    NO = "no"
    PARTIAL = "partial"
    NOT_APPLICABLE = "na"

    @classmethod
    def from_string(cls, value: str) -> 'ResponseType':
        """Convert string to ResponseType."""
        value_lower = value.lower()
        for response_type in cls:
            if response_type.value == value_lower:
                return response_type
        raise ValueError(f"Invalid response type: {value}")

    def to_score(self) -> float:
        """
        Convert response to numeric score.

        Returns:
            1.0 for YES, 0.5 for PARTIAL, 0.0 for NO/NA
        """
        if self == ResponseType.YES:
            return 1.0
        elif self == ResponseType.PARTIAL:
            return 0.5
        else:
            return 0.0


@dataclass
class AssessmentResponse:
    """
    Represents a single response to a questionnaire question.

    Attributes:
        practice_id: ID of the security practice (e.g., "sm", "pc")
        level: Maturity level being assessed (1, 2, or 3)
        question_id: Unique question identifier
        response: The answer (yes/no/partial/na)
        domain_id: Domain identifier (e.g., "software", "infrastructure")
        notes: Additional notes or context
        evidence: References to supporting evidence
    """
    practice_id: str
    level: int
    question_id: str
    response: ResponseType
    domain_id: str = "software"  # Default domain for backward compatibility
    notes: str = ""
    evidence: str = ""

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'practice_id': self.practice_id,
            'level': self.level,
            'question_id': self.question_id,
            'response': self.response.value,
            'domain_id': self.domain_id,
            'notes': self.notes,
            'evidence': self.evidence
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'AssessmentResponse':
        """Create AssessmentResponse from dictionary."""
        return cls(
            practice_id=data['practice_id'],
            level=data['level'],
            question_id=data['question_id'],
            response=ResponseType.from_string(data['response']),
            domain_id=data.get('domain_id', 'software'),  # Default for backward compatibility
            notes=data.get('notes', ''),
            evidence=data.get('evidence', '')
        )

    def get_score(self) -> float:
        """Get numeric score for this response (0.0, 0.5, or 1.0)."""
        return self.response.to_score()


@dataclass
class Assessment:
    """
    Represents a complete OpenSAMM assessment.

    Contains metadata about the assessment and all responses to the questionnaire.

    Attributes:
        name: Assessment name
        organization: Organization being assessed
        assessor: Person(s) conducting the assessment
        description: Optional description
        id: Database ID (None for new assessments)
        created_at: Creation timestamp
        updated_at: Last update timestamp
        responses: Dictionary of responses keyed by question_id
    """
    name: str
    organization: str = ""
    assessor: str = ""
    description: str = ""
    id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    responses: Dict[str, AssessmentResponse] = field(default_factory=dict)

    def add_response(self, response: AssessmentResponse):
        """
        Add or update a questionnaire response.

        Args:
            response: The AssessmentResponse to add
        """
        self.responses[response.question_id] = response
        self.updated_at = datetime.now()

    def get_response(
        self,
        practice_id: str,
        level: int,
        question_id: str
    ) -> Optional[AssessmentResponse]:
        """
        Retrieve a specific response.

        Args:
            practice_id: Practice identifier
            level: Maturity level
            question_id: Question identifier

        Returns:
            AssessmentResponse if found, None otherwise
        """
        return self.responses.get(question_id)

    def get_responses_for_practice(self, practice_id: str, domain_id: Optional[str] = None) -> List[AssessmentResponse]:
        """
        Get all responses for a specific practice.

        Args:
            practice_id: Practice identifier
            domain_id: Optional domain identifier to filter by domain

        Returns:
            List of AssessmentResponse objects
        """
        responses = [
            response for response in self.responses.values()
            if response.practice_id == practice_id
        ]
        if domain_id:
            responses = [r for r in responses if r.domain_id == domain_id]
        return responses

    def get_responses_for_level(
        self,
        practice_id: str,
        level: int,
        domain_id: Optional[str] = None
    ) -> List[AssessmentResponse]:
        """
        Get all responses for a specific practice and level.

        Args:
            practice_id: Practice identifier
            level: Maturity level
            domain_id: Optional domain identifier to filter by domain

        Returns:
            List of AssessmentResponse objects
        """
        responses = [
            response for response in self.responses.values()
            if response.practice_id == practice_id and response.level == level
        ]
        if domain_id:
            responses = [r for r in responses if r.domain_id == domain_id]
        return responses

    def get_completion_percentage(self, total_questions: int) -> float:
        """
        Calculate percentage of questionnaire completed.

        Args:
            total_questions: Total number of questions in the questionnaire

        Returns:
            Percentage (0-100) of questions answered
        """
        if total_questions == 0:
            return 0.0
        return (len(self.responses) / total_questions) * 100.0

    def get_response_count(self) -> int:
        """Get total number of responses."""
        return len(self.responses)

    def has_responses(self) -> bool:
        """Check if any responses have been recorded."""
        return len(self.responses) > 0

    def delete_response(self, question_id: str) -> bool:
        """
        Delete a response.

        Args:
            question_id: Question identifier

        Returns:
            True if response was deleted, False if not found
        """
        if question_id in self.responses:
            del self.responses[question_id]
            self.updated_at = datetime.now()
            return True
        return False

    def get_responses_for_domain(self, domain_id: str) -> List[AssessmentResponse]:
        """
        Get all responses for a specific domain.

        Args:
            domain_id: Domain identifier

        Returns:
            List of AssessmentResponse objects
        """
        return [
            response for response in self.responses.values()
            if response.domain_id == domain_id
        ]

    def clear_responses_for_practice(self, practice_id: str, domain_id: Optional[str] = None):
        """
        Clear all responses for a specific practice.

        Args:
            practice_id: Practice identifier
            domain_id: Optional domain identifier to filter by domain
        """
        to_delete = [
            qid for qid, response in self.responses.items()
            if response.practice_id == practice_id and (domain_id is None or response.domain_id == domain_id)
        ]
        for qid in to_delete:
            del self.responses[qid]
        if to_delete:
            self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        """
        Convert to dictionary for serialization.

        Returns:
            Dictionary representation of the assessment
        """
        return {
            'id': self.id,
            'name': self.name,
            'organization': self.organization,
            'assessor': self.assessor,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'responses': {
                qid: response.to_dict()
                for qid, response in self.responses.items()
            },
            'response_count': len(self.responses)
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Assessment':
        """
        Create Assessment from dictionary.

        Args:
            data: Dictionary with assessment data

        Returns:
            Assessment instance
        """
        assessment = cls(
            name=data['name'],
            organization=data.get('organization', ''),
            assessor=data.get('assessor', ''),
            description=data.get('description', ''),
            id=data.get('id')
        )

        # Parse timestamps
        if 'created_at' in data:
            assessment.created_at = datetime.fromisoformat(data['created_at'])
        if 'updated_at' in data:
            assessment.updated_at = datetime.fromisoformat(data['updated_at'])

        # Parse responses
        if 'responses' in data:
            for qid, response_data in data['responses'].items():
                response = AssessmentResponse.from_dict(response_data)
                assessment.responses[qid] = response

        return assessment

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"Assessment(id={self.id}, name='{self.name}', "
            f"organization='{self.organization}', "
            f"responses={len(self.responses)})"
        )


if __name__ == "__main__":
    # Test the assessment model
    print("Testing Assessment Model...")

    # Create a new assessment
    assessment = Assessment(
        name="Q4 2025 Security Assessment",
        organization="Acme Corp",
        assessor="Security Team"
    )
    print(f"Created: {assessment}")

    # Add some responses
    response1 = AssessmentResponse(
        practice_id="sm",
        level=1,
        question_id="sm_l1_q1",
        response=ResponseType.YES,
        notes="Annual risk assessment completed"
    )
    assessment.add_response(response1)

    response2 = AssessmentResponse(
        practice_id="sm",
        level=1,
        question_id="sm_l1_q2",
        response=ResponseType.PARTIAL,
        notes="Roadmap exists but needs updates"
    )
    assessment.add_response(response2)

    response3 = AssessmentResponse(
        practice_id="pc",
        level=1,
        question_id="pc_l1_q1",
        response=ResponseType.YES
    )
    assessment.add_response(response3)

    print(f"\nAfter adding responses: {assessment}")
    print(f"Completion: {assessment.get_completion_percentage(108):.1f}% (3/108 questions)")

    # Test serialization
    data = assessment.to_dict()
    print(f"\nSerialized to dict with {len(data)} fields")

    # Test deserialization
    restored = Assessment.from_dict(data)
    print(f"Restored: {restored}")
    print(f"Responses match: {len(restored.responses) == len(assessment.responses)}")

    # Test practice filtering
    sm_responses = assessment.get_responses_for_practice("sm")
    print(f"\nResponses for Strategy & Metrics: {len(sm_responses)}")
    for resp in sm_responses:
        print(f"  - {resp.question_id}: {resp.response.value} (score: {resp.get_score()})")
