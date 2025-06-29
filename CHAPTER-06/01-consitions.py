# Asking the user to enter their age
_age = int(input("Enter Your Age: "))

# Checking if the age is greater than or equal to 18
if (_age >= 18):
    # If condition is true (age is 18 or more), this line will be executed
    print("You are above the age of consent.")
    print("Good for you.")
else:
    # If condition is false (age is less than 18), this block will run
    print("You are below the age of consent.")

# This line runs regardless of the condition
print("End of the program.")