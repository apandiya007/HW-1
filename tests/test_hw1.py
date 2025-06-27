"""
Integration tests for the Housing Priority Calculator.
Tests the main calculate_score function that coordinates both classes.
"""

import unittest
from unittest.mock import patch
from typing import Dict

from src.question_asker import HousingQuestionAsker
from src.priority_calculator import HousingPriorityCalculator


class TestHousingPriorityIntegration(unittest.TestCase):
    """Integration tests for the Housing Priority Calculator.

    Instructions on using unittest.mock.patch:

    - Each patch context manager replaces the target function with a mock value.
    - Supply return_value to specify what the mock should return.
    - Since we're now using classes in separate files, we patch the class methods.

    e.g.:

        with patch.object(HousingQuestionAsker, 'ask_class_year', return_value=4):
            with patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=16):
                # test code here
    """

    def test_calculate_score_senior_graduating(self) -> None:
        """Test calculate_score for a graduating senior."""
        # Based on mocks:
        #   year=4 → X pts, grad=True → Y pts, credits=16 → Z pts,
        #   additional={'honors':True} → W pts
        # Total = X+Y+Z+W (Replace with your actual scoring system)
        #
        # This is just an example - you'll need to update based on your scoring system:
        # expected = 9,  Update this based on your actual point system

        with patch.object(HousingQuestionAsker, "ask_class_year", return_value=4):
            with patch.object(
                HousingQuestionAsker, "ask_graduation_status", return_value=True
            ):
                with patch.object(
                    HousingQuestionAsker, "ask_credits_earned", return_value=16
                ):
                    with patch.object(
                        HousingQuestionAsker,
                        "ask_additional_questions",
                        return_value={"old23": False, "honors": True},
                    ):
                        # Uncomment and complete this test
                        # result = calculate_score()
                        # self.assertEqual(result, expected)
                        pass

    def test_calculate_score_freshman(self) -> None:
        """TODO: Test calculate_score for a freshman (no graduation question should be asked)."""
        # Note: ask_graduation_status should NOT be called for freshman
        # Based on mocks:
        #   year=1 → X pts, grad=N/A → 0 pts, credits=8 → Y pts, additional=all False → Z pts
        # Total = X+0+Y+Z

        # expected = 5, Update this based on your actual point system

        with patch.object(HousingQuestionAsker, "ask_class_year", return_value=1):
            with patch.object(
                HousingQuestionAsker, "ask_credits_earned", return_value=8
            ):
                with patch.object(
                    HousingQuestionAsker,
                    "ask_additional_questions",
                    return_value={"old23": False, "honors": False},
                ):
                    # Uncomment and complete this test
                    # result = calculate_score()
                    # self.assertEqual(result, expected)
                    pass

    def test_calculate_score_senior_not_graduating(self) -> None:
        """TODO: Test calculate_score for a non-graduating senior."""
        # expected = 7, Update this based on your actual point system

        with patch.object(HousingQuestionAsker, "ask_class_year", return_value=4):
            with patch.object(
                HousingQuestionAsker, "ask_graduation_status", return_value=False
            ):
                with patch.object(
                    HousingQuestionAsker, "ask_credits_earned", return_value=20
                ):
                    with patch.object(
                        HousingQuestionAsker,
                        "ask_additional_questions",
                        return_value={"old23": True, "honors": False},
                    ):
                        # Uncomment and complete this test
                        # result = calculate_score()
                        # self.assertEqual(result, expected)
                        pass

    def test_calculate_score_junior(self) -> None:
        """Test calculate_score for a junior (no graduation question should be asked)."""
        # expected = 8, Update this based on your actual point system

        with patch.object(HousingQuestionAsker, "ask_class_year", return_value=3):
            with patch.object(
                HousingQuestionAsker, "ask_credits_earned", return_value=12
            ):
                with patch.object(
                    HousingQuestionAsker,
                    "ask_additional_questions",
                    return_value={"old23": True, "honors": True},
                ):
                    # TODO: Uncomment and complete this test
                    # result = calculate_score()
                    # self.assertEqual(result, expected)
                    pass

    def test_graduation_question_only_for_seniors(self) -> None:
        """Test that graduation status is only asked for seniors."""
        # This test should verify that ask_graduation_status is only called when class year is 4
        # You might want to use patch to track method calls
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
