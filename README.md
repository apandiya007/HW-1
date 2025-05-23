# HW 1: Housing Priority Calculator

## Overview

Welcome to your first programming assignment of the semester! In this assignment you will be building a housing “priority score” engine in Python that decides who gets the first pick of campus housing.  You’ll dive into human-centered design—chatting with users, uncovering their needs, and iterating on your plan—while mastering Python basics: grabbing input, crafting if/elif/else logic, performing arithmetic, and tallying up points. From initial brainstorming through prototyping to user testing and reflection, you’ll sharpen both your empathy for real users and your fluency in Python—skills that will power every project you take on next. You will use the provided scaffold (`hw1.py`) which contains separate methods for:

1. **User input**
   * `ask_class_year()`
   * `ask_graduation_status()`
   * `ask_credits_earned()`
   * `ask_additional_questions()`
2. **Business logic**
   * `points_for_class_year(year)`
   * `points_for_graduation(is_graduating)`
   * `points_for_credits(credits)`
   * `points_for_additional_questions(response)`
3. **Orchestration**
   * `calculate_score()`
   * `main()`

## Your tasks:

### Part 1: Understanding and Running the Code

1. **Read** through `hw1.py` to see how each method should work and how they collaborate.
2. **Run** the script in your terminal (once you have completed the assignment):
   ```bash
   python3 hw1.py
   ```
3. **Interact** with the prompts to observe how your inputs affect the final score.

### Part 2: Writing Unit Tests

Writing tests is a very important part of programming and a very essential skill. You will have to write tests for your methods and ensure that they work as intended.

1. **Navigate** to `tests/` in your project root.
2. **Enter** the file `tests/test_hw1.py`.
3. **Write** test cases for each of these methods:
   * **points_for_class_year**: check values for years 1–4 and that the correct points are being assigned.
   * **points_for_graduation**: ensure that your logic works correctly, for example: `True` ↦ 1, `False` ↦ 0.
   * **points_for_credits**: test if the number of points per credit is calculated correctly.
   * **points_for_additional_questions**: test that your method returns the correct number of points for specific answers by the users.
   * **calculate_score**: use `unittest.mock.patch` to simulate all inputs and verify the total. More instructions for this are inside the test file.



### Part 3: Extending Additional Questions

* **Modify** `ask_additional_questions()` to include at least two new yes/no prompts (e.g., older than 23?, honors student?).
* **Assign** distinct point values (e.g., 2 for student older than 23, 2 for honors).
* **Write** matching tests according to your questions.
* **Return** a dictionary where each key corresponds to a question and the value contains `'y'/'n'` as per the user input.

## Submission Instructions

1. **Push** to your repository and submit the link on canvas.

## Grading Rubric


Feel free to ask questions on Piazza if anything is unclear. Good luck!
