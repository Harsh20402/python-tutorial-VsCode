# Write a python function which converts inches to cms.

# Function to convert inches to centimeters
def in_to_cm(param1):
  result = param1 * 2.54
  return f"{result: .2f}"

# Take user input
inch_input = float(input("Enter length in inches: ").strip())

# Call the function and display result
converted = in_to_cm(inch_input)
print(f"{inch_input} inch(es) is equal to {converted} cm.")
