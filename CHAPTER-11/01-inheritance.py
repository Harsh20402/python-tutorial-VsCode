# Define a base class called 'Employee'
class Employee:
    # Class attribute shared by all Employee instances
    company = "ITC"
    
    # Method to display employee details (name and salary)
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}.")

# Define a derived class 'Programmer' that inherits from 'Employee'
class Programmer(Employee):
    # Overrides the 'company' attribute for Programmer instances
    company = "Numone Technologies"
    
    # Method to display programmer's language skill
    def showlanguage(self):
        print(f"The name is {self.name} and he is a good with {self.language} language.")

# Create an instance of Employee
a = Employee()

# Create an instance of Programmer
b = Programmer()

# Print the 'company' attribute for both instances
# a uses Employee's company -> "ITC"
# b uses Programmer's company -> "Numone Technologies"
print(a.company, b.company)

# NOTE:
# At this point, neither a.name, a.salary, b.name, b.salary, nor b.language are set,
# so calling a.show() or b.showlanguage() would raise an AttributeError unless you set those attributes first.
