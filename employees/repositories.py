class InMemoryEmployeeRepository:
    def __init__(self):
        self.employees = []
        self.next_id = 1

    def get_all_employees(self):
        return self.employees

    def get_employee(self, employee_id):
        for emp in self.employees:
            if emp['id'] == employee_id:
                return emp
        return None

    def email_exists(self, email):
        return any(emp['email'] == email for emp in self.employees)

    def add_employee(self, first_name, last_name, email):
        employee = {
            "id": self.next_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        self.employees.append(employee)
        self.next_id += 1
        return employee

    def delete_employee(self, employee_id):
        for i, emp in enumerate(self.employees):
            if emp['id'] == employee_id:
                self.employees.pop(i)
                return True
        return False

    def reset(self):
        self.employees = []
        self.next_id = 1


repository = InMemoryEmployeeRepository()

