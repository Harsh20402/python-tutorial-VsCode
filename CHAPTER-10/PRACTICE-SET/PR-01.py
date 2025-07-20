#  Create a class “Programmer” for storing information of few programmers working at Microsoft.

# Define a class 'Programmer' to store information about programmers at Microsoft
class Programmer:
  # Class attributes shared by all instances unless overridden
  company = "Microsoft"
  employe_name = "Unkonwn"  # Default name if none is provided
  employe_salary = "120000"  # Default salary
  employee_address = "PAN-INDIA"  # Default location

  # Constructor to initialize each programmer's specific data
  def __init__(self, param1, param2, param3):
    # Use provided name or fallback to default
    self.emp_name = param1 if param1 else self.employe_name

    # Use provided salary or fallback to default
    self.emp_salary = param2 if param2 else self.employe_salary

    # Company is always Microsoft, taken from class attribute
    self.emp_company = self.company

    # Use provided location or fallback to default
    self.emp_location = param3 if param3 else self.employee_address

    # Print the employee's information in a formatted way
    print(f"""
    Company Name: {self.emp_company}
    Employee Name: {self.emp_name}
    Employee Location: {self.emp_location}
    Employee Salary: {self.emp_salary}
          """)

# Creating first instance with custom name and location, but default salary
Harsh = Programmer("Harsh Shaw", None, "Kolkata")

# Creating second instance with all default values
Amit = Programmer(None, None, None)