LAB 1 – MLOps (IE-7374)

This lab focuses on setting up a Python project with virtual environments, source code, testing frameworks, and CI/CD integration using GitHub Actions.

------------------------------------------------------------
Steps Covered
------------------------------------------------------------

1. Virtual Environment
   - Created using: python -m venv .venv
   - Activated and verified dependencies with: pip list

2. GitHub Repository
   - Initialized with: git init
   - Folder structure:
        src/        → Source code
        test/       → Test files
        data/       → Data (if required)
   - Added .gitignore to exclude venv and cache files

3. Code Development
   - File: src/calculator.py
        fun1() → addition
        fun2() → subtraction
        fun3() → multiplication
        fun4() → combined operation

4. Testing
   - Pytest: test/test_pytest.py
   - Unittest: test/test_unittest.py
   - Commands:
        pytest -v
        python -m unittest discover -s test -p "test_*.py" -v

5. CI/CD Setup
   - Workflows added under .github/workflows/
        pytest_action.yml
        unittest_action.yml
   - Runs automatically on every push to main
   - Verifies tests and prints pass/fail status

------------------------------------------------------------
Tools Used
------------------------------------------------------------

Python 3.12
Pytest
Unittest
GitHub Actions
Loguru (for logging)

------------------------------------------------------------
Result
------------------------------------------------------------

✅ All tests passed locally and in GitHub Actions  
✅ Clean repo structure ready for grading  
✅ Includes both Pytest and Unittest CI workflows
