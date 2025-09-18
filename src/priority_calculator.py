"""
HW 1: Housing Priority Calculator - Priority Calculator Module
"""

from typing import Dict


class HousingPriorityCalculator:
    

    def points_for_class_year(self, year: int) -> int:
       
        if year == 1:
            return 2
        if year == 2:
            return 5
        if year == 3:
            return 9
        if year == 4:
            return 14
        return 0

    def points_for_graduation(self, is_graduating: bool) -> int:
       
        return 7 if is_graduating else 1

    def points_for_credits(self, num_credits: int) -> int:
    
        if num_credits <= 30:
            score = num_credits
        elif num_credits <= 60:
            score = 30 + (num_credits - 30) * 2
        else:
            score = 30 + 60 + int((num_credits - 60) * 0.5)
        return min(score, 100)

    def points_for_additional_questions(self, responses: Dict[str, bool]) -> int:
       
        score = 0
        if responses.get("athlete", False):
            score += 4
        if responses.get("first_gen", False):
            score += 6
        if responses.get("resident_assistant", False):
            score += 8
        return score

    def calculate_total_score(
        self,
        year: int,
        is_graduating: bool,
        num_credits: int,
        additional_responses: Dict[str, bool],
    ) -> int:
        
        return (
            self.points_for_class_year(year)
            + self.points_for_graduation(is_graduating)
            + self.points_for_credits(num_credits)
            + self.points_for_additional_questions(additional_responses)
        )
