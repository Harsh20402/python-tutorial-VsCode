# Parent class representing an employee
class Employee:
  def __init__(self):
    # Initialize company and name attributes
    self.company = "ITC"
    self.name = "Default Name"

  def show(self):
    # Display employee name and company
    print(f"The name of the employee is {self.name} and the company is {self.company}.")

# Another parent class representing coding skills
class CoderLanguage:
  def __init__(self):
    # Initialize language attribute
    self.language = "Python"
    
  def print_language(self):
    # Display the programming language
    print(f"Out of all the languages, here is your language: {self.language}.")

# Child class inheriting from both Employee and CoderLanguage
class Programmer(Employee, CoderLanguage):
  def __init__(self):
    # Call constructors of both parent classes to ensure all attributes are initialized
    Employee.__init__(self)
    CoderLanguage.__init__(self)
    
  def showlanguage(self):
    # Display name and programming language from inherited attributes
    print(f"The name is {self.name}, and he is good with {self.language}.")

# Create an instance of Programmer
Harsh = Programmer()

# Call method to show the programmer's language proficiency
Harsh.showlanguage()
