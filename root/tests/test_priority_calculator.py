# test_priority_calculator.py
#!/usr/bin/env python3
"""
Unit tests for the HousingPriorityCalculator class.
"""

import unittest
from typing import Dict
from priority_calculator import HousingPriorityCalculator


class TestHousingPriorityCalculator(unittest.TestCase):
    """Unit tests for the HousingPriorityCalculator class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.priority_calculator = HousingPriorityCalculator()

    def test_points_for_class_year_freshman(self) -> None:
        """TODO: Test points_for_class_year for freshman (year 1)."""
        # TODO: Test that year 1 returns expected points
        # Example:
        # result = self.priority_calculator.points_for_class_year(1)
        # self.assertEqual(result, expected_points_for_freshman)
        pass

    def test_points_for_class_year_sophomore(self) -> None:
        """TODO: Test points_for_class_year for sophomore (year 2)."""
        # TODO: Test that year 2 returns expected points
        pass

    def test_points_for_class_year_junior(self) -> None:
        """TODO: Test points_for_class_year for junior (year 3)."""
        # TODO: Test that year 3 returns expected points
        pass

    def test_points_for_class_year_senior(self) -> None:
        """TODO: Test points_for_class_year for senior (year 4)."""
        # TODO: Test that year 4 returns expected points
        pass

    def test_points_for_class_year_invalid(self) -> None:
        """TODO: Test points_for_class_year with invalid year."""
        # TODO: Test behavior with year outside 1-4 range
        # You might return 0 points or raise an exception - document your choice
        pass

    def test_points_for_graduation_true(self) -> None:
        """TODO: Test points_for_graduation when graduating."""
        # TODO: Test that True returns expected points for graduating students
        pass

    def test_points_for_graduation_false(self) -> None:
        """TODO: Test points_for_graduation when not graduating."""
        # TODO: Test that False returns expected points for non-graduating students
        pass

    def test_points_for_credits_zero(self) -> None:
        """TODO: Test points_for_credits with 0 credits."""
        # TODO: Test scoring for 0 credits
        pass

    def test_points_for_credits_low(self) -> None:
        """TODO: Test points_for_credits with low credit count (e.g., 7)."""
        # TODO: Test scoring for low credit count
        pass

    def test_points_for_credits_medium(self) -> None:
        """TODO: Test points_for_credits with medium credit count (e.g., 15)."""
        # TODO: Test scoring for medium credit count
        pass

    def test_points_for_credits_high(self) -> None:
        """TODO: Test points_for_credits with high credit count (e.g., 30)."""
        # TODO: Test scoring for high credit count
        pass

    def test_points_for_additional_questions_all_true(self) -> None:
        """TODO: Test points_for_additional_questions with all True responses."""
        # TODO: Test with responses like {'old23': True, 'honors': True}
        pass

    def test_points_for_additional_questions_all_false(self) -> None:
        """TODO: Test points_for_additional_questions with all False responses."""
        # TODO: Test with responses like {'old23': False, 'honors': False}
        pass

    def test_points_for_additional_questions_mixed(self) -> None:
        """TODO: Test points_for_additional_questions with mixed responses."""
        # TODO: Test with responses like {'old23': True, 'honors': False}
        pass

    def test_calculate_total_score_freshman_scenario(self) -> None:
        """TODO: Test calculate_total_score for a freshman scenario."""
        # TODO: Test with year=1, is_graduating=False, credits=8, additional_responses={'old23': False, 'honors': True}
        # Calculate expected total based on your scoring system
        pass

    def test_calculate_total_score_senior_graduating_scenario(self) -> None:
        """TODO: Test calculate_total_score for a graduating senior scenario."""
        # TODO: Test with year=4, is_graduating=True, credits=16, additional_responses={'old23': True, 'honors': True}
        # Calculate expected total based on your scoring system
        pass

    def test_calculate_total_score_senior_non_graduating_scenario(self) -> None:
        """TODO: Test calculate_total_score for a non-graduating senior scenario."""
        # TODO: Test with year=4, is_graduating=False, credits=20, additional_responses={'old23': False, 'honors': False}
        # Calculate expected total based on your scoring system
        pass

    def test_calculate_total_score_edge_cases(self) -> None:
        """TODO: Test calculate_total_score with edge cases."""
        # TODO: Test with unusual combinations like very high credits, invalid years, etc.
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)