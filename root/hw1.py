# hw1.py
#!/usr/bin/env python3
"""
HW 1: Housing Priority Calculator

This scaffold contains method signatures and TODO instructions. Implement each part as described in the handout.
"""

def ask_class_year():
    """TODO: Ask the student for their class year and return it as int.
    Example Prompts:
      - What is your class year? (1=Freshman, 2=Sophomore, 3=Junior, 4=Senior)
    """
    # TODO: implement input parsing and validation
    pass


def points_for_class_year(year):
    """TODO: Given an integer `year`, return:
      The points as an integer, using whatever scoring system you decide. Mention the scoring guide on the summary doc.
    """
    # TODO: implement logic to calculate points based on class year
    pass


def ask_graduation_status():
    """TODO: Ask if the student is graduating this semester, this question must ONLY appear if the student is a senior. Return True for 'y', False for 'n'.
    Example Prompt:
      - Are you graduating this semester? (y/n)
    """
    # TODO: implement input loop and return boolean ('y' = TRUE, 'n' = FALSE)
    pass


def points_for_graduation(is_graduating):
    """TODO: Return points based on your criteria."""
    # TODO: implement logic for calculating points for a graduating student
    pass


def ask_credits_earned():
    """TODO: Ask for credits earned and return as int.
    Prompt:
      - How many credits have you earned?
    """
    # TODO: implement input to get the number of credits earned
    pass


def points_for_credits(credits):
    """TODO: Compute points: use your scoring system. Mention this in the summary section."""
    # TODO: implement points system for credits
    pass


def ask_additional_questions():
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


def points_for_additional_questions(responses):
    """TODO: Given the dict from ask_additional_questions(), assign points:
      e.g. 2 points for True on each question, you can assign your own scoring system that you deem valid.
    """
    # TODO: implement scoring logic
    pass


def calculate_score():
    """TODO: Orchestrate all steps:
      1) ask_class_year → add points_for_class_year()
      2) if senior → ask_graduation_status + points_for_graduation()
      3) ask_credits_earned → points_for_credits()
      4) ask_additional_questions → points_for_additional_questions()
      Return total score.
    """
    # TODO: call the above functions, sum and return score
    pass


def main():
    """Entry point: print header, compute score, print footer. (For easier readability)"""
    # TODO: implement
    pass


if __name__ == "__main__":
    main()