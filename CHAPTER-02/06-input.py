# Prompt the user to type anything and store the input in _userInput
# Note: By default, input() returns a value of type 'str' (string)
_userInput = input("Type Any Thing: ")  # _userInput is of type str

# Display what the user typed using an f-string
print(f"Your entered: {_userInput}")

# Prompt the user to enter the first number
# Convert the input string to an integer using int()
# After conversion, 'a' is of type int
a = int(input("Enter a number: "))  # input is str, converted to int

# Prompt the user to enter the second number
# Convert the input string to an integer using int()
# After conversion, 'b' is also of type int
b = int(input("Enter another number: "))  # input is str, converted to int

# Display both entered numbers and their sum using an f-string
# The sum of two integers (a + b) is also an int
print(f"The numbers are {a} and {b}, and the sum is {a + b}")
