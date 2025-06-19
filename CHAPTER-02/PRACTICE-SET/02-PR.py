# Write a python program to find remainder when a number is divided by Z.

# Taking the first number as input and converting it to an integer
_num1 = int(input("Enter Number one: "))

# Taking the second number as input (the divisor) and converting it to an integer
_num2 = int(input("Enter Number two (divisor): "))

# Calculating the remainder using the modulus operator
_remainder = _num1 % _num2

# Displaying the remainder using an f-string
print(f"The remainder when {_num1} is divided by {_num2} is {_remainder}")