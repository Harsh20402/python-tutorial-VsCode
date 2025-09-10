# ====================================================
# 1. Raising a Built-in Exception
# ====================================================
print("1. Raising a Built-in Exception")

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You tried to divide by zero!")  # raise built-in exception
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("Caught exception:", e)

# Output:
# Caught exception: You tried to divide by zero!


# ====================================================
# 2. Raising ValueError with Custom Message
# ====================================================
print("\n2. Raising ValueError with Custom Message")

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")   # raise ValueError manually
    print(f"Age is set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print("Caught exception:", e)

# Output:
# Caught exception: Age cannot be negative


# ====================================================
# 3. Raising Multiple Types of Exceptions
# ====================================================
print("\n3. Raising Multiple Types of Exceptions")

def process_number(num):
    if not isinstance(num, int):
        raise TypeError("Only integers are allowed")   # raise TypeError
    if num < 0:
        raise ValueError("Number must be positive")    # raise ValueError
    return num * 2

try:
    print(process_number("abc"))
except (TypeError, ValueError) as e:
    print("Caught exception:", e)

# Output:
# Caught exception: Only integers are allowed


# ====================================================
# 4. Creating and Raising a Custom Exception
# ====================================================
print("\n4. Creating and Raising a Custom Exception")

# Custom exception class (inherits from Exception)
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("You don’t have enough balance!")  # raise custom exception
    return balance - amount

try:
    new_balance = withdraw(500, 1000)
except InsufficientFundsError as e:
    print("Caught exception:", e)

# Output:
# Caught exception: You don’t have enough balance!
