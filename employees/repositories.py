class InMemoryEmployeeRepository:
    def __init__(self):
        self.employees = [
            {"id": 1, "first_name": "Anna", "last_name": "Andersson", "email": "anna.andersson@example.com"},
            {"id": 2, "first_name": "Erik", "last_name": "Svensson", "email": "erik.svensson@example.com"},
            {"id": 3, "first_name": "Maria", "last_name": "Larsson", "email": "maria.larsson@example.com"},
        ]
        self.next_id = 4

    def get_all_employees(self):
        return self.employees


repository = InMemoryEmployeeRepository()

