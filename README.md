```markdown
# Debugging and Automation with ChatGPT

## Project Overview

This project explores how artificial intelligence, specifically ChatGPT, can be used to improve **code quality, debugging efficiency, documentation, and error handling** across different programming languages and scenarios.

Through a series of practical tasks, we analyze buggy or incomplete code, identify issues, and apply structured solutions while following best practices in software development.

---

## Tasks Summary

### 0. Debugging – Python Factorial
**File:** `debugging/factorial.py`

In this task, we fixed a Python script that calculates the factorial of a number using a loop.  
The original code caused an infinite loop because the loop counter was never decremented.

**What was fixed:**
- Added the missing decrement of the loop variable
- Ensured the script runs correctly from the command line

**Skills learned:**
- Identifying infinite loops
- Debugging logic errors
- Command-line argument handling

---

### 1. Debugging – Python Arguments
**File:** `debugging/print_arguments.py`

This task required modifying a script so that it prints **only the arguments passed**, excluding the script name.

**What was fixed:**
- Adjusted the loop to skip `sys.argv[0]`

**Skills learned:**
- Understanding `sys.argv`
- Proper handling of command-line arguments

---

### 2. Debugging – HTML / JavaScript
**File:** `debugging/change_background.html`

The goal was to fix a webpage so that clicking a button changes the background color.

**What was fixed:**
- Corrected missing HTML structure
- Ensured JavaScript runs after the DOM is loaded
- Properly linked the button event listener

**Skills learned:**
- Basic DOM manipulation
- Debugging JavaScript event handling
- HTML structure awareness

---

### 3. Debugging – Python Minesweeper
**File:** `debugging/mines.py`

This task involved improving a console-based Minesweeper game by adding a **win condition**.

**What was added:**
- A method to detect when all non-mine cells are revealed
- A victory message when the player wins
- Structural and indentation fixes

**Skills learned:**
- Game logic implementation
- Recursive functions
- State tracking in grid-based games

---

### 4. Documentation – Python Factorial (Recursive)
**File:** `debugging/factorial_recursive.py`

The objective was to document a recursive factorial function using proper Python docstrings.

**What was added:**
- Clear docstring with:
  - Function description
  - Parameters
  - Return value

**Skills learned:**
- Writing professional documentation
- Using Python docstrings correctly

---

### 5. Error Handling – Python Checkbook
**File:** `debugging/checkbook.py`

This task focused on preventing the program from crashing due to invalid user input.

**What was fixed:**
- Added `try/except` blocks to handle non-numeric input
- Prevented `ValueError` exceptions from stopping execution

**Skills learned:**
- Error handling with `try/except`
- Writing robust interactive programs
- User input validation

---

### 6. Debugging – Tic Tac Toe (Python)
**File:** `debugging/tic.py`

In this task, we debugged and improved a Tic Tac Toe game by fixing logic and input errors.

**What was fixed:**
- Prevented crashes from invalid input
- Ensured correct player win detection
- Validated board boundaries and occupied cells

**Skills learned:**
- Defensive programming
- Game state validation
- Control flow and logic correction

---

## Conclusion

This project demonstrates how ChatGPT can assist in:
- Debugging complex issues
- Improving code robustness
- Writing clear documentation
- Automating repetitive development tasks

By completing these tasks, we strengthened our understanding of debugging techniques, input validation, documentation standards, and game logic implementation across multiple technologies.
