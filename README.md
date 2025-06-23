# HW 1: Housing Priority Calculator

## Learning Outcomes
- Practice Test-Driven Development (TDD) methodology
- Practice writing functions in Python with type annotations, documentation, and tests
- Writing classes in Python with proper separation of concerns
- Understanding object-oriented design principles
- Reading and writing text files
- Learning to write tests that define requirements before implementation

## Overview
Welcome to your first programming assignment of the semester! In this assignment you will be building a housing "priority score" engine in Python that decides who gets the first pick of campus housing. You'll dive into human-centered design—chatting with users, uncovering their needs, and iterating on your plan—while mastering Python basics: grabbing input, crafting if/elif/else logic, performing arithmetic, and tallying up points.

**Important: This assignment follows Test-Driven Development (TDD) principles. You will write your tests FIRST, then implement the code to make those tests pass.**

This assignment introduces you to **object-oriented programming** by separating functionality into two distinct classes:

### File Structure
1. **`question_asker.py`** - Contains the `HousingQuestionAsker` class (skeleton provided)
   * `ask_class_year()`
   * `ask_graduation_status()`
   * `ask_credits_earned()`
   * `ask_additional_questions()`

2. **`priority_calculator.py`** - Contains the `HousingPriorityCalculator` class (skeleton provided)
   * `points_for_class_year(year)`
   * `points_for_graduation(is_graduating)`
   * `points_for_credits(credits)`
   * `points_for_additional_questions(responses)`
   * `calculate_total_score(year, is_graduating, credits, additional_responses)`

3. **`hw1.py`** - Main orchestration file (skeleton provided)
   * `calculate_score()` - coordinates both classes
   * `main()` - entry point

## Your Tasks (TDD Approach):

### Part 1: Design Your Scoring System
1. **Decide** on your scoring system for each component:
   - How many points for each class year (1-4)?
   - How many points for graduating vs. not graduating?
   - How many points per credit hour?
   - What additional questions will you ask and how many points each?
2. **Document** your scoring system in `SUMMARY.md` - you'll need this for writing tests!

### Part 2: Write Tests FIRST 
**Before implementing any methods**, complete all the TODO items in the test files:

#### 2a. Complete `test_question_asker.py`
- **Write tests** for input validation and error handling
- **Test** that methods return correct data types
- **Test** invalid input followed by valid input scenarios
- **Use `@patch('builtins.input')`** to mock user input

#### 2b. Complete `test_priority_calculator.py`
- **Write specific test cases** based on your scoring system
- **Fill in expected values** for each test method
- **Test edge cases** (invalid years, negative credits, etc.)
- **Run tests** - they should all fail initially (this is expected!)

#### 2c. Complete `test_hw1.py`
- **Write integration tests** for the main coordination function
- **Use `@patch.object()`** to simulate all inputs and verify totals
- **Test** that graduation questions are only asked for seniors
- **Test** different scenarios (freshman, senior graduating, etc.)

### Part 3: Implement Methods to Make Tests Pass
Now implement the actual methods in the order that makes sense:

#### 3a. Implement `question_asker.py`
- **Implement input validation** and error handling
- **Run tests**: `python3 -m pytest test_question_asker.py -v`
- **Handle edge cases** like invalid input followed by valid input

#### 3b. Implement `priority_calculator.py`
- **Implement each method** according to your scoring system
- **Run tests frequently**: `python3 -m pytest test_priority_calculator.py -v`
- **Make sure each test passes** before moving to the next method


#### 3c. Implement `hw1.py`
- **Implement the coordination logic** between both classes
- **Run integration tests**: `python3 -m pytest test_hw1.py -v`
- **Make sure graduation questions are only asked for seniors**

### Part 4: Extending Additional Questions
* **Add at least two new yes/no prompts** (e.g., older than 23?, honors student?)
* **Update your tests first** to include these new questions
* **Then implement** the functionality to make tests pass
* **Return** a dictionary where each key corresponds to a question and the value is a boolean

### Part 5: Final Testing and Integration
* **Run all tests** to ensure everything works together:
  ```
  python3 test_runner.py
  ```

* **Execute your program (manual testing)**:
  ```bash
  python3 hw1.py
  ```

  You may run your program directly to manually test that it works in addition to unittesting.

* **Verify** that your inputs produce the expected scores according to your test cases

## Running Tests
While you are completing the test files, you may want to run individual test files at a time, instead of running them all at once. To do this, you can run test_runner.py with the -t option in your terminal to only run tests in the files you specify. Note: the test file names you provide must exist in the tests/ directory, or they won't run. 

  Example command to only run tests in test_hw1.py
  ```python3 test_runner.py -t test_hw1.py```

  You can also run multiple test files by listing the file names after the -t option. 
  Example command: 
  ```python3 test_runner.py -t test_hw1.py test_priority_calculator.py```

  If you just want to run all tests in the tests/ directory, you can run `python3 test_runner.py` omitting the `-t` flag at the end. This will run all test files with the pattern `test_*.py` inside of the tests/ directory. Make sure all your test file names start with `test_`, or else they will not run

## Submission Instructions
1. **Push** all files to your repository:
   * `question_asker.py` (fully implemented)
   * `priority_calculator.py` (fully implemented)
   * `hw1.py` (fully implemented)
   * `test_question_asker.py` (fully implemented)
   * `test_priority_calculator.py` (fully implemented)
   * `test_hw1.py` (fully implemented)
   * `SUMMARY.md` (completed with scoring rationale)

2. **Submit** the repository link on Canvas.

## Grading Rubric
- **Test Quality**: Comprehensive, well-designed tests that cover edge cases (30%)
- **TDD Process**: Evidence of writing tests before implementation (20%)
- **Implementation**: All methods work correctly and make tests pass (25%)
- **Object-Oriented Design**: Proper separation of concerns between classes (15%)
- **Documentation**: Complete SUMMARY.md with clear scoring rationale (10%)

Feel free to ask questions on Piazza if anything is unclear. Good luck!