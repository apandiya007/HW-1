# test_hw1.py
#!/usr/bin/env python3
"""
Integration tests for the Housing Priority Calculator.
Tests the main calculate_score function that coordinates both classes.
"""

import unittest
from unittest.mock import patch, MagicMock
from typing import Dict
from hw1 import calculate_score
from question_asker import HousingQuestionAsker
from priority_calculator import HousingPriorityCalculator


class TestHousingPriorityIntegration(unittest.TestCase):
    """Integration tests for the Housing Priority Calculator."""

    """
     Instructions on using unittest.mock.patch:
     
     - Each @patch decorator replaces the target function with a mock value.
     - Supply return_value to specify what the mock should return.
     - The decorated test method must accept an argument per patch, in reverse order.
     - Since we're now using classes in separate files, we patch the class methods.
     
      e.g.:
      
        @patch.object(HousingQuestionAsker, 'ask_class_year', return_value=4) 
        @patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=16)
        def test_example(self, mock_credits, mock_year):  
        
        ----> Here mock_credits corresponds to ask_credits_earned
        ----> mock_year corresponds to ask_class_year
    """

    @patch.object(HousingQuestionAsker, 'ask_class_year', return_value=4) 
    @patch.object(HousingQuestionAsker, 'ask_graduation_status', return_value=True)
    @patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=16)
    @patch.object(HousingQuestionAsker, 'ask_additional_questions', return_value={'old23': False, 'honors': True})
    def test_calculate_score_senior_graduating(self, mock_additional: MagicMock, mock_credits: MagicMock, mock_grad: MagicMock, mock_year: MagicMock) -> None:
        """TODO: Test calculate_score for a graduating senior."""
        # Based on mocks:
        #   year=4 → X pts, grad=True → Y pts, credits=16 → Z pts, additional={'honors':True} → W pts
        # Total = X+Y+Z+W (Replace with your actual scoring system)
        # 
        # This is just an example - you'll need to update based on your scoring system:
        expected = 9  # TODO: Update this based on your actual point system
        
        # TODO: Uncomment and complete this test
        # result = calculate_score()
        # self.assertEqual(result, expected)
        pass

    @patch.object(HousingQuestionAsker, 'ask_class_year', return_value=1) 
    @patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=8)
    @patch.object(HousingQuestionAsker, 'ask_additional_questions', return_value={'old23': False, 'honors': False})
    def test_calculate_score_freshman(self, mock_additional: MagicMock, mock_credits: MagicMock, mock_year: MagicMock) -> None:
        """TODO: Test calculate_score for a freshman (no graduation question should be asked)."""
        # Note: ask_graduation_status should NOT be called for freshman
        # Based on mocks:
        #   year=1 → X pts, grad=N/A → 0 pts, credits=8 → Y pts, additional=all False → Z pts
        # Total = X+0+Y+Z
        
        expected = 5  # TODO: Update this based on your actual point system
        
        # TODO: Uncomment and complete this test
        # result = calculate_score()
        # self.assertEqual(result, expected)
        pass

    @patch.object(HousingQuestionAsker, 'ask_class_year', return_value=4) 
    @patch.object(HousingQuestionAsker, 'ask_graduation_status', return_value=False)
    @patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=20)
    @patch.object(HousingQuestionAsker, 'ask_additional_questions', return_value={'old23': True, 'honors': False})
    def test_calculate_score_senior_not_graduating(self, mock_additional: MagicMock, mock_credits: MagicMock, mock_grad: MagicMock, mock_year: MagicMock) -> None:
        """TODO: Test calculate_score for a non-graduating senior."""
        expected = 7  # TODO: Update this based on your actual point system
        
        # TODO: Uncomment and complete this test
        # result = calculate_score()
        # self.assertEqual(result, expected)
        pass

    @patch.object(HousingQuestionAsker, 'ask_class_year', return_value=3) 
    @patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=12)
    @patch.object(HousingQuestionAsker, 'ask_additional_questions', return_value={'old23': True, 'honors': True})
    def test_calculate_score_junior(self, mock_additional: MagicMock, mock_credits: MagicMock, mock_year: MagicMock) -> None:
        """TODO: Test calculate_score for a junior (no graduation question should be asked)."""
        expected = 8  # TODO: Update this based on your actual point system
        
        # TODO: Uncomment and complete this test
        # result = calculate_score()
        # self.assertEqual(result, expected)
        pass

    def test_graduation_question_only_for_seniors(self) -> None:
        """TODO: Test that graduation status is only asked for seniors."""
        # This test should verify that ask_graduation_status is only called when class year is 4
        # You might want to use patch to track method calls
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)