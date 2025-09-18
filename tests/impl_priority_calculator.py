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
        result = self.priority_calculator.points_for_class_year(1)
        self.assertEqual(result, 2)

    def test_points_for_class_year_sophomore(self) -> None:
        """Test points_for_class_year for sophomore (year 2)."""
        result = self.priority_calculator.points_for_class_year(2)
        self.assertEqual(result, 5)

    def test_points_for_class_year_junior(self) -> None:
        """Test points_for_class_year for junior (year 3)."""
        result = self.priority_calculator.points_for_class_year(3)
        self.assertEqual(result, 9)

    def test_points_for_class_year_senior(self) -> None:
        """Test points_for_class_year for senior (year 4)."""
        result = self.priority_calculator.points_for_class_year(4)
        self.assertEqual(result, 14)
    
    def test_points_for_graduation_true(self) -> None:
        """Test points_for_graduation when graduating."""
        result = self.priority_calculator.points_for_graduation(True)
        self.assertEqual(result, 7)

    def test_points_for_graduation_false(self) -> None:
        """Test points_for_graduation when not graduating."""
        result = self.priority_calculator.points_for_graduation(False)
        self.assertEqual(result, 1)

    def test_points_for_credits_zero(self) -> None:
        """Test points_for_credits with 0 credits."""
       
        result = self.priority_calculator.points_for_credits(0)
        self.assertEqual(result, 0)
        

    def test_points_for_credits_low(self) -> None:
       result = self.priority_calculator.points_for_credits(7)
       self.assertEqual(result, 7)

    def test_points_for_credits_medium(self) -> None:
        """Test points_for_credits with medium credit count (e.g., 15)."""
        result = self.priority_calculator.points_for_credits(17)
        self.assertEqual(result, 17)

    def test_points_for_credits_high(self) -> None:
        """Test points_for_credits with high credit count (e.g., 30)."""
        result = self.priority_calculator.points_for_credits(40)
        self.assertEqual(result, 50)

    def test_points_for_additional_questions_all_true(self) -> None:
        """Test points_for_additional_questions with all True responses."""
        responses = {"athlete": True, "first_gen": True, "resident_assistant":True}
        result = self.priority_calculator.points_for_additional_questions(responses)
        self.assertEqual(result, 18)

    def test_points_for_additional_questions_all_false(self) -> None:
        """Test points_for_additional_questions with all False responses."""
        responses = {"athlete": False, "first_gen": False, "resident_assistant": False}
        result = self.priority_calculator.points_for_additional_questions(responses)
        self.assertEqual(result, 0)

    def test_points_for_additional_questions_mixed(self) -> None:
        """Test points_for_additional_questions with mixed responses."""
        responses = {"athlete": True, "first_gen": False, "resident_assistant":True}
        result = self.priority_calculator.points_for_additional_questions(responses)
        self.assertEqual(result, 12)

    def test_calculate_total_score_freshman_scenario(self) -> None:
        """Test calculate_total_score for a freshman scenario."""
        result = self.priority_calculator.calculate_total_score(
            year=1,
            is_graduating=False,
            num_credits=8,
            additional_responses= {"athlete": False, "first_gen": True}
         )
        
        self.assertEqual(result, 17)

    def test_calculate_total_score_senior_graduating_scenario(self) -> None:
        """Test calculate_total_score for a graduating senior scenario."""
        result = self.priority_calculator.calculate_total_score(
            year=4,
            is_graduating=True,
            num_credits=16,
            additional_responses= {"athlete": True, "first_gen": True}
        )
        
        self.assertEqual(result, 47)

    def test_calculate_total_score_senior_non_graduating_scenario(self) -> None:
        """Test calculate_total_score for a non-graduating senior scenario."""
        result = self.priority_calculator.calculate_total_score(
            year=4,
            is_graduating=False,
            num_credits=20,
            additional_responses= {"athlete": False, "first_gen": False}
        )
        
        self.assertEqual(result, 35)

    def test_calculate_total_score_edge_cases(self) -> None:
         result = self.priority_calculator.calculate_total_score(
            year=4,
            is_graduating=True,
            num_credits=200,
            additional_responses= {"athlete": True, "first_gen": True, "resident_assistant": True}
         )
        
         self.assertEqual(result, 139)
