"""
Unit tests for the HousingQuestionAsker class.

IMPORTANT: Complete ALL test methods below BEFORE implementing any methods in question_asker.py
"""

import unittest
from unittest.mock import patch
from src.question_asker import HousingQuestionAsker


class TestHousingQuestionAsker(unittest.TestCase):
    """Unit tests for the HousingQuestionAsker class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.question_asker = HousingQuestionAsker()



    def test_ask_class_year_valid_input(self) -> None:
        """Test ask_class_year with valid input.
        
        This first test is already written for you. 
        
        Use this test as an example to complete the rest of the tests.
        """
        with patch('builtins.input', return_value='3'):
            result = self.question_asker.ask_class_year()
            self.assertEqual(result, 3)

    def test_ask_class_year_freshman(self) -> None:
        """Test ask_class_year returns 1 for freshman."""
        with patch('builtins.input', return_value='1'):
            result = self.question_asker.ask_class_year()
            self.assertEqual(result, 1)
            

    def test_ask_class_year_senior(self) -> None:
        """Test ask_class_year returns 4 for senior."""
        with patch('builtins.input', return_value='4'):
            result = self.question_asker.ask_class_year()
            self.assertEqual(result, 4)
            

    def test_ask_class_year_invalid_then_valid(self) -> None:
        """Test ask_class_year with invalid input followed by valid input."""
        with patch('builtins.input', side_effect=['-4', '2']):
            result = self.question_asker.ask_class_year()
            self.assertEqual(result, 2)
            

    def test_ask_class_year_out_of_range_then_valid(self) -> None:
        """Test ask_class_year with out-of-range inputs (0, 5) then valid input."""
        with patch('builtins.input', side_effect=['0', '5', '2']):
            result = self.question_asker.ask_class_year()
            self.assertEqual(result, 2)
            

    def test_ask_graduation_status_yes(self) -> None:
        """Test ask_graduation_status with 'y' input."""
        with patch('builtins.input', return_value='y'):
            result = self.question_asker.ask_graduation_status()
            self.assertTrue(result)
            

    def test_ask_graduation_status_uppercase_yes(self) -> None:
        """Test ask_graduation_status with 'Y' input (uppercase)."""
        with patch('builtins.input', return_value='Y'):
            result = self.question_asker.ask_graduation_status()
            self.assertTrue(result)
            

    def test_ask_graduation_status_no(self) -> None:
        """Test ask_graduation_status with 'n' input."""
        with patch('builtins.input', return_value='n'):
            result = self.question_asker.ask_graduation_status()
            self.assertFalse(result)
            

    def test_ask_graduation_status_uppercase_no(self) -> None:
        """Test ask_graduation_status with 'N' input (uppercase)."""
        with patch('builtins.input', return_value='N'):
            result = self.question_asker.ask_graduation_status()
            self.assertFalse(result)
            

    def test_ask_graduation_status_invalid_then_valid(self) -> None:
        """Test ask_graduation_status with invalid inputs followed by valid input."""
        with patch('builtins.input', side_effect=['maybe', 'yes', 'y']):
            result = self.question_asker.ask_graduation_status()
            self.assertTrue(result)
            

    def test_ask_credits_earned_valid(self) -> None:
        """Test ask_credits_earned with valid input."""
        with patch('builtins.input', return_value='15'):
            result = self.question_asker.ask_credits_earned()
            self.assertEqual(result, 15)

    def test_ask_credits_earned_zero(self) -> None:
        """Test ask_credits_earned with zero credits."""
        with patch('builtins.input', return_value='0'):
            result = self.question_asker.ask_credits_earned()
            self.assertEqual(result, 0)
            

    def test_ask_credits_earned_high_number(self) -> None:
        """Test ask_credits_earned with high credit count."""
        with patch('builtins.input', return_value='120'):
            result = self.question_asker.ask_credits_earned()
            self.assertEqual(result, 120)

    def test_ask_credits_earned_invalid_then_valid(self) -> None:
        """Test ask_credits_earned with invalid inputs followed by valid input."""
        with patch('builtins.input', side_effect=['-5', '-10', '20']):
            result = self.question_asker.ask_credits_earned()
            self.assertEqual(result, 20)

    def test_ask_additional_questions_basic(self) -> None:
        """Test ask_additional_questions with basic y/n responses."""
        with patch('builtins.input', side_effect=['y', 'n']):
            result = self.question_asker.ask_additional_questions()
            self.assertEqual(result, {"athlete": True, "first_gen": False})

    def test_ask_additional_questions_reverse(self) -> None:
        """Test ask_additional_questions with n/y responses."""
        with patch('builtins.input', side_effect=['n', 'y']):
            result = self.question_asker.ask_additional_questions()
            self.assertEqual(result, {"athlete": False, "first_gen": True})

    def test_ask_additional_questions_uppercase(self) -> None:
        """Test ask_additional_questions with uppercase responses."""
        with patch('builtins.input', side_effect=['Y', 'N']):
            result = self.question_asker.ask_additional_questions()
            self.assertEqual(result, {"athlete": True, "first_gen": False})


    def test_ask_additional_questions_with_invalid_input(self) -> None:
        """Test ask_additional_questions with some invalid inputs."""
        with patch('builtins.input', side_effect=['invalid', 'y', 'maybe', 'n']):
            result = self.question_asker.ask_additional_questions()
            self.assertEqual(result, {"athlete": True, "first_gen": False})
