# PIAIC Python Projects

## Overview

Welcome to my repository of Python projects from the Presidential Initiative for Artificial Intelligence and Computing (PIAIC)! This collection showcases my progress through the foundational Python programming course, focusing on core concepts like basic syntax, data structures, control flow, functions, and interactive programming. These projects are part of Quarter 1 (Q1) of the PIAIC Artificial Intelligence curriculum, designed to build practical skills in Python for beginners.

The projects follow a structured learning path, starting from introductory concepts and progressing to more advanced topics like lists, functions, and graphical applications. Each module includes hands-on exercises and small applications to reinforce learning objectives, such as writing clean, readable code and making programs interactive.

This repository is built for educational purposes and can serve as a portfolio for aspiring Python developers. All code is written in Python 3.13+ and tested in a virtual environment using `uv`.

## Project Structure

The repository is organized into numbered directories representing weekly or modular lessons. Here's the breakdown:

| Directory | Description | Key Concepts Covered |
|-----------|-------------|----------------------|
| **00_intro_python** | Introduction to Python basics, including setup, variables, data types, and simple I/O. | Environment setup, print statements, input handling, basic operators. |
| **01_expressions** | Working with expressions, arithmetic operations, and basic calculations. | Mathematical expressions, comparison operators, type conversion. |
| **02_lists** | Exploring lists: creation, manipulation, 2D lists, and list-based applications (e.g., canvas grid for an eraser tool). | List indexing, slicing, nested lists, iteration over lists. |
| **03_if_statements** | Conditional logic with if-else statements and decision-making programs. | Boolean logic, conditional branching, nested ifs. |
| **04_dictionaries** | Dictionaries for key-value data storage and operations. | Dictionary creation, access, updates, iteration. |
| **05_loop_control_flow** | Loops for repetition: for and while loops, with control statements. | Iteration, break/continue, loop patterns. |
| **06_functions_flow** | Functions: definition, parameters, return values, and modular code. | Function syntax, scope, recursion basics, lambda functions. |
| **07_information_flow** | Advanced topics like file I/O, error handling, and data processing. | Reading/writing files, try-except blocks, data validation. |

- **Additional Files**:
  - `main.py`: Entry point for running the entire project suite (if integrated).
  - `python-version`: Specifies the required Python version (3.13+).
  - `pyproject.toml`: Project configuration for dependencies and build tools.
  - `README.md`: This file!
  - `.gitignore`: Ignores virtual environments, caches, and build artifacts.
  - `uv.lock`: Lockfile for reproducible dependencies via `uv`.
  - `README.md`: Project overview.

## Setup Instructions

To run these projects locally:

1. **Clone the Repository**:
   ```
   git clone https://github.com/anushahashmi071/piaic-python-projects.git
   cd piaic-python-projects
   ```

2. **Install Dependencies**:
   - This project uses `uv` for package management. Install `uv` if not already available:
     ```
     pip install uv
     ```
   - Create a virtual environment and install dependencies:
     ```
     uv venv
     uv pip install pygame  # For graphical projects like 02_lists/03_erase_canvas.py
     ```

3. **Run a Specific Project**:
   - Navigate to the directory (e.g., `cd 02_lists`).
   - Run the script:
     ```
     uv run 03_erase_canvas.py  # Example for the eraser canvas
     ```
   - For console-based projects (e.g., in 00_intro_python):
     ```
     uv run hello.py
     ```

4. **Development Tools**:
   - Use VS Code or PyCharm with the Python extension.
   - For testing: Run `uv run python -m pytest` (if tests are added).

## Key Projects Highlights

- **00_intro_python**: Simple "Hello, World!" and basic calculator to get started with Python syntax.
- **02_lists**: Interactive eraser canvas using Pygame—a graphical grid (2D list) where users drag an eraser to "erase" blue cells to white, demonstrating list manipulation and event handling.
- **03_if_statements**: Programs for decision-making, like age verification or grade calculators.
- **06_functions_flow**: Modular functions like `greet(name)`, `is_adult(age)`, and `make_sentence(word, pos)` for reusable code.

These projects emphasize clean code practices, error handling, and interactivity, aligning with PIAIC's focus on practical AI foundations.

## Learning Outcomes

By completing these projects, I've achieved:
- Proficiency in Python fundamentals (variables, loops, conditionals).
- Hands-on experience with data structures (lists, dictionaries).
- Skills in modular programming with functions and main() entry points.
- Basic graphical programming with Pygame.
- Use of modern tools like `uv` for environment management.

## Contributing

Feel free to fork this repository, submit pull requests for improvements, or open issues for bugs. Contributions should:
- Follow PEP 8 style guidelines.
- Include docstrings for functions.
- Add tests where applicable.

<!-- ## Acknowledgments

- **PIAIC**: For the structured curriculum and resources.
- **Pygame Community**: For the graphics library used in interactive projects.
- **uv Tool**: For modern Python package management. -->

---

*Last Updated: October 07, 2025*  
*Author: [Anusha Hashmi]*  
*Contact: [anusahashmi071@gmail.com]*  

<!-- For more on PIAIC, visit [presidentialinitiative.gov.pk](https://piaic.org). Happy coding! 🚀 -->
