# Write a class “Calculator” capable of finding square, cube and square root of a number. 

# Define a Calculator class to compute square, cube, and square root
class Calculator:
  
  # Constructor that accepts a number and calculates values
  def __init__(self, param1):
    self.param1 = param1  # Store the input number
    self.square_no = self.square()  # Call instance method
    self.cube_no = self.cube()      # Call instance method
    self.root_no = self.root()      # Call instance method

    # Display results
    print(f"""
    The square of {self.param1} is {self.square_no}.
    The cube of {self.param1} is {self.cube_no}.
    The square root of {self.param1} is {self.root_no}
    """)

  # Method to calculate square
  def square(self):
    return self.param1 ** 2

  # Method to calculate cube
  def cube(self):
    return self.param1 ** 3

  # Method to calculate square root
  def root(self):
    return round(self.param1 ** 0.5, 2)

# Take user input and create Calculator object
User_input = int(input("Enter the number: "))
Result = Calculator(User_input)