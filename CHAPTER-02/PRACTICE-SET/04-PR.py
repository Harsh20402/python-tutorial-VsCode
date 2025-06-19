# Use comparison operator to find out a given variable a is greater than b or not.

# Taking the first number as input
_num1 = int(input("Enter the first number: "))

# Taking the second number as input
_num2 = int(input("Enter the second number: "))

# Comparing whether _num1 is greater than or equal to _num2
_comparison = _num1 >= _num2

# Displaying the result
print(f"Entered numbers are {_num1} and {_num2}. Is {_num1} greater than or equal to {_num2}? {_comparison}")
