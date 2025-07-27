# Create a class ‘Employee’ and add salary and increment properties to it.

# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary.

class Employee:
    def __init__(self, salary):
        # Initialize the base salary
        self._salary = salary
        self._increment = 1.0  # Default increment multiplier

    @property
    def salary(self):
        # Getter for salary
        return self._salary

    @salary.setter
    def salary(self, value):
        # Setter for salary
        if value < 0:
            print("❌ Salary cannot be negative.")
        else:
            self._salary = value

    @property
    def increment(self):
        # Getter for increment
        return self._increment

    @increment.setter
    def increment(self, value):
        # Setter for increment
        if value < 1:
            print("❌ Increment must be >= 1.0")
        else:
            self._increment = value
            
    @property
    def salaryAfterIncrement(self):
        # Calculates the salary after applying the increment
        return int(self._salary * self._increment)
      
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        # Sets the increment value based on the desired updated salary
        if value <= self._salary:
            print("❌ Updated salary must be greater than current salary.")
        else:
            self._increment = value / self._salary
            
            
class Employee:
    def __init__(self, salary):
        # Initialize the base salary
        self._salary = salary
        self._increment = 1.0  # Default increment multiplier

    @property
    def salary(self):
        # Getter for salary
        return self._salary

    @salary.setter
    def salary(self, value):
        # Setter for salary
        if value < 0:
            print("❌ Salary cannot be negative.")
        else:
            self._salary = value

    @property
    def increment(self):
        # Getter for increment
        return self._increment

    @increment.setter
    def increment(self, value):
        # Setter for increment
        if value < 1:
            print("❌ Increment must be >= 1.0")
        else:
            self._increment = value

    @property
    def salaryAfterIncrement(self):
        # Calculates the salary after applying the increment
        return int(self._salary * self._increment)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        # Sets the increment value based on the desired updated salary
        if value <= self._salary:
            print("❌ Updated salary must be greater than current salary.")
        else:
            self._increment = value / self._salary


# Example usage:
emp = Employee(50000)

print(f"Base Salary: ₹{emp.salary}")
print(f"Current Increment: {emp.increment}")
print(f"Salary After Increment: ₹{emp.salaryAfterIncrement}")

# Let's say the employee wants their salary after increment to be ₹60000
emp.salaryAfterIncrement = 60000  # This will auto-update the increment value

print(f"\n📈 New Increment Multiplier: {emp.increment}")
print(f"💰 Updated Salary After Increment: ₹{emp.salaryAfterIncrement}")
