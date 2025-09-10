# -----------------------------------
# 1. ValueError
# Occurs when a function gets an argument of the right type but invalid value.
# -----------------------------------
print("1. ValueError")
try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# OUTPUT: 1. ValueError
# ValueError: invalid literal for int() with base 10: 'abc'

# -----------------------------------
# 2. TypeError
# Raised when an operation is applied to an incompatible type.
# -----------------------------------
print("\n2. TypeError")
try:
    result = "5" + 2
except TypeError as e:
    print(f"TypeError: {e}")

# OUTPUT: 2. TypeError
# TypeError: can only concatenate str (not "int") to str

# -----------------------------------
# 3. NameError
# Happens when you try to use a variable that is not defined.
# -----------------------------------
print("\n3. NameError")
try:
    print(x)
except NameError as e:
    print(f"NameError: {e}")

# OUTPUT: 3. NameError
# NameError: name 'x' is not defined

# -----------------------------------
# 4. IndexError
# Raised when accessing an index that is out of range in a list/tuple.
# -----------------------------------
print("\n4. IndexError")
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"IndexError: {e}")

# OUTPUT: 4. IndexError
# IndexError: list index out of range

# -----------------------------------
# 5. KeyError
# Occurs when you try to access a non-existent key in a dictionary.
# -----------------------------------
print("\n5. KeyError")
try:
    d = {"a": 1, "b": 2}
    print(d["c"])
except KeyError as e:
    print(f"KeyError: {e}")
    
# OUTPUT: 5. KeyError
# KeyError: 'c'

# -----------------------------------
# 6. ZeroDivisionError
# Raised when dividing a number by zero.
# -----------------------------------
print("\n6. ZeroDivisionError")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# OUTPUT: 6. ZeroDivisionError
# ZeroDivisionError: division by zero

# -----------------------------------
# 7. FileNotFoundError
# Occurs when trying to open a file that doesn’t exist.
# -----------------------------------
print("\n7. FileNotFoundError")
try:
    f = open("nofile.txt", "r")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
    
# OUTPUT: 7. FileNotFoundError
# FileNotFoundError: [Errno 2] No such file or directory: 'nofile.txt'

# -----------------------------------
# 8. AttributeError
# Happens when an object doesn’t have the attribute/method you’re trying to use.
# -----------------------------------
print("\n8. AttributeError")
try:
    x = 10
    x.append(5)   # int has no append method
except AttributeError as e:
    print(f"AttributeError: {e}")
    
# OUTPUT: 8. AttributeError
# AttributeError: 'int' object has no attribute 'append'


# -----------------------------------
# 9. ImportError / ModuleNotFoundError
# Raised when you try to import a module that doesn’t exist.
# -----------------------------------
print("\n9. ImportError / ModuleNotFoundError")
try:
    import not_a_module
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")

# OUTPUT: 9. ImportError / ModuleNotFoundError
# ModuleNotFoundError: No module named 'not_a_module'

# -----------------------------------
# 10. Handling Multiple Exceptions
# -----------------------------------
print("\n10. Handling Multiple Exceptions")

# Separate handling
try:
    num = int("abc")
    result = 10 / 0
except ValueError:
    print("ValueError: Invalid number format.")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

# OUTPUT: ValueError: Invalid number format.

# Handling multiple in one line
try:
    num = int("abc")
except (ValueError, TypeError) as e:
    print(f"Caught exception: {e}")

# OUTPUT: Caught exception: invalid literal for int() with base 10: 'abc'