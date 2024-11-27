from employee import Employee
from validationHelper import ValidationHelper  

class EmployeeManager:
    def __init__(self, file_manager):
        self.file_manager = file_manager  
        self.employees = self.file_manager.load_data()  

    def add_employee(self, emp_id, name, designation, email, age=None, department=None, salary=None):
        try:
            name = ValidationHelper.validate_name(name)
            email = ValidationHelper.validate_email(email)
            if age is not None:
                age = ValidationHelper.validate_numeric_input(age)
            if salary is not None:
                salary = ValidationHelper.validate_numeric_input(salary)
        except ValueError as e:
            print(f"Error: {e}")
            return
        if emp_id in self.employees:
            print(f"Error: Employee ID '{emp_id}' already exists.")
            return
        if any(emp.email == email for emp in self.employees.values()):
            print(f"Error: Email '{email}' is already in use.")
            return
        new_employee = Employee(emp_id, name, designation, email, age, department, salary)
        self.employees[emp_id] = new_employee
        save_message = self.file_manager.save_data(self.employees)
        print(save_message)

    def find_employee_by_id(self, emp_id):
        employee = self.employees.get(emp_id)  
        if employee:
            return employee  
        print(f"Error: Employee with ID '{emp_id}' not found.")
        return None

    def update_employee(self, emp_id, name=None, designation=None, email=None, age=None, department=None, salary=None):
        if emp_id not in self.employees:
            print(f"Error: Employee with ID '{emp_id}' not found.")
            return
        current_employee = self.employees[emp_id]
        try:
            name = ValidationHelper.validate_name(name or current_employee.name)
            email = ValidationHelper.validate_email(email or current_employee.email)
            age = ValidationHelper.validate_numeric_input(age or current_employee.age, allow_empty=True)
            salary = ValidationHelper.validate_numeric_input(salary or current_employee.salary, allow_empty=True)
        except ValueError as e:
            print(f"Error: {e}")
            return
        updated_employee = Employee(
            emp_id=emp_id,
            name=name,
            designation=designation or current_employee.designation,
            email=email,
            age=age if age is not None else current_employee.age,
            department=department if department is not None else current_employee.department,
            salary=salary if salary is not None else current_employee.salary,
        )
        self.employees[emp_id] = updated_employee
        self.file_manager.save_data(self.employees)
        print(f"Employee with ID {emp_id} has been updated.")

    def delete_employee(self, emp_id):
        if emp_id not in self.employees:
            print(f"Error: Employee with ID '{emp_id}' not found.")
            return
        del self.employees[emp_id]  
        self.file_manager.save_data(self.employees)  
        print(f"Employee with ID {emp_id} has been deleted.")

    def view_all_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        print(f'Total Number of Employees: {len(self.employees)}')
        for emp_id, employee in self.employees.items():
            print(f"ID: {employee.emp_id}, Name: {employee.name}")

    def search_employee(self, search_term):
        search_term = search_term.lower() 
        results = [
            emp for emp in self.employees.values()
            if search_term in emp.name.lower() or search_term in emp.designation.lower()
        ]
        return results
