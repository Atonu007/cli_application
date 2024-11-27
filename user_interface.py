import json
import os
import time
from validationHelper import ValidationHelper  

class CLI:
    def __init__(self, employee_manager): 
        self.employee_manager = employee_manager

    def clear_screen(self):
        if os.name == 'nt':  
            os.system('cls')
        else:  
            os.system('clear')

    def show_menu(self):
        print("\n--- Employee Management System ---")
        print("1. Add a New Employee")
        print("2. Update Employee Information")
        print("3. Delete an Employee Record")
        print("4. View All Employees")
        print("5. Search for an Employee")
        print("6. Exit")

    def get_user_input(self):
        choice = input("Please enter your choice: ").strip()
        return choice

    def add_employee_flow(self):
        self.clear_screen()
        print("\n--- Add New Employee ---")
        try:
            emp_id = ValidationHelper.validate_non_empty_input("Enter Employee ID (numeric): ", is_numeric=True)
            name = ValidationHelper.validate_name(input("Enter Employee Name: ").strip())
            designation = ValidationHelper.validate_non_empty_input("Enter Employee Designation: ")
            email = ValidationHelper.validate_email(input("Enter Employee Email: ").strip())
            age = ValidationHelper.validate_numeric_input(input("Enter Employee Age (optional): ").strip() or '', allow_empty=True) or None
            department = input("Enter Department (optional): ").strip() or "No department"
            salary = ValidationHelper.validate_numeric_input(input("Enter Salary (optional): ").strip() or '', allow_empty=True) or None
            self.employee_manager.add_employee(emp_id, name, designation, email, age, department, salary)
            time.sleep(2)
            self.clear_screen()
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_employee_flow(self):
        """Flow to update an existing employee's information."""
        self.clear_screen()
        print("\n--- Update Employee Information ---")
        try:
            emp_id = ValidationHelper.validate_non_empty_input("Enter the Employee ID to update (numeric): ", is_numeric=True).strip()
            employee = self.employee_manager.find_employee_by_id(emp_id)
            if not employee:
                print(f"Error: Employee with ID '{emp_id}' not found.")
                return 
            name = ValidationHelper.validate_name(input(f"Enter new Employee Name (current: {employee.name}) (leave empty to keep unchanged): ").strip() or employee.name)
            designation = input(f"Enter new Employee Designation (current: {employee.designation}) (leave empty to keep unchanged): ").strip() or employee.designation
            email = ValidationHelper.validate_email(input(f"Enter new Employee Email (current: {employee.email}) (leave empty to keep unchanged): ").strip() or employee.email)
            age = ValidationHelper.validate_numeric_input(input(f"Enter new Employee Age (current: {employee.age}) (leave empty to keep unchanged): ").strip() or '', allow_empty=True) or employee.age
            department = input(f"Enter new Department (current: {employee.department}) (leave empty to keep unchanged): ").strip() or employee.department
            salary = ValidationHelper.validate_numeric_input(input(f"Enter new Salary (current: {employee.salary}) (leave empty to keep unchanged): ").strip() or '', allow_empty=True) or employee.salary
            self.employee_manager.update_employee(
                emp_id, name, designation, email, age, department, salary
            )
            time.sleep(2)
            self.clear_screen()
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_employee_flow(self):
        self.clear_screen()
        print("\n--- Delete Employee Record ---")
        try:
            emp_id = input("Enter the Employee ID to delete: ").strip()
            self.employee_manager.delete_employee(emp_id)
            time.sleep(2)
            self.clear_screen()
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_all_employees_flow(self):
        self.clear_screen()
        print("\n--- View All Employees ---")
        self.employee_manager.view_all_employees()

    def search_employee_flow(self):
        self.clear_screen()
        print("\n--- Search for an Employee ---")
        try:
            search_term = input("Enter the Employee Name or Designation to search: ").strip()
            results = self.employee_manager.search_employee(search_term)
            if results:
                print("\nSearch Results:")
                results_dict = [emp.to_dict() for emp in results]
                print(json.dumps(results_dict, indent=4))  
            else:
                print("No employees found matching the search criteria.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_user_input()
            if choice == '6':
                print("Exiting the program...")
                break 
            elif choice == '1':
                self.add_employee_flow()  
            elif choice == '2':
                self.update_employee_flow() 
            elif choice == '3':
                self.delete_employee_flow()  
            elif choice == '4':
                self.view_all_employees_flow()
            elif choice == '5':
                self.search_employee_flow()
            else:
                print("Invalid choice! Please try again.")
