#!/usr/bin/env python3
"""
Unit tests for the HousingQuestionAsker class.

IMPORTANT: Complete ALL test methods below BEFORE implementing any methods in question_asker.py
This follows Test-Driven Development (TDD) - write tests first, then make them pass!
"""

import unittest
from unittest.mock import patch, MagicMock
from src.question_asker import HousingQuestionAsker


class TestHousingQuestionAsker(unittest.TestCase):
    """Unit tests for the HousingQuestionAsker class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.question_asker = HousingQuestionAsker()

    def test_ask_class_year_valid_input(self) -> None:
        """Test ask_class_year with valid input."""

        with patch('builtins.input', return_value='3'):
            # TODO: Remove 'pass' and implement the test
            # You should do this by calling self.question_asker.ask_class_year()
            # and verify it returns the correct integer

            # Expected: should return 3 (the mocked input)
            pass


    @patch('builtins.input', return_value='1')
    def test_ask_class_year_freshman(self, mock_input: MagicMock) -> None:
        """Test ask_class_year returns 1 for freshman."""
        # TODO: Test that method returns 1 for freshman input
        pass

    @patch('builtins.input', return_value='4')
    def test_ask_class_year_senior(self, mock_input: MagicMock) -> None:
        """Test ask_class_year returns 4 for senior."""
        # TODO: Test that method returns 4 for senior input
        pass

    @patch('builtins.input', side_effect=['invalid', '2'])
    def test_ask_class_year_invalid_then_valid(self, mock_input: MagicMock) -> None:
        """Test ask_class_year with invalid input followed by valid input."""
        # TODO: Test that the method handles invalid input gracefully
        # Expected: should eventually return 2 after rejecting 'invalid'
        # Hint: Use side_effect to simulate multiple inputs
        pass

    @patch('builtins.input', side_effect=['0', '5', '2'])
    def test_ask_class_year_out_of_range_then_valid(self, mock_input: MagicMock) -> None:
        """Test ask_class_year with out-of-range inputs (0, 5) then valid input."""
        # TODO: Test that numbers outside 1-4 are rejected
        # Expected: should return 2 after rejecting 0 and 5
        pass

    @patch('builtins.input', return_value='y')
    def test_ask_graduation_status_yes(self, mock_input: MagicMock) -> None:
        """Test ask_graduation_status with 'y' input."""
        # TODO: Test that the method returns True for 'y'
        # Expected: should return True
        pass

    @patch('builtins.input', return_value='Y')
    def test_ask_graduation_status_uppercase_yes(self, mock_input: MagicMock) -> None:
        """Test ask_graduation_status with 'Y' input (uppercase)."""
        # TODO: Test that uppercase 'Y' also returns True
        pass

    @patch('builtins.input', return_value='n')
    def test_ask_graduation_status_no(self, mock_input: MagicMock) -> None:
        """Test ask_graduation_status with 'n' input."""
        # TODO: Test that the method returns False for 'n'
        # Expected: should return False
        pass

    @patch('builtins.input', return_value='N')
    def test_ask_graduation_status_uppercase_no(self, mock_input: MagicMock) -> None:
        """Test ask_graduation_status with 'N' input (uppercase)."""
        # TODO: Test that uppercase 'N' also returns False
        pass

    @patch('builtins.input', side_effect=['maybe', 'yes', 'y'])
    def test_ask_graduation_status_invalid_then_valid(self, mock_input: MagicMock) -> None:
        """Test ask_graduation_status with invalid inputs followed by valid input."""
        # TODO: Test that the method handles invalid input gracefully
        # Expected: should return True after rejecting 'maybe' and 'yes'
        pass

    @patch('builtins.input', return_value='15')
    def test_ask_credits_earned_valid(self, mock_input: MagicMock) -> None:
        """Test ask_credits_earned with valid input."""
        # TODO: Test that the method returns the correct integer
        # Expected: should return 15
        pass

    @patch('builtins.input', return_value='0')
    def test_ask_credits_earned_zero(self, mock_input: MagicMock) -> None:
        """Test ask_credits_earned with zero credits."""
        # TODO: Test that 0 credits is valid input
        pass

    @patch('builtins.input', return_value='120')
    def test_ask_credits_earned_high_number(self, mock_input: MagicMock) -> None:
        """Test ask_credits_earned with high credit count."""
        # TODO: Test that high credit numbers work correctly
        pass

    @patch('builtins.input', side_effect=['not_a_number', '-5', '20'])
    def test_ask_credits_earned_invalid_then_valid(self, mock_input: MagicMock) -> None:
        """Test ask_credits_earned with invalid inputs followed by valid input."""
        # TODO: Test that the method handles invalid input gracefully
        # Expected: should return 20 after rejecting 'not_a_number' and '-5'
        # Hint: Negative credits should probably be invalid
        pass

    @patch('builtins.input', side_effect=['y', 'n'])
    def test_ask_additional_questions_basic(self, mock_input: MagicMock) -> None:
        """Test ask_additional_questions with basic y/n responses."""
        # TODO: Test that the method returns a dictionary with boolean values
        # Expected result format: {'question1_key': True, 'question2_key': False}
        # 
        # You need to decide what your two additional questions will be and their keys
        # Common examples: 'old23', 'honors', 'athlete', 'work_study', etc.
        pass

    @patch('builtins.input', side_effect=['n', 'y']) 
    def test_ask_additional_questions_reverse(self, mock_input: MagicMock) -> None:
        """Test ask_additional_questions with n/y responses."""
        # TODO: Test with opposite responses (n first, y second)
        pass

    @patch('builtins.input', side_effect=['Y', 'N'])
    def test_ask_additional_questions_uppercase(self, mock_input: MagicMock) -> None:
        """Test ask_additional_questions with uppercase responses."""
        # TODO: Test that uppercase Y/N work correctly
        pass

    @patch('builtins.input', side_effect=['invalid', 'y', 'maybe', 'n'])
    def test_ask_additional_questions_with_invalid_input(self, mock_input: MagicMock) -> None:
        """Test ask_additional_questions with some invalid inputs."""
        # TODO: Test that the method handles invalid input gracefully for both questions
        # Expected: should return proper dict after rejecting 'invalid' and 'maybe'

    def test_return_types(self) -> None:
        """Test that all methods return the correct data types."""
        # TODO: This test should verify return types without mocking input
        # You might want to use patch or handle this differently
        # This is a structural test to ensure type hints are respected
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)