# question_asker.py
#!/usr/bin/env python3
"""
HW 1: Housing Priority Calculator - Question Asker Module

This module contains the HousingQuestionAsker class responsible for gathering user input.
Implement each method as described in the handout.
"""

class HousingQuestionAsker:
    """Class responsible for asking questions and gathering user input."""
    
    def ask_class_year(self):
        """TODO: Ask the student for their class year and return it as int.
        Example Prompts:
          - What is your class year? (1=Freshman, 2=Sophomore, 3=Junior, 4=Senior)
        """
        # TODO: implement input parsing and validation
        pass

    def ask_graduation_status(self):
        """TODO: Ask if the student is graduating this semester, this question must ONLY appear if the student is a senior. Return True for 'y', False for 'n'.
        Example Prompt:
          - Are you graduating this semester? (y/n)
        """
        # TODO: implement input loop and return boolean ('y' = TRUE, 'n' = FALSE)
        pass

    def ask_credits_earned(self):
        """TODO: Ask for credits earned and return as int.
        Prompt:
          - How many credits have you earned?
        """
        # TODO: implement input to get the number of credits earned
        pass

    def ask_additional_questions(self):
        """TODO: Ask at least two yes/no prompts and return a dict of responses.
        Example keys:
          - 'old23': Are you older than 23? (y/n)
          - 'honors': Are you in the honors program? (y/n)
        Return: dict where values are booleans.
        
        Eg: return {
            'old23': older_than_23,    # a y/n from your first prompt
            'honors': in_honors_program # a y/n from your second prompt
        }
        """
        # TODO: implement prompts and fill a dict
        pass