# Taking age input from user and converting it to integer
a = int(input("Enter your age: "))

# -------- If statement no: 1 --------
# Checking if the age is even using modulus operator (%)
if (a % 2 == 0):
    print(f"{a} is even")
# -------- End of If statement no: 1 --------

# -------- If statement no: 2 --------
# Checking if the age is valid and if the user is above or below the age of consent
if (a >= 18):
    print("You are above the age of consent")
    print("Good for you")

# Checking for invalid negative input
elif (a < 0):
    print("You are entering an invalid negative age")

# If age is less than 18 but not negative
else:
    print("You are below the age of consent")
# -------- End of If statement no: 2 --------

# This line runs regardless of any condition
print("End of Program")
