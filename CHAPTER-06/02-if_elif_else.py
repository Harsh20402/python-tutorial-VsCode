# Taking age input from the user and converting it to an integer
_age = int(input("Enter Your Age: "))

# Checking if age is 18 or more
if (_age >= 18):
    print("You are above the age for the consent.\nGood for you.")

# Checking if the age is less than 0 (invalid negative input)
elif (_age < 0):
    print("You are entering an invalid negative age.")

# Checking if the age is exactly 0 (not a valid age)
elif (_age == 0):
    print("You are entering 0, which is not a valid age.")

# If none of the above, the user must be below 18 but greater than 0
else:
    print("You are below the age for the consent.")
