# This function performs multiplication of two numbers
# param1 and param2 are called "parameters"
# They are like placeholders that will receive values when the function is called
def multi(param1, param2):
  # Multiply the two values and store the result
  result = param1 * param2

  # Just to show something is happening
  print("Processing....")

  # Return the result back to wherever the function was called
  return result

# Ask the user to enter the first number, and convert the input from string to integer
num1 = int(input("Enter 1st number: "))

# Ask the user to enter the second number, and convert the input from string to integer
num2 = int(input("Enter 2nd number: "))

# Call the multi() function with num1 and num2 as "arguments"
# Arguments are actual values we pass into a function when calling it
# The returned value (multiplication result) is shown in the print statement
print(f"Multiplication of {num1} and {num2} is {multi(num1, num2)}.")
