# Base class (Level 1)
class Person:
    def __init__(self):
        # Initialize base attributes
        self.name = "John Doe"
        self.age = 30

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Intermediate class (Level 2) inherits from Person
class Employee(Person):
    def __init__(self):
        # Explicitly call the constructor of Person
        Person.__init__(self)
        # Initialize Employee-specific attributes
        self.company = "TCS"
        self.salary = 50000

    def show_employee(self):
        print(f"Works at: {self.company}, Salary: ₹{self.salary}")

# Derived class (Level 3) inherits from Employee
class Programmer(Employee):
    def __init__(self):
        # Explicitly call the constructor of Employee
        Employee.__init__(self)
        # Initialize Programmer-specific attributes
        self.language = "Python"

    def show_programmer(self):
        print(f"Programming Language: {self.language}")

# Create an instance of the Programmer class
dev = Programmer()

# Call methods from all levels of the inheritance hierarchy
dev.show_details()      # From Person
dev.show_employee()     # From Employee
dev.show_programmer()   # From Programmer
