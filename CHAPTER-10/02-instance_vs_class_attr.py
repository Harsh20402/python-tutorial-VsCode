# Define a class named 'BasicEmployee'
class BasicEmployee:
  # These are class attributes (shared by all instances unless overridden)
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
Amit.location = "Kolkata"   # Object attribute (unique to Amit)

# Override the class attribute 'name' with an object-specific value
Amit.name = "Amit Saha"     # Now 'name' becomes an object attribute for Amit

# Print details for Amit
print(f'''
Employee Name: {Amit.name}           # Uses the object attribute (overrides class attribute)
Employee Location: {Amit.location}   # Object attribute
Employee Occupation: {Amit.occupation} # Still uses class attribute
Employee Salary: {Amit.salary}         # Still uses class attribute
''')

# 🔍 Summary:
# - 'name', 'occupation', and 'salary' are class attributes.
# - 'location' is defined only for 'Amit', so it's an object attribute.
# - Once you assign Amit.name = "Amit Saha", 'name' becomes an object attribute for Amit.
# - Harsh still uses the class-level 'name', 'occupation', and 'salary'.