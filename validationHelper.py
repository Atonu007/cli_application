import re

class ValidationHelper:

    @staticmethod
    def validate_name(name):
        if any(char.isdigit() for char in name):
            raise ValueError("Name cannot contain numbers.")
        return name

    @staticmethod
    def validate_email(email):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format.")
        return email

    @staticmethod
    def validate_numeric_input(input_value, allow_empty=False):
        if allow_empty and (input_value is None or input_value == ""):
            return None  
        if isinstance(input_value, (int, float)):
            return float(input_value)
        input_str = str(input_value).strip()
        try:
            return float(input_str)
        except ValueError:
            raise ValueError(f"{input_str} must be a valid number.")

    @staticmethod
    def validate_non_empty_input(prompt, is_numeric=False):
        user_input = input(prompt).strip()
        if not user_input:
            raise ValueError("Input cannot be empty.")
        if is_numeric and not user_input.isdigit():
            raise ValueError("Input must be a numeric value.")
        return user_input
