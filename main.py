from user_interface import CLI
from file_manager import FileManager
from employeeManager import EmployeeManager

def main():
    file_manager = FileManager("employees.txt") 
    employee_manager = EmployeeManager(file_manager) 
    cli = CLI(employee_manager)
    cli.run()

if __name__ == "__main__":
    main()
