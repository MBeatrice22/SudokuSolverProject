class Employee:
    def __init__(self, name, salary):
        # Atributele comune pentru toți angajații
        self.name = name
        self.salary = salary

    def get_details(self):
        """Returnează detalii despre angajat."""
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        # Apelăm constructorul clasei de bază pentru a inițializa name și salary
        super().__init__(name, salary)
        # Atributul suplimentar specific managerului
        self.department = department

    def get_details(self):
        """Suprascriem metoda pentru a include departamentul."""
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


# Exemplu de utilizare:
emp = Employee("John", 3000)
mgr = Manager("Alice", 5000, "IT")

print(emp.get_details())  # "Employee: John, Salary: 3000"
print(mgr.get_details())  # "Manager: Alice, Salary: 5000, Department: IT"
