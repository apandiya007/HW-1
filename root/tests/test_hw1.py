import unittest
from unittest.mock import patch
from hw1 import (
    points_for_class_year,
    points_for_graduation,
    points_for_credits,
    points_for_additional_questions,
    calculate_score,
)

class TestHousingPriority(unittest.TestCase):
    """Unit tests for the Housing Priority Calculator."""

    def test_points_for_class_year(self):
        # TODO: write assertions for years 1-4 and an out-of-range case
        pass

    def test_points_for_graduation(self):
        # TODO: write assertions for True → 1, False → 0 (1 for TRUE is just an example, you will have to use whatever points you had assigned instead)
        pass

    def test_points_for_credits(self):
        # TODO: write assertions: credits 0,7,8,15,16, etc.
        pass

    def test_points_for_additional_questions(self):
        # TODO: simulate a sample `responses` dict and assert returned points
        pass

    """
     Instructions on using unittest.mock.patch:
     
     - Each @patch decorator replaces the target function with a mock value.
     - Supply return_value to specify what the mock should return.
     - The decorated test method must accept an argument per patch, in reverse order.
     
      e.g.:
      
        @patch('hw1.ask_class_year', return_value=4) 
        @patch('hw1.ask_credits_earned', return_value=16)
        def test_example(self, mock_credits, mock_year):  
        
        ----> Here mock_credits will take the value of @patch('hw1.ask_credits_earned', return_value=16)
        ----> Whereas, mock_year will take the value of the previous patch statement: @patch('hw1.ask_class_year', return_value=4) 
        
            # mock_credits is for ask_credits_earned, mock_year is for ask_class_year
    """

    @patch('hw1.ask_class_year', return_value=4) 
    @patch('hw1.ask_graduation_status', return_value=True)
    @patch('hw1.ask_credits_earned', return_value=16)
    @patch('hw1.ask_additional_questions', return_value={'old23': False, 'honors': True})
    def test_calculate_score(self, mock_additional, mock_credits, mock_grad, mock_year):
        # Based on mocks:
        #   year=4 → 4pts, grad=True → 1pt, credits=16//8=2pts, additional={'honors':True}→2pts
        # Total = 4+1+2+2 = 9 (This is just an example scoring system, you will have to make your own.)
        expected = 9
        self.assertEqual(calculate_score(), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
