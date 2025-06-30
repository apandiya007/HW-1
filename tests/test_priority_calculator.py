#!/usr/bin/env python3
"""
Unit tests for the HousingPriorityCalculator class.
"""

import unittest
from src.priority_calculator import HousingPriorityCalculator


class TestHousingPriorityCalculator(unittest.TestCase):
    """Unit tests for the HousingPriorityCalculator class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.priority_calculator = HousingPriorityCalculator()

    def test_points_for_class_year_freshman(self) -> None:
        """Test points_for_class_year for freshman (year 1)."""
        # Based on YOUR scoring system, what should freshman get?
        # If your system gives freshman 10 points, then:
        # expected_points = 10

        # WRITE YOUR TEST HERE FIRST, THEN IMPLEMENT THE METHOD
        pass

    def test_points_for_class_year_sophomore(self) -> None:
        """Test points_for_class_year for sophomore (year 2)."""
        # Based on YOUR scoring system, what should sophomores get?
        # WRITE YOUR TEST HERE FIRST, THEN IMPLEMENT THE METHOD
        pass

    def test_points_for_class_year_junior(self) -> None:
        """Test points_for_class_year for junior (year 3)."""
        # Based on YOUR scoring system, what should juniors get?
        # WRITE YOUR TEST HERE FIRST, THEN IMPLEMENT THE METHOD
        pass

    def test_points_for_class_year_senior(self) -> None:
        """Test points_for_class_year for senior (year 4)."""
        # Based on YOUR scoring system, what should seniors get?
        # WRITE YOUR TEST HERE FIRST, THEN IMPLEMENT THE METHOD
        pass

    def test_points_for_class_year_invalid(self) -> None:
        """Test points_for_class_year with invalid year."""
        # What should happen with year 0 or year 5?
        # Should you return 0 points or raise an exception?
        pass

    def test_points_for_graduation_true(self) -> None:
        """Test points_for_graduation when graduating."""
        # How many points should graduating students get?
        pass

    def test_points_for_graduation_false(self) -> None:
        """Test points_for_graduation when not graduating."""
        # How many points should non-graduating students get?
        pass

    def test_points_for_credits_zero(self) -> None:
        """Test points_for_credits with 0 credits."""
        # What should 0 credits give? Usually 0 points.
        # result = self.priority_calculator.points_for_credits(0)
        # self.assertEqual(result, 0)
        pass

    def test_points_for_credits_low(self) -> None:
        """Test points_for_credits with low credit count (e.g., 7)."""
        pass

    def test_points_for_credits_medium(self) -> None:
        """Test points_for_credits with medium credit count (e.g., 15)."""
        # Test your scoring system with 15 credits
        pass

    def test_points_for_credits_high(self) -> None:
        """Test points_for_credits with high credit count (e.g., 30)."""
        # Test your scoring system with 30 credits
        pass

    def test_points_for_additional_questions_all_true(self) -> None:
        """Test points_for_additional_questions with all True responses."""
        # Based on YOUR additional questions and scoring:
        # If you ask 'old23' (2 pts) and 'honors' (3 pts):
        # responses = {'old23': True, 'honors': True}
        pass

    def test_points_for_additional_questions_all_false(self) -> None:
        """Test points_for_additional_questions with all False responses."""
        # Usually all False should give 0 points:
        # responses = {'old23': False, 'honors': False}
        pass

    def test_points_for_additional_questions_mixed(self) -> None:
        """Test points_for_additional_questions with mixed responses."""
        # Test partial points:
        # responses = {'old23': True, 'honors': False}
        pass

    def test_calculate_total_score_freshman_scenario(self) -> None:
        """Test calculate_total_score for a freshman scenario."""
        # Calculate expected total based on YOUR scoring system
        # Example scenario: year=1, is_graduating=False, credits=8, additional_responses={'old23': False, 'honors': True}
        # If your system: freshman=10pts, not_graduating=0pts, credits=8pts, honors_only=3pts
        # expected_total = 10 + 0 + 8 + 3 = 21
        pass

    def test_calculate_total_score_senior_graduating_scenario(self) -> None:
        """Test calculate_total_score for a graduating senior scenario."""
        # Calculate expected total for: year=4, is_graduating=True, credits=16, additional_responses={'old23': True, 'honors': True}
        # Work out the math based on YOUR scoring system first!
        pass

    def test_calculate_total_score_senior_non_graduating_scenario(self) -> None:
        """Test calculate_total_score for a non-graduating senior scenario."""
        # Calculate expected total for: year=4, is_graduating=False, credits=20, additional_responses={'old23': False, 'honors': False}
        # Work out the math based on YOUR scoring system first!
        pass

    def test_calculate_total_score_edge_cases(self) -> None:
        """Test calculate_total_score with edge cases."""
        # Test unusual combinations:
        # - Very high credits (e.g., 150)
        # - Invalid years (if your method handles them)
        # - Empty additional_responses dict
        # - Negative credits (should this be allowed?)
        pass
