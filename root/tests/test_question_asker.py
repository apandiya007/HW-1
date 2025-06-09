# test_question_asker.py
#!/usr/bin/env python3
"""
Unit tests for the HousingQuestionAsker class.
"""

import unittest
from unittest.mock import patch, MagicMock
from typing import Any
from question_asker import HousingQuestionAsker


class TestHousingQuestionAsker(unittest.TestCase):
    """Unit tests for the HousingQuestionAsker class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.question_asker = HousingQuestionAsker()

    @patch('builtins.input', return_value='3')
    def test_ask_class_year_valid_input(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_class_year with valid input."""
        # TODO: Test that the method returns the correct integer
        # Example:
        # result = self.question_asker.ask_class_year()
        # self.assertEqual(result, 3)
        pass

    @patch('builtins.input', side_effect=['invalid', '2'])
    def test_ask_class_year_invalid_then_valid(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_class_year with invalid input followed by valid input."""
        # TODO: Test that the method handles invalid input gracefully
        pass

    @patch('builtins.input', return_value='y')
    def test_ask_graduation_status_yes(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_graduation_status with 'y' input."""
        # TODO: Test that the method returns True for 'y'
        pass

    @patch('builtins.input', return_value='n')
    def test_ask_graduation_status_no(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_graduation_status with 'n' input."""
        # TODO: Test that the method returns False for 'n'
        pass

    @patch('builtins.input', side_effect=['maybe', 'y'])
    def test_ask_graduation_status_invalid_then_valid(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_graduation_status with invalid input followed by valid input."""
        # TODO: Test that the method handles invalid input gracefully
        pass

    @patch('builtins.input', return_value='15')
    def test_ask_credits_earned_valid(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_credits_earned with valid input."""
        # TODO: Test that the method returns the correct integer
        pass

    @patch('builtins.input', side_effect=['not_a_number', '20'])
    def test_ask_credits_earned_invalid_then_valid(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_credits_earned with invalid input followed by valid input."""
        # TODO: Test that the method handles invalid input gracefully
        pass

    @patch('builtins.input', side_effect=['y', 'n'])
    def test_ask_additional_questions(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_additional_questions with sample responses."""
        # TODO: Test that the method returns a dictionary with boolean values
        # Example expected result: {'old23': True, 'honors': False}
        pass

    @patch('builtins.input', side_effect=['invalid', 'y', 'maybe', 'n'])
    def test_ask_additional_questions_with_invalid_input(self, mock_input: MagicMock) -> None:
        """TODO: Test ask_additional_questions with some invalid inputs."""
        # TODO: Test that the method handles invalid input gracefully for both questions
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)