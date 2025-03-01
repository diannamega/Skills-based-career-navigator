# Testing Guide for the Skills-Based Career Navigator

This document outlines the testing methodology, tools, and procedures used to ensure the quality and reliability of the Skills-Based Career Navigator project. It provides instructions on performing tests and understanding expected inputs and outputs.

## 1. Testing Methodology

We employ a **unit testing** methodology, focusing on testing individual functions or components of the code in isolation. This approach allows us to:

*   **Isolate bugs:** Quickly identify the source of errors.
*   **Improve code quality:** Force us to think about edge cases and potential error conditions.
*   **Facilitate refactoring:** Confidently modify code without introducing unintended side effects.
*   **Ensure reliability:** Verify that each component of the system functions as expected.

## 2. Testing Tools and Libraries

*   **`unittest` (Python Standard Library):** We use Python's built-in `unittest` framework for writing and running our unit tests. It provides the core structure for organizing tests, defining test cases, and making assertions.
*   **`pandas`:** Used for creating mock DataFrames in our tests, simulating data loading from CSV files.
*   **`networkx`:** While we don't directly test `networkx`'s internal functions, we assert that our functions correctly create and manipulate `networkx` graphs.
*   **`unittest.mock` (or `mock`):** Used for creating mock objects to isolate functions from external dependencies (e.g., the file system, database connections).

## 3. Test File Structure

The test files are organized as follows:

*   Each function that needs to be tested has its own file.
*   The test file name convention is `test_<function_name>.py`.
*   Each test file contains a class that inherits from `unittest.TestCase`.
*   Each test method within the class tests a specific aspect of the module.

## 4. Performing Tests

1.  **Ensure Dependencies are Installed:** Make sure you have the necessary libraries installed.
    ```bash
    pip install pandas networkx prettytable
    ```

2.  **Navigate to the Project Directory:** Open a terminal or command prompt and navigate to the directory containing the Python script and the `test_*.py` files.

3.  **Run the Tests:** Use the following commands to run all tests in a file:
    ```bash
    python -m unittest test_load_and_preprocess_data.py
    python -m unittest test_create_career_network.py
    python -m unittest test_calculate_overall_match.py
    python -m unittest test_recommend_careers.py
    ```

    Or, to run all tests in the current directory, use:
    ```bash
    python -m unittest discover -p "test_*.py"
    ```

4.  **Interpret the Output:** The test runner will execute the tests and display the results.
    *   `.` (dot): Indicates a passing test.
    *   `F`: Indicates a failing test (an assertion failed).
    *   `E`: Indicates a test that raised an unexpected exception (error).

    For failing or erroring tests, the output will include a traceback that helps you pinpoint the location of the problem in your code.

## 5. Example Test Cases and Expected Outputs

Here are some examples of the tests and what inputs and outputs are expected.

### 5.1 `test_load_and_preprocess_data.py`

*   **Run test with the following:**
    `python -m unittest test_load_and_preprocess_data.py`

*   **Expected Output:**
    *   The function should return the test results, one failure and two successes
        ```
        .Error loading data from dummy_dir: Failed to parse CSV
        ..
        ----------------------------------------------------------------------
        Ran 3 tests in 0.001s
        ```

*   **Test Case:** `test_load_and_preprocess_data_filenotfound`

    *   **Input (Mocked):**
        *   `os.listdir` raises a `FileNotFoundError`
    *   **Expected Output:**
        *   The function should return `.Error loading data from dummy_dir: Failed to parse CSV`

### 5.2 `test_create_career_network.py`

*   **Run test with the following:** 
    `python -m unittest test_create_career_network_simple.py`

*   **Expected Output:**
    *   The function should return the test results, one failure and two successes
        ```
        ....
        ----------------------------------------------------------------------
        Ran 4 tests in 0.003s
        ```