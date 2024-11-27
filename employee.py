class Employee:
    def __init__(self, emp_id, name, designation, email, age=None, department=None, salary=None):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.email = email
        self.age = age
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.designation},{self.email},{self.age},{self.department},{self.salary}"

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "designation": self.designation,
            "email": self.email,
            "age": self.age,
            "department": self.department,
            "salary": self.salary
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            emp_id=data["emp_id"],
            name=data["name"],
            designation=data["designation"],
            email=data["email"],
            age=data.get("age"),
            department=data.get("department"),
            salary=data.get("salary")
        )
