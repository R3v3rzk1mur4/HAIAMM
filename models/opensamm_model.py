"""
OpenSAMM Model Classes

This module defines the domain model for the OWASP Software Assurance Maturity Model (SAMM) v1.0.
It provides classes to represent business functions, security practices, maturity levels, and
assessment criteria.
"""

import json
import os
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from pathlib import Path


@dataclass
class AssessmentCriteria:
    """
    Represents a single assessment question for a maturity level.

    Attributes:
        id: Unique identifier for the question (e.g., "sm_l1_q1")
        question: The assessment question text
        guidance: Additional guidance to help answer the question
    """
    id: str
    question: str
    guidance: str = ""

    @classmethod
    def from_dict(cls, data: Dict) -> 'AssessmentCriteria':
        """Create AssessmentCriteria from dictionary."""
        return cls(
            id=data.get('id', ''),
            question=data.get('question', ''),
            guidance=data.get('guidance', '')
        )

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'id': self.id,
            'question': self.question,
            'guidance': self.guidance
        }


@dataclass
class MaturityLevel:
    """
    Represents a single maturity level (1, 2, or 3) within a security practice.

    Attributes:
        level: The maturity level number (1, 2, or 3)
        objective: High-level objective for this maturity level
        activities: List of activities to achieve this level
        assessment_criteria: List of assessment questions for this level
    """
    level: int
    objective: str
    activities: List[str] = field(default_factory=list)
    assessment_criteria: List[AssessmentCriteria] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict) -> 'MaturityLevel':
        """Create MaturityLevel from dictionary."""
        criteria = [
            AssessmentCriteria.from_dict(q)
            for q in data.get('assessment_criteria', [])
        ]
        return cls(
            level=data.get('level', 0),
            objective=data.get('objective', ''),
            activities=data.get('activities', []),
            assessment_criteria=criteria
        )

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'level': self.level,
            'objective': self.objective,
            'activities': self.activities,
            'assessment_criteria': [c.to_dict() for c in self.assessment_criteria]
        }

    def get_question_count(self) -> int:
        """Get the number of assessment questions for this level."""
        return len(self.assessment_criteria)


@dataclass
class SecurityPractice:
    """
    Represents one of the 12 security practices in OpenSAMM v1.0.

    Each practice belongs to a business function and has 3 maturity levels.

    Attributes:
        id: Short identifier (e.g., "sm", "pc", "ta")
        name: Full name of the practice (e.g., "Strategy & Metrics")
        short_name: Abbreviated name (e.g., "SM")
        objective: Overall objective of this practice
        description: Detailed description
        maturity_levels: List of 3 maturity levels
    """
    id: str
    name: str
    short_name: str
    objective: str
    description: str
    maturity_levels: List[MaturityLevel] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict) -> 'SecurityPractice':
        """Create SecurityPractice from dictionary."""
        levels = [
            MaturityLevel.from_dict(level_data)
            for level_data in data.get('maturity_levels', [])
        ]
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            short_name=data.get('short_name', ''),
            objective=data.get('objective', ''),
            description=data.get('description', ''),
            maturity_levels=levels
        )

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'short_name': self.short_name,
            'objective': self.objective,
            'description': self.description,
            'maturity_levels': [l.to_dict() for l in self.maturity_levels]
        }

    def get_level(self, level_num: int) -> Optional[MaturityLevel]:
        """
        Get a specific maturity level.

        Args:
            level_num: Level number (1, 2, or 3)

        Returns:
            MaturityLevel if found, None otherwise
        """
        for level in self.maturity_levels:
            if level.level == level_num:
                return level
        return None

    def get_questions_for_level(self, level_num: int) -> List[AssessmentCriteria]:
        """
        Get all assessment questions for a specific maturity level.

        Args:
            level_num: Level number (1, 2, or 3)

        Returns:
            List of AssessmentCriteria for the level
        """
        level = self.get_level(level_num)
        return level.assessment_criteria if level else []

    def get_total_questions(self) -> int:
        """Get total number of assessment questions across all levels."""
        return sum(level.get_question_count() for level in self.maturity_levels)


@dataclass
class BusinessFunction:
    """
    Represents one of the 4 business functions in OpenSAMM v1.0.

    Each function contains 3 security practices.

    Attributes:
        id: Identifier (e.g., "governance", "construction")
        name: Full name (e.g., "Governance")
        description: Description of the business function
        practices: List of 3 SecurityPractice objects
    """
    id: str
    name: str
    description: str
    practices: List[SecurityPractice] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict) -> 'BusinessFunction':
        """Create BusinessFunction from dictionary."""
        practices = [
            SecurityPractice.from_dict(practice_data)
            for practice_data in data.get('practices', [])
        ]
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            description=data.get('description', ''),
            practices=practices
        )

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'practices': [p.to_dict() for p in self.practices]
        }

    def get_practice(self, practice_id: str) -> Optional[SecurityPractice]:
        """
        Get a specific security practice by ID.

        Args:
            practice_id: Practice identifier (e.g., "sm", "pc")

        Returns:
            SecurityPractice if found, None otherwise
        """
        for practice in self.practices:
            if practice.id == practice_id:
                return practice
        return None


