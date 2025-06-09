# priority_calculator.py
#!/usr/bin/env python3
"""
HW 1: Housing Priority Calculator - Priority Calculator Module

This module contains the HousingPriorityCalculator class responsible for calculating priority scores.
Implement each method as described in the handout.
"""

from typing import Dict

class HousingPriorityCalculator:
    """Class responsible for calculating priority scores based on student information."""
    
    def points_for_class_year(self, year: int) -> int:
        """TODO: Given an integer `year`, return:
          The points as an integer, using whatever scoring system you decide. Mention the scoring guide on the summary doc.
        """
        # TODO: implement logic to calculate points based on class year
        pass

    def points_for_graduation(self, is_graduating: bool) -> int:
        """TODO: Return points based on your criteria."""
        # TODO: implement logic for calculating points for a graduating student
        pass

    def points_for_credits(self, credits: int) -> int:
        """TODO: Compute points: use your scoring system. Mention this in the summary section."""
        # TODO: implement points system for credits
        pass

    def points_for_additional_questions(self, responses: Dict[str, bool]) -> int:
        """TODO: Given the dict from ask_additional_questions(), assign points:
          e.g. 2 points for True on each question, you can assign your own scoring system that you deem valid.
        """
        # TODO: implement scoring logic
        pass

    def calculate_total_score(self, year: int, is_graduating: bool, credits: int, additional_responses: Dict[str, bool]) -> int:
        """TODO: Calculate the total priority score based on all inputs.
        Args:
            year (int): Class year (1-4)
            is_graduating (bool): Whether student is graduating this semester
            credits (int): Number of credits earned
            additional_responses (dict): Dictionary of additional question responses
        Returns:
            int: Total priority score
        """
        # TODO: use other methods to calculate total score
        pass