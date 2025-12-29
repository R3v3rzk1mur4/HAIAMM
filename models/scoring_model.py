"""
Scoring Model

This module provides maturity scoring algorithms for HAIAMM multi-domain assessments.
It calculates achieved maturity levels and scores based on questionnaire responses.
Supports both OpenSAMM (single domain) and HAIAMM (multi-domain) models.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union
from models.assessment_model import Assessment, AssessmentResponse
from models.opensamm_model import OpenSAMMModel, SecurityPractice

# Import HAIAMMModel conditionally for multi-domain support
try:
    from models.haiamm_model import HAIAMMModel
    HAIAMM_AVAILABLE = True
except ImportError:
    HAIAMM_AVAILABLE = False
    HAIAMMModel = None


@dataclass
class LevelScore:
    """
    Score for a single maturity level.

    Attributes:
        level: Maturity level (1, 2, or 3)
        total_questions: Total questions for this level
        answered_questions: Number of questions answered
        yes_count: Number of "yes" responses
        partial_count: Number of "partial" responses
        no_count: Number of "no" responses
        na_count: Number of "N/A" responses
        score: Calculated score (0-100%)
        is_achieved: Whether this level is achieved (>= 80%)
    """
    level: int
    total_questions: int = 0
    answered_questions: int = 0
    yes_count: int = 0
    partial_count: int = 0
    no_count: int = 0
    na_count: int = 0
    score: float = 0.0
    is_achieved: bool = False

    def calculate_score(self):
        """
        Calculate score for this level.

        Scoring:
        - Yes = 1.0 point
        - Partial = 0.5 points
        - No = 0.0 points
        - N/A = excluded from calculation
        """
        if self.total_questions == 0:
            self.score = 0.0
            self.is_achieved = False
            return

        # Calculate points (excluding N/A)
        scorable_questions = self.total_questions - self.na_count
        if scorable_questions == 0:
            self.score = 0.0
            self.is_achieved = False
            return

        points = (self.yes_count * 1.0) + (self.partial_count * 0.5)
        max_points = scorable_questions * 1.0

        self.score = (points / max_points) * 100.0 if max_points > 0 else 0.0
        self.is_achieved = self.score >= 80.0


@dataclass
class PracticeScore:
    """
    Calculated maturity score for a security practice.

    Attributes:
        practice_id: Practice identifier
        practice_name: Practice full name
        achieved_level: Highest achieved maturity level (0-3)
        level_scores: Scores for each maturity level
        overall_score: Overall practice score (0-100%)
    """
    practice_id: str
    practice_name: str
    achieved_level: int = 0
    level_scores: Dict[int, LevelScore] = field(default_factory=dict)
    overall_score: float = 0.0

    def calculate_overall_score(self):
        """Calculate overall practice score as average of all levels."""
        if not self.level_scores:
            self.overall_score = 0.0
            return

        total = sum(ls.score for ls in self.level_scores.values())
        self.overall_score = total / len(self.level_scores)

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'practice_id': self.practice_id,
            'practice_name': self.practice_name,
            'achieved_level': self.achieved_level,
            'overall_score': self.overall_score,
            'level_scores': {
                level: {
                    'score': ls.score,
                    'is_achieved': ls.is_achieved,
                    'yes_count': ls.yes_count,
                    'partial_count': ls.partial_count,
                    'no_count': ls.no_count,
                    'na_count': ls.na_count
                }
                for level, ls in self.level_scores.items()
            }
        }


class ScoringEngine:
    """
    Calculate maturity scores from assessment responses.

    Implements the SAMM scoring algorithm:
    - Level N is achieved if >= 80% of questions answered "yes"
    - Partial responses count as 50%
    - Achieved level is highest level meeting threshold

    Supports both OpenSAMM (single domain) and HAIAMM (multi-domain) models.
    """

    def __init__(self, samm_model: Union[OpenSAMMModel, 'HAIAMMModel']):
        """
        Initialize scoring engine.

        Args:
            samm_model: OpenSAMM or HAIAMM model instance
        """
        self.samm_model = samm_model
        self.is_multi_domain = HAIAMM_AVAILABLE and isinstance(samm_model, HAIAMMModel)

    def calculate_practice_score(
        self,
        practice: SecurityPractice,
        responses: List[AssessmentResponse]
    ) -> PracticeScore:
        """
        Calculate score for a single practice.

        Args:
            practice: SecurityPractice instance
            responses: List of responses for this practice

        Returns:
            PracticeScore with calculated scores
        """
        score = PracticeScore(
            practice_id=practice.id,
            practice_name=practice.name
        )

        # Calculate scores for each maturity level
        for maturity_level in practice.maturity_levels:
            level_num = maturity_level.level
            level_questions = maturity_level.assessment_criteria

            # Initialize level score
            level_score = LevelScore(
                level=level_num,
                total_questions=len(level_questions)
            )

            # Count responses for this level
            level_responses = [
                r for r in responses
                if r.level == level_num
            ]

            level_score.answered_questions = len(level_responses)

            for response in level_responses:
                response_value = response.response.value
                if response_value == 'yes':
                    level_score.yes_count += 1
                elif response_value == 'partial':
                    level_score.partial_count += 1
                elif response_value == 'no':
                    level_score.no_count += 1
                elif response_value == 'na':
                    level_score.na_count += 1

            # Calculate score
            level_score.calculate_score()
            score.level_scores[level_num] = level_score

        # Determine achieved level (highest level with >= 80% score)
        score.achieved_level = 0
        for level_num in sorted(score.level_scores.keys()):
            if score.level_scores[level_num].is_achieved:
                score.achieved_level = level_num
            else:
                # Stop at first non-achieved level (levels must be sequential)
                break

        # Calculate overall score
        score.calculate_overall_score()

        return score

    def calculate_all_scores(self, assessment: Assessment, domain_id: Optional[str] = None) -> Dict[str, PracticeScore]:
        """
        Calculate scores for all practices.

        Args:
            assessment: Assessment with responses
            domain_id: Optional domain ID for multi-domain models

        Returns:
            Dictionary mapping practice_id to PracticeScore
        """
        scores = {}

        if self.is_multi_domain:
            # For HAIAMM, get practices for specific domain or all practices
            if domain_id:
                practices = self.samm_model.get_all_practices_for_domain(domain_id)
            else:
                # Get all practices across all domains
                practices = []
                for domain in self.samm_model.domains:
                    practices.extend(domain.get_all_practices())
        else:
            # For OpenSAMM, get all practices (single domain)
            practices = self.samm_model.get_all_practices()

        for practice in practices:
            # Get responses for this practice
            practice_responses = assessment.get_responses_for_practice(practice.id, domain_id)

            # Calculate score
            practice_score = self.calculate_practice_score(practice, practice_responses)
            scores[practice.id] = practice_score

        return scores

    def calculate_domain_scores(self, assessment: Assessment) -> Dict[str, Dict[str, PracticeScore]]:
        """
        Calculate scores for all domains (HAIAMM multi-domain only).

        Args:
            assessment: Assessment with responses

        Returns:
            Dictionary mapping domain_id to dictionary of practice scores
        """
        if not self.is_multi_domain:
            # For OpenSAMM, return single domain with all scores
            return {'default': self.calculate_all_scores(assessment)}

        domain_scores = {}
        for domain in self.samm_model.domains:
            domain_scores[domain.id] = self.calculate_all_scores(assessment, domain.id)

        return domain_scores

    def calculate_function_average(
        self,
        function_id: str,
        practice_scores: Dict[str, PracticeScore]
    ) -> float:
        """
        Calculate average maturity for a business function.

        Args:
            function_id: Business function identifier
            practice_scores: Dictionary of practice scores

        Returns:
            Average achieved level for the function (0-3)
        """
        if self.is_multi_domain:
            # For HAIAMM, get function from first domain (they're all the same structure)
            function = None
            if self.samm_model.domains:
                function = self.samm_model.domains[0].get_function(function_id)
        else:
            # For OpenSAMM
            function = self.samm_model.get_function(function_id)

        if not function:
            return 0.0

        practice_ids = [p.id for p in function.practices]
        levels = [
            practice_scores[pid].achieved_level
            for pid in practice_ids
            if pid in practice_scores
        ]

        return sum(levels) / len(levels) if levels else 0.0

    def calculate_overall_maturity(
        self,
        practice_scores: Dict[str, PracticeScore]
    ) -> float:
        """
        Calculate overall organizational maturity.

        Args:
            practice_scores: Dictionary of practice scores

        Returns:
            Average achieved level across all practices (0-3)
        """
        if not practice_scores:
            return 0.0

        total_level = sum(score.achieved_level for score in practice_scores.values())
        return total_level / len(practice_scores)

    def get_summary(
        self,
        assessment: Assessment,
        practice_scores: Dict[str, PracticeScore]
    ) -> Dict:
        """
        Get comprehensive scoring summary.

        Args:
            assessment: Assessment instance
            practice_scores: Calculated practice scores

        Returns:
            Dictionary with summary information
        """
        # Calculate function averages
        function_averages = {}

        if self.is_multi_domain:
            # For HAIAMM, get business functions from first domain (they're all the same)
            business_functions = self.samm_model.domains[0].business_functions if self.samm_model.domains else []
        else:
            # For OpenSAMM, get business functions directly
            business_functions = self.samm_model.business_functions

        for function in business_functions:
            avg = self.calculate_function_average(function.id, practice_scores)
            function_averages[function.id] = {
                'name': function.name,
                'average_level': avg,
                'practices': [
                    {
                        'id': p.id,
                        'name': p.name,
                        'achieved_level': practice_scores.get(p.id, PracticeScore(p.id, p.name)).achieved_level
                    }
                    for p in function.practices
                ]
            }

        overall_maturity = self.calculate_overall_maturity(practice_scores)

        # Count practices by achieved level
        level_distribution = {0: 0, 1: 0, 2: 0, 3: 0}
        for score in practice_scores.values():
            level_distribution[score.achieved_level] += 1

        return {
            'assessment_name': assessment.name,
            'total_responses': assessment.get_response_count(),
            'overall_maturity': overall_maturity,
            'function_averages': function_averages,
            'level_distribution': level_distribution,
            'practice_count': len(practice_scores),
            'practices_scored': sum(1 for s in practice_scores.values() if s.achieved_level > 0)
        }


if __name__ == "__main__":
    # Test the scoring model
    from models.opensamm_model import load_opensamm_model
    from models.assessment_model import ResponseType

    print("Testing Scoring Model...")

    # Load model
    samm_model = load_opensamm_model()
    print(f"✓ Loaded: {samm_model}\n")

    # Create test assessment with responses
    assessment = Assessment(
        name="Test Scoring",
        organization="Test Org"
    )

    # Add test responses for Strategy & Metrics (sm)
    test_responses = [
        # Level 1 - all yes (should achieve level 1)
        ("sm", 1, "sm_l1_q1", ResponseType.YES),
        ("sm", 1, "sm_l1_q2", ResponseType.YES),
        ("sm", 1, "sm_l1_q3", ResponseType.YES),
        # Level 2 - partial (should not achieve level 2)
        ("sm", 2, "sm_l2_q1", ResponseType.YES),
        ("sm", 2, "sm_l2_q2", ResponseType.PARTIAL),
        ("sm", 2, "sm_l2_q3", ResponseType.NO),
        # Level 3 - no responses
    ]

    for practice_id, level, qid, response_type in test_responses:
        assessment.add_response(AssessmentResponse(
            practice_id=practice_id,
            level=level,
            question_id=qid,
            response=response_type
        ))

    print(f"Created test assessment with {assessment.get_response_count()} responses\n")

    # Test scoring
    engine = ScoringEngine(samm_model)

    # Test single practice
    print("[1] Testing Single Practice Score:")
    sm_practice = samm_model.get_practice("sm")
    sm_responses = assessment.get_responses_for_practice("sm")
    sm_score = engine.calculate_practice_score(sm_practice, sm_responses)

    print(f"✓ Practice: {sm_score.practice_name}")
    print(f"  Achieved Level: {sm_score.achieved_level}")
    print(f"  Overall Score: {sm_score.overall_score:.1f}%")
    print(f"  Level Scores:")
    for level, ls in sorted(sm_score.level_scores.items()):
        print(f"    Level {level}: {ls.score:.1f}% (Yes:{ls.yes_count} Partial:{ls.partial_count} No:{ls.no_count}) {'✓ Achieved' if ls.is_achieved else '✗ Not Achieved'}")

    # Test all practices
    print("\n[2] Testing All Practices:")
    all_scores = engine.calculate_all_scores(assessment)
    print(f"✓ Calculated scores for {len(all_scores)} practices")
    for pid, score in all_scores.items():
        if score.achieved_level > 0:
            print(f"  {pid.upper()}: Level {score.achieved_level} ({score.overall_score:.1f}%)")

    # Test summary
    print("\n[3] Testing Summary:")
    summary = engine.get_summary(assessment, all_scores)
    print(f"✓ Overall Maturity: {summary['overall_maturity']:.2f}")
    print(f"  Total Responses: {summary['total_responses']}")
    print(f"  Practices Scored: {summary['practices_scored']}/{summary['practice_count']}")
    print(f"  Level Distribution: {summary['level_distribution']}")

    print("\n✓ All tests passed!")
