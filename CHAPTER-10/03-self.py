# Define a class named 'Employee'
class Employee:
  # Class attributes (shared among all instances unless overridden)
  name = "Unknown Name"
  designation = "Python Developer"
  salary = 350000

  # Instance method to print employee details
  def get_details(self):
    # 'self' refers to the instance calling this method
    print(f"Hey! {self.name}, your designation is {self.designation} and your annual CTC is {self.salary}.")

# Create an instance/object named 'Harsh' of the Employee class
Harsh = Employee()

# Override the class attribute 'name' for this particular object
Harsh.name = "Harsh Shaw"

# Harsh.get_details() === Employee.get_details(Harsh)
# Call the get_details method using the object
Harsh.get_details()

# The line above is internally equivalent to this:
Employee.get_details(Harsh)
# This shows how Python automatically passes the object ('Harsh') as the first argument to 'self'

# ✅ Explanation of `self`:
# - `self` is not a keyword, but a naming convention (you could name it anything, but using 'self' is best practice).
# - It refers to the **current instance of the class**.
# - When you do `Harsh.get_details()`, Python translates it internally to `Employee.get_details(Harsh)`,
#   where `Harsh` is passed as the value of `self`.