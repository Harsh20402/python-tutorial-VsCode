class Employee:
  a = 22  # Class variable
  
  @classmethod
  def show(self):  # 'self' here refers to the class, not the instance
    print(f"The class attribute of a is {self.a}.")
    
obj = Employee()
obj.a = 50  # This creates an instance variable 'a' for obj
obj.show()
