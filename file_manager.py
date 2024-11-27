import json
from employee import Employee

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                return {emp_data['emp_id']: Employee.from_dict(emp_data) for emp_data in data}
        except FileNotFoundError:
            print("File not found. Returning an empty dictionary.")
            return {}
        except json.JSONDecodeError:
            print("File is empty or corrupted. Returning an empty dictionary.")
            return {}

    def save_data(self, employees_dict):
        try:
            with open(self.file_name, 'w') as file:
                json.dump([emp.to_dict() for emp in employees_dict.values()], file, indent=4)
            return "Data saved successfully."
        except Exception as e:
            return f"Error saving data: {e}"
