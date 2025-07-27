class Employee:
    def __init__(self, name, salary):
        self._name = name          # _name is a "protected" variable
        self._salary = salary      # _salary is a "protected" variable

    @property
    def name(self):
        # This makes name behave like an attribute, but with getter control
        return self._name

    @property
    def salary(self):
        # This is a getter for salary
        return self._salary

    @salary.setter
    def salary(self, value):
        # This is a setter to control salary updates
        if value < 0:
            print("❌ Salary can't be negative!")
        else:
            self._salary = value

# Create an Employee object
emp = Employee("Harsh", 50000)

# Access name and salary like attributes
print(emp.name)      # ✅ Allowed (getter)
print(emp.salary)    # ✅ Allowed (getter)

# Update salary
emp.salary = 60000   # ✅ Allowed (setter)
print(emp.salary)

emp.salary = -1000   # ❌ Blocked by setter logic
