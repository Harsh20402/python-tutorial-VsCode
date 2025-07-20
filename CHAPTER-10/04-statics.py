# Define a class named 'Employee'
class Employee:
  # Class attributes (shared by all instances)
  attr_1 = "value 1"
  attr_2 = "value 2"
  
  # Define a static method using the @staticmethod decorator
  @staticmethod
  def msg():
    # This method does not take 'self' or 'cls' as a parameter
    print("This one is the static method.")

# Create an instance of the Employee class
Test = Employee()

# Call the static method using the instance
Test.msg()   # Output: This one is the static method.
