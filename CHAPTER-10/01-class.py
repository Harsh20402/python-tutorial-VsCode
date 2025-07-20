# Define a class named 'BasicEmployee'
class BasicEmployee:
  # These are class attributes (shared by all instances or objects unless overridden)
  name = "Harsh Shaw"               # Class attribute: default name
  occupation = "Software Developer" # Class attribute: default occupation
  salary = 228000                    # Class attribute: default salary

# Create an instance of BasicEmployee and assign it to 'Harsh'
Harsh = BasicEmployee()

# Print details for Harsh using class attributes
print(f'''
Employee Name: {Harsh.name}
Employee Occupation: {Harsh.occupation}
Employee Salary: {Harsh.salary}
''')

# Create another instance of BasicEmployee and assign it to 'Amit'
Amit = BasicEmployee()

# Assign an object-specific attribute
Amit.location = "Kolkata"   # Object or Instance attribute (unique to Amit)

# Print details for Amit
print(f'''
Employee Name: {Amit.name}           # Still uses class attribute
Employee Location: {Amit.location}   # Object attribute
Employee Occupation: {Amit.occupation} # Still uses class attribute
Employee Salary: {Amit.salary}         # Still uses class attribute
''')


