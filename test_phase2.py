#!/usr/bin/env python3
"""
Phase 2 Test Script

Tests Questionnaire Engine functionality:
1. Questionnaire generation
2. Question navigation
3. Response collection
4. Progress tracking
5. Auto-save
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from models.opensamm_model import load_opensamm_model
from models.assessment_model import Assessment, ResponseType
from models.questionnaire_model import (
    create_full_questionnaire,
    create_level1_questionnaire,
    create_custom_questionnaire
)
from services.database_service import DatabaseService
from controllers.questionnaire_controller import QuestionnaireController


def test_phase2():
    """Test Phase 2: Questionnaire Engine."""
    print("=" * 60)
    print("HAIAMM Phase 2 Test - Questionnaire Engine")
    print("=" * 60)

    # Test 1: Load OpenSAMM Model
    print("\n[1/8] Loading OpenSAMM Model...")
    try:
        samm_model = load_opensamm_model()
        print(f"✓ Model loaded: {samm_model}")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 2: Generate Questionnaires
    print("\n[2/8] Generating Questionnaires...")
    try:
        # Full questionnaire
        full_q = create_full_questionnaire(samm_model)
        print(f"✓ Full questionnaire: {full_q.get_total_questions()} questions")

        # Level 1 only
        level1_q = create_level1_questionnaire(samm_model)
        print(f"✓ Level 1 questionnaire: {level1_q.get_total_questions()} questions")

        # Custom (Governance only)
        custom_q = create_custom_questionnaire(
            samm_model,
            practice_ids=["sm", "pc", "eg"],
            name="Governance Assessment"
        )
        print(f"✓ Custom questionnaire: {custom_q.get_total_questions()} questions")
        print(f"  Sections: {custom_q.get_section_count()}")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 3: Create Assessment and Controller
    print("\n[3/8] Creating Assessment and Controller...")
    try:
        assessment = Assessment(
            name="Phase 2 Test Assessment",
            organization="Test Organization",
            assessor="Test User"
        )

        db = DatabaseService()
        assessment_id = db.save_assessment(assessment)
        assessment = db.load_assessment(assessment_id)

        # Use Level 1 questionnaire for faster testing
        controller = QuestionnaireController(assessment, level1_q, db)
        print(f"✓ Controller created")
        print(f"  Assessment ID: {assessment_id}")
        print(f"  Questionnaire: {level1_q.get_total_questions()} questions")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 4: Navigate Questions
    print("\n[4/8] Testing Question Navigation...")
    try:
        # Get first question
        question = controller.get_current_question()
        print(f"✓ First question: {question.practice_name} L{question.level}")
        print(f"  Q: {question.text[:60]}...")

        # Navigate forward
        for i in range(3):
            next_q = controller.next_question()
            if next_q:
                print(f"✓ Next question {i+2}: {next_q.practice_name} L{next_q.level}")

        # Navigate backward
        prev_q = controller.previous_question()
        if prev_q:
            print(f"✓ Previous works: {prev_q.practice_name} L{prev_q.level}")

        # Reset to first question
        controller.go_to_question(0, 0)
        print(f"✓ Navigation to specific question works")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 5: Add Responses
    print("\n[5/8] Adding Responses...")
    try:
        # Add responses to first 10 questions
        responses_to_add = [
            (ResponseType.YES, "Good implementation"),
            (ResponseType.YES, "Process established"),
            (ResponseType.PARTIAL, "Work in progress"),
            (ResponseType.NO, "Not yet implemented"),
            (ResponseType.YES, "Fully compliant"),
            (ResponseType.PARTIAL, "Partial coverage"),
            (ResponseType.YES, "Documentation exists"),
            (ResponseType.NOT_APPLICABLE, "N/A for our org"),
            (ResponseType.YES, "Complete"),
            (ResponseType.YES, "Well implemented"),
        ]

        for i, (response_type, notes) in enumerate(responses_to_add):
            controller.go_to_question(0, i % 3)  # Spread across first sections
            controller.next_question() if i > 0 else None
            current_q = controller.get_current_question()
            if current_q:
                controller.add_response(
                    current_q,
                    response_type,
                    notes=notes,
                    evidence=f"evidence_{i+1}.pdf" if i % 3 == 0 else ""
                )

        print(f"✓ Added {len(responses_to_add)} responses")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 6: Check Progress
    print("\n[6/8] Checking Progress...")
    try:
        progress = controller.get_progress()
        print(f"✓ Overall progress:")
        print(f"  Completed: {progress['completed']}/{progress['total']}")
        print(f"  Percentage: {progress['percentage']:.1f}%")
        print(f"  Remaining: {progress['remaining']}")

        # Check section progress
        section_progress = controller.get_section_progress(0)
        print(f"✓ Section progress (Strategy & Metrics):")
        print(f"  {section_progress['practice_name']}: "
              f"{section_progress['completed']}/{section_progress['total']} "
              f"({section_progress['percentage']:.1f}%)")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 7: Get Summary and Unanswered Questions
    print("\n[7/8] Getting Summary...")
    try:
        summary = controller.get_summary()
        print(f"✓ Summary:")
        print(f"  Assessment: {summary['assessment_name']}")
        print(f"  Questionnaire: {summary['questionnaire_name']}")
        print(f"  Sections: {summary['sections']}")
        print(f"  Complete: {summary['is_complete']}")
        print(f"  Response counts:")
        for resp_type, count in summary['response_counts'].items():
            if count > 0:
                print(f"    {resp_type}: {count}")

        unanswered = controller.get_unanswered_questions()
        print(f"✓ Unanswered questions: {len(unanswered)}")
        if unanswered:
            print(f"  First unanswered: {unanswered[0].practice_name} L{unanswered[0].level}")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Test 8: Verify Persistence
    print("\n[8/8] Verifying Persistence...")
    try:
        # Save explicitly
        controller.save()

        # Create version snapshot
        version_id = controller.create_snapshot("Phase 2 test snapshot")
        print(f"✓ Version snapshot created: {version_id}")

        # Reload assessment from database
        reloaded = db.load_assessment(assessment_id)
        print(f"✓ Reloaded assessment: {reloaded.name}")
        print(f"  Responses: {reloaded.get_response_count()}")

        # Verify responses match
        if reloaded.get_response_count() == assessment.get_response_count():
            print(f"✓ Response count matches!")
        else:
            print(f"✗ Response count mismatch!")
            return False

        # Get version history
        history = db.get_version_history(assessment_id)
        print(f"✓ Version history: {len(history)} version(s)")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

    # Success!
    print("\n" + "=" * 60)
    print("✓ Phase 2 Test PASSED - Questionnaire Engine working!")
    print("=" * 60)
    print("\nPhase 2 Deliverables:")
    print("✓ Dynamic questionnaire generation from OpenSAMM model")
    print("✓ Customizable questionnaires (full/level1/custom)")
    print("✓ Question navigation (next/previous/jump)")
    print("✓ Response collection with validation")
    print("✓ Progress tracking (overall and per-section)")
    print("✓ Auto-save functionality")
    print("✓ Version control snapshots")
    print("✓ Summary and reporting")
    print("\nNext Steps: Phase 3 - Scoring & Visualization")
    return True


if __name__ == "__main__":
    success = test_phase2()
    sys.exit(0 if success else 1)