class OpenSAMMModel:
    """
    Complete OpenSAMM v1.0 model representation.

    Contains 4 business functions with 3 practices each, totaling 12 security practices.
    Each practice has 3 maturity levels with assessment criteria.

    Attributes:
        version: SAMM version (e.g., "1.0")
        model_name: Full model name
        description: Model description
        business_functions: List of 4 BusinessFunction objects
    """

    def __init__(self):
        """Initialize empty OpenSAMM model."""
        self.version: str = "1.0"
        self.model_name: str = ""
        self.description: str = ""
        self.business_functions: List[BusinessFunction] = []
        self._practice_index: Dict[str, SecurityPractice] = {}

    def load_from_config(self, config_path: Optional[str] = None):
        """
        Load OpenSAMM model from JSON configuration file.

        Args:
            config_path: Path to JSON config file. If None, uses default location.

        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config file is invalid JSON
        """
        if config_path is None:
            # Default to config/opensamm_v1_data.json
            module_dir = Path(__file__).parent.parent
            config_path = module_dir / "config" / "opensamm_v1_data.json"

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"OpenSAMM config file not found: {config_path}")

        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.version = data.get('version', '1.0')
        self.model_name = data.get('model_name', '')
        self.description = data.get('description', '')

        # Load business functions
        self.business_functions = [
            BusinessFunction.from_dict(func_data)
            for func_data in data.get('business_functions', [])
        ]

        # Build practice index for fast lookup
        self._build_practice_index()

    def _build_practice_index(self):
        """Build internal index for fast practice lookup."""
        self._practice_index = {}
        for function in self.business_functions:
            for practice in function.practices:
                self._practice_index[practice.id] = practice

    def get_practice(self, practice_id: str) -> Optional[SecurityPractice]:
        """
        Get a security practice by its ID.

        Args:
            practice_id: Practice identifier (e.g., "sm", "pc", "ta")

        Returns:
            SecurityPractice if found, None otherwise
        """
        return self._practice_index.get(practice_id)

    def get_all_practices(self) -> List[SecurityPractice]:
        """
        Get all 12 security practices.

        Returns:
            List of all SecurityPractice objects
        """
        practices = []
        for function in self.business_functions:
            practices.extend(function.practices)
        return practices

    def get_function(self, function_id: str) -> Optional[BusinessFunction]:
        """
        Get a business function by its ID.

        Args:
            function_id: Function identifier (e.g., "governance", "construction")

        Returns:
            BusinessFunction if found, None otherwise
        """
        for function in self.business_functions:
            if function.id == function_id:
                return function
        return None

    def get_practice_count(self) -> int:
        """Get total number of security practices (should be 12)."""
        return len(self._practice_index)

    def get_total_questions(self) -> int:
        """Get total number of assessment questions across all practices."""
        return sum(
            practice.get_total_questions()
            for practice in self.get_all_practices()
        )

    def generate_full_questionnaire_structure(self) -> Dict:
        """
        Generate a complete questionnaire structure for all practices.

        Returns:
            Dictionary with questionnaire structure organized by function and practice
        """
        questionnaire = {
            'version': self.version,
            'model_name': self.model_name,
            'total_questions': self.get_total_questions(),
            'functions': []
        }

        for function in self.business_functions:
            func_data = {
                'id': function.id,
                'name': function.name,
                'description': function.description,
                'practices': []
            }

            for practice in function.practices:
                practice_data = {
                    'id': practice.id,
                    'name': practice.name,
                    'short_name': practice.short_name,
                    'objective': practice.objective,
                    'levels': []
                }

                for level in practice.maturity_levels:
                    level_data = {
                        'level': level.level,
                        'objective': level.objective,
                        'questions': [
                            {
                                'id': q.id,
                                'question': q.question,
                                'guidance': q.guidance
                            }
                            for q in level.assessment_criteria
                        ]
                    }
                    practice_data['levels'].append(level_data)

                func_data['practices'].append(practice_data)

            questionnaire['functions'].append(func_data)

        return questionnaire

    def to_dict(self) -> Dict:
        """Convert entire model to dictionary for serialization."""
        return {
            'version': self.version,
            'model_name': self.model_name,
            'description': self.description,
            'business_functions': [f.to_dict() for f in self.business_functions]
        }

    def __repr__(self) -> str:
        """String representation of the model."""
        return (
            f"OpenSAMMModel(version={self.version}, "
            f"functions={len(self.business_functions)}, "
            f"practices={self.get_practice_count()}, "
            f"total_questions={self.get_total_questions()})"
        )


# Module-level function for easy loading
def load_opensamm_model(config_path: Optional[str] = None) -> OpenSAMMModel:
    """
    Convenience function to load and return an OpenSAMM model.

    Args:
        config_path: Optional path to config file

    Returns:
        Loaded OpenSAMMModel instance

    Example:
        >>> model = load_opensamm_model()
        >>> print(f"Total practices: {model.get_practice_count()}")
        Total practices: 12
    """
    model = OpenSAMMModel()
    model.load_from_config(config_path)
    return model


if __name__ == "__main__":
    # Test the model loading
    try:
        model = load_opensamm_model()
        print(f"Loaded: {model}")
        print(f"\nBusiness Functions:")
        for func in model.business_functions:
            print(f"  - {func.name} ({len(func.practices)} practices)")
            for practice in func.practices:
                total_q = practice.get_total_questions()
                print(f"      {practice.short_name}: {practice.name} ({total_q} questions)")
    except Exception as e:
        print(f"Error loading model: {e}")
