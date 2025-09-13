# Global variables (defined outside any function)
num_01: int = 10
num_02: int = 20


def pnt1():
    # Here, we create a NEW local variable with the same name (num_01).
    # This does NOT affect the global num_01.
    num_01 = 100
    print(num_01)   # Prints the local variable → 100


# Print the global variable num_01 (before function call)
print(num_01)  # Output: 10

# Call the function pnt1()
pnt1()         # Output: 100 (local scope)

# Print the global variable num_01 again
print(num_01)  # Output: 10 (global is unchanged)


def pnt2():
    # Use 'global' keyword to modify the global variable num_02
    global num_02
    num_02 = 200   # This changes the global num_02
    print(num_02)  # Output: 200 (global is updated)


# Print the global variable num_02 (before function call)
print(num_02)  # Output: 20

# Call the function pnt2()
pnt2()         # Output: 200 (global variable updated)

# Print the global variable num_02 again
print(num_02)  # Output: 200 (changed globally)
