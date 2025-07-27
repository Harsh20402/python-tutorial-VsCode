class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        # Overload the '+' operator to add salaries
        return self.salary + other.salary

    def __gt__(self, other):
        # Overload the '>' operator to compare salaries
        return self.salary > other.salary

    def __str__(self):
        # For a clean print() of the object
        return f"Employee(name={self.name}, salary={self.salary})"

# Create two Employee objects
emp1 = Employee("Harsh", 50000)
emp2 = Employee("Raj", 60000)

# '+' now adds their salaries
print("Total salary:", emp1 + emp2)  # → 110000

# '>' now compares their salaries
if emp1 > emp2:
    print(f"{emp1.name} has a higher salary.")
else:
    print(f"{emp2.name} has a higher salary.")



"""
🧠 Common Operator Overloading Methods in Python:

| Operator | Method        | Meaning               |
| -------- | ------------- | --------------------- |
| `+`      | `__add__`     | Addition              |
| `-`      | `__sub__`     | Subtraction           |
| `*`      | `__mul__`     | Multiplication        |
| `/`      | `__truediv__` | Division              |
| `==`     | `__eq__`      | Equal to              |
| `>`      | `__gt__`      | Greater than          |
| `<`      | `__lt__`      | Less than             |
| `str()`  | `__str__`     | String representation |

"""