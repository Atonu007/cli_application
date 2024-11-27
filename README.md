# Employee Management System (CLI)

## Overview

The **Employee Management System** is a command-line application that allows users to perform CRUD (Create, Read, Update, Delete) operations on employee records. It’s designed with a modular architecture to ensure easy maintenance and future extension. The system uses a text file (`employees.txt`) for data storage in a structured format (JSON).

---

## System Architecture

The system is organized into several Python modules, each with specific responsibilities:

- **`main.py`**: The entry point of the application. Initializes components and starts the program.
- **`interface.py`**: Defines the Command-Line Interface (CLI) where users interact with the application.
- **`employee.py`**: Defines the `Employee` class, which represents employee data and methods for interacting with employee records.
- **`employeeManager.py`**: Manages employee-related operations such as adding, updating, deleting, and searching employees.
- **`fileManager.py`**: Handles reading from and writing to the employee data file (`employees.txt`).
- **`validationHelper.py`**: Provides utility functions to validate user inputs (e.g., name, email, numeric values).

---

## Code Flow

### 1. Initialization (`main.py`)

- The program begins by initializing the `FileManager`, `EmployeeManager`, and `CLI`.
- `FileManager` reads employee data from the `employees.txt` file on startup.
- `EmployeeManager` handles the logic for CRUD operations on employee records.
- `CLI` manages user input and displays the menu for user interaction.

### 2. Command-Line Interface (CLI) (`interface.py`)

- Upon starting the application, the CLI displays a menu with options:
  - **Add a New Employee**
  - **Update Employee Information**
  - **Delete an Employee Record**
  - **View All Employees**
  - **Search for an Employee**
  - **Exit**
  
- The user selects an option, and the corresponding operation is executed, such as adding, updating, or deleting employee records.

### 3. Employee Management (`employeeManager.py`)

The `EmployeeManager` class provides the following functions:
  
- **Add an Employee**: Adds a new employee after validating input and checking for duplicate employee IDs.
- **Update an Employee**: Updates an employee's details, such as name, email, salary, etc.
- **Delete an Employee**: Deletes an employee by their ID.
- **View All Employees**: Displays a list of all employees with their basic information.
- **Search Employees**: Searches for employees by name or designation.
  
Each operation is validated, and the data is saved using the `FileManager`.

### 4. Validation (`validationHelper.py`)

The `ValidationHelper` class ensures user inputs are correct:
  
- **Name Validation**: Ensures the name does not contain numbers.
- **Email Validation**: Verifies the email format.
- **Numeric Validation**: Ensures inputs like age and salary are valid numbers.
- **Non-empty Input Validation**: Ensures fields like employee ID and name are not left empty.

### 5. File Handling (`fileManager.py`)

The `FileManager` class handles reading from and writing to the `employees.txt` file:

- **Load Data**: Reads employee data in JSON format from the `employees.txt` file when the program starts.
- **Save Data**: Writes updates (add, update, delete) back to the `employees.txt` file.

### 6. Employee Class (`employee.py`)

The `Employee` class defines the structure of an employee record with the following attributes:

- **Employee ID** (`emp_id`)
- **Name**
- **Designation**
- **Email**
- **Age**
- **Department**
- **Salary**

The class provides the following methods:
  
- **`to_dict()`**: Converts an employee object to a dictionary format for JSON serialization.
- **`from_dict()`**: Creates an employee object from a dictionary.

---

## Running the Application

To run the application, follow these steps:

1. Clone the repository or download the source code.
2. Make sure you have Python installed on your system.
3. Ensure the `employees.txt` file exists in the same directory as the code.
4. Run the `main.py` file:
   ```bash
   python main.py
   ```

## Output Screenshots

Visit the following path for output screenshots:

- **[Path to output screenshots]([py_test/output](https://github.com/Atonu007/cli_application/tree/main/output))**
   
