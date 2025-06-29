# Write a program to find the greatest of four numbers entered by the user.

# Taking four numbers as input from the user
_num1 = int(input("Enter 1st number: "))
_num2 = int(input("Enter 2nd number: "))
_num3 = int(input("Enter 3rd number: "))
_num4 = int(input("Enter 4th number: "))

# Checking if _num1 is greater than or equal to all other numbers
if (_num1 >= _num2 and _num1 >= _num3 and _num1 >= _num4):
    print(f"The greatest number is {_num1}")

# Checking if _num2 is the greatest
elif (_num2 >= _num1 and _num2 >= _num3 and _num2 >= _num4):
    print(f"The greatest number is {_num2}")

# Checking if _num3 is the greatest
elif (_num3 >= _num1 and _num3 >= _num2 and _num3 >= _num4):
    print(f"The greatest number is {_num3}")

# If none of the above, then _num4 must be the greatest
else:
    print(f"The greatest number is {_num4}")