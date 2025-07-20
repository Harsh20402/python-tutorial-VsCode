# Define a class to store employee information
class Get_EMP_Info:
  
  # Default class attributes
  name = "Unknow"
  designation = "Software Engineer"
  salary = 360000
  
  # Static method that doesn't depend on class or instance data
  @staticmethod
  def msg():
    print("Loading....")
  
  # Constructor method to initialize instance with custom or default values
  def __init__(self, param1=None, param2=None, param3=None):
    # Call the static method to simulate some loading behavior
    Get_EMP_Info.msg()
    
    # If a value is provided, use it; otherwise, fall back to the default class attribute
    self.name = param1 if param1 else Get_EMP_Info.name
    self.designation = param2 if param2 else Get_EMP_Info.designation
    self.salary = param3 if param3 else Get_EMP_Info.salary
    
    # Print the initialized employee information
    print(f"Hey! {self.name}, your designation is {self.designation} and your annual CTC is {self.salary}.")

# Create an object with no valid input, so defaults will be used
Harsh = Get_EMP_Info("", "", None)

# Create an object with all custom values
Amit = Get_EMP_Info("Amit Kumar", "Data Engineer", 1200000)
