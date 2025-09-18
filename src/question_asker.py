"""
HW 1: Housing Priority Calculator - Question Asker Module

This module contains the HousingQuestionAsker class responsible for gathering user input.

IMPORTANT: Do NOT implement these methods until you have completed ALL tests in 
test_question_asker.py!

Step 1: Complete all required items in test_question_asker.py
Step 2: Run tests (they should fail) - this is expected!
Step 3: Implement methods below to make tests pass
Step 4: Run tests again to verify they pass
"""
from typing import Dict

class HousingQuestionAsker:
    """Class responsible for asking questions and gathering user input."""

    def ask_class_year(self) -> int:
        while True:
            try:
                year_str = input("Please enter your class year: 1 = Freshman, 2 = Sophomore, 3 = Junior, 4 = Senior ")
                year = int(year_str)
                if year in (1, 2, 3, 4):
                    return year
                print("Invalid input. Please enter 1, 2, 3, or 4")
            except ValueError:
                print("Invalid input. Please enter a number from 1-4")

            
        

    def ask_graduation_status(self) -> bool:
        while True:
            status = input("Are you graduating this semester? (y/n): ").strip().lower()
            if status in ("y", "n" ):
                return status == "y"
            print("Invalid input. Please enter 'y' or 'n' ")
        
    def ask_credits_earned(self) -> int:
        while True:
            try:
                credits_str = input("How many credits have you earned? ")
                credits = int(credits_str)
                if credits >= 0:
                    return credits
                print("Invalid input. Credits can't be negative. ")
            except ValueError:
                 print("Invalid input. Please enter a non-negative integer ")
       
    def ask_additional_questions(self) -> Dict[str, bool]:
        responses: Dict[str, bool] = {}
    
        # Q1: asks user if they are an athlete
        while True:
            ans1 = input("Are you a student athlete? (y/n): ").strip().lower()
            if ans1 in ("y", "n" ):
                responses["athlete"] = ans1 == "y"
                break
            print("Invalid input. Please enter 'y' or 'n' ")
        
        # Q2: asks user if they are a first gen college student
        while True:
            ans2 = input("Are you a first-generation college student? (y/n): ").strip().lower()
            if ans2 in ("y", "n" ):
                responses["first_gen"] = ans2 == "y"
                break
            print("Invalid input. Please enter 'y' or 'n' ")
        
        return responses
        