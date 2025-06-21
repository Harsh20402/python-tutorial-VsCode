# Arithmetic Operators
a = 8
b = 4 

print("Arithmetic Operators")
print(a + b)  # Addition: 8 + 4 = 12
print(a - b)  # Subtraction: 8 - 4 = 4
print(a * b)  # Multiplication: 8 * 4 = 32
print(a / b)  # Division (float): 8 / 4 = 2.0
print(a // b)  # Floor Division (int): 8 // 4 = 2

# Assignment Operators
c = 4 - 2      # Subtract and assign: c = 2
d = 6
d += 3         # Increment d by 3: d = 6 + 3 = 9
d -= 3         # Decrement d by 3: d = 9 - 3 = 6

print("\nAssignment Operators")
print(c)       # Output: 2
print(d)       # Output: 6

# Comparison Operators
print("\nComparison Operators")

e = 5 < 4
print(e)       # Output: False (5 is not less than 4)

e = 5 > 4
print(e)       # Output: True (5 is not less than 4)

e = 5 <= 5
print(e)       # Output: True (5 is less than or equal to 5)

e = 5 >= 5
print(e)       # Output: True (5 is less than or equal to 5)

e = 5 != 7
print(e)       # Output: True (5 is not equal to 7)

e = 5 == 7
print(e)       # Output: False (5 is not equal to 7)

# Logical Operators
print("\nLogical Operators")

# Truth table for 'or'
print("True or False is", True or False)     # True
print("True or True is", True or True)       # True
print("False or True is", False or True)     # True
print("False or False is", False or False)   # False

# Truth table for 'and'
print("True and False is", True and False)   # False
print("True and True is", True and True)     # True
print("False and True is", False and True)   # False
print("False and False is", False and False) # False

# 'not' operator
print("not True is", not(True))              # False
print("not False is", not(False))            # True
