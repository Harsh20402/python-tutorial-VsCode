# Demonstrating the use of type() function to check variable data types

a = 22
print(type(a))  # <class 'int'> — a is an integer

a = 22.22
print(type(a))  # <class 'float'> — a is a floating-point number

a = "Harsh"
print(type(a))  # <class 'str'> — a is a string

a = True
print(type(a))  # <class 'bool'> — a is a boolean value (True)

a = False
print(type(a))  # <class 'bool'> — a is a boolean value (False)

a = None
print(type(a))  # <class 'NoneType'> — a is a NoneType (represents null or no value)

# Type conversion from string to float
b = "32.12"
print(float(b), type(float(b)))  # 32.12 <class 'float'> — string converted to float
