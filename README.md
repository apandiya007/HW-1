# HW 1: Housing Priority Calculator

## Learning Outcomes
- Practice reading and contributing to existing starter code
- Practice writing functions in Python with type annotations, documentation, and tests
- Writing classes in Python with proper separation of concerns
- Understanding object-oriented design principles
- Reading and writing text files

## Overview
Welcome to your first programming assignment of the semester! In this assignment you will be building a housing "priority score" engine in Python that decides who gets the first pick of campus housing. You'll dive into human-centered design—chatting with users, uncovering their needs, and iterating on your plan—while mastering Python basics: grabbing input, crafting if/elif/else logic, performing arithmetic, and tallying up points. From initial brainstorming through prototyping to user testing and reflection, you'll sharpen both your empathy for real users and your fluency in Python—skills that will power every project you take on next.

This assignment introduces you to **object-oriented programming** by separating functionality into two distinct classes:

### File Structure
1. **`question_asker.py`** - Contains the `HousingQuestionAsker` class
   * `ask_class_year()`
   * `ask_graduation_status()`
   * `ask_credits_earned()`
   * `ask_additional_questions()`

2. **`priority_calculator.py`** - Contains the `HousingPriorityCalculator` class
   * `points_for_class_year(year)`
   * `points_for_graduation(is_graduating)`
   * `points_for_credits(credits)`
   * `points_for_additional_questions(responses)`
   * `calculate_total_score(year, is_graduating, credits, additional_responses)`

3. **`hw1.py`** - Main orchestration file
   * `calculate_score()` - coordinates both classes
   * `main()` - entry point

## Your Tasks:

### Part 1: Understanding and Running the Code
1. **Read** through all three Python files to understand how the classes work together.
2. **Implement** all the methods in both classes according to the TODO instructions.
3. **Implement** the coordination logic in `hw1.py` that uses both classes together.
4. **Run** the script in your terminal (once you have completed the assignment):
   ```bash
   python3 hw1.py
   ```
5. **Interact** with the prompts to observe how your inputs affect the final score.

### Part 2: Writing Unit Tests
Writing tests is a very important part of programming and a very essential skill. You will write tests for both classes and the main coordination function.

#### Test Files Structure:
1. **`test_question_asker.py`** - Tests for the `HousingQuestionAsker` class
   * Test input validation and error handling
   * Use `@patch('builtins.input')` to mock user input
   * Test that methods return correct data types

2. **`test_priority_calculator.py`** - Tests for the `HousingPriorityCalculator` class
   * **`points_for_class_year`**: check values for years 1–4 and edge cases
   * **`points_for_graduation`**: ensure logic works correctly (e.g., `True` ↦ X points, `False` ↦ Y points)
   * **`points_for_credits`**: test if the number of points per credit is calculated correctly
   * **`points_for_additional_questions`**: test correct points for specific user responses
   * **`calculate_total_score`**: test with various combinations of inputs

3. **`test_hw1.py`** - Integration tests for the main coordination function
   * **`calculate_score`**: use `unittest.mock.patch` with `@patch.object()` to simulate all inputs and verify the total
   * Test that graduation questions are only asked for seniors
   * Test different scenarios (freshman, senior graduating, senior not graduating, etc.)

### Part 3: Extending Additional Questions
* **Modify** `ask_additional_questions()` in the `HousingQuestionAsker` class to include at least two new yes/no prompts (e.g., older than 23?, honors student?).
* **Update** `points_for_additional_questions()` in the `HousingPriorityCalculator` class to assign distinct point values (e.g., 2 for student older than 23, 2 for honors).
* **Write** matching tests in both test files according to your questions.
* **Return** a dictionary where each key corresponds to a question and the value is a boolean (`True`/`False`).

### Part 4: Class Coordination
* **Implement** the `calculate_score()` function in `hw1.py` to:
  1. Create instances of both classes
  2. Use `HousingQuestionAsker` to gather all user input
  3. Use `HousingPriorityCalculator` to compute the final score
  4. Handle the logic for only asking graduation status if the student is a senior
  5. Return the total score

## Running Tests
You can run tests for individual components:
```bash
python3 -m pytest test_question_asker.py -v
python3 -m pytest test_priority_calculator.py -v
python3 -m pytest test_hw1.py -v
```

Or run all tests:
```bash
python3 -m pytest -v
```

## Submission Instructions
1. **Push** all files to your repository:
   * `question_asker.py`
   * `priority_calculator.py` 
   * `hw1.py`
   * `test_question_asker.py`
   * `test_priority_calculator.py`
   * `test_hw1.py`
   * `SUMMARY.md` (completed)
2. **Submit** the repository link on Canvas.

## Grading Rubric
- **Implementation**: All methods work correctly and handle edge cases
- **Object-Oriented Design**: Proper separation of concerns between classes
- **Testing**: Comprehensive unit tests and integration tests
- **Code Quality**: Clean, readable code with good practices
- **Documentation**: Complete SUMMARY.md with scoring rationale

Feel free to ask questions on Piazza if anything is unclear. Good luck!