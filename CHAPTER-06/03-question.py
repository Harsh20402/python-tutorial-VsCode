# Write a program toprint yes when the age entered by the user is greater than or equal to 18.

# Program to print a message if age is >= 18 and handle other edge cases

# Taking user input and converting it to an integer
_age = int(input("Enter Your Age: "))

# Case 1: Age is negative — invalid input
if (_age < 0):
    print("You are entering an invalid negative age.")

# Case 2: Age is exactly 0 — also invalid
elif (_age == 0):
    print("You are entering 0, which is not a valid age.")

# Case 3: Age is 18 or more — eligible to vote
elif (_age >= 18):
    print("You are eligible to vote.")  # (Fixed wording: “to give the vote” → “to vote”)

# Case 4: Age is positive but less than 18 — not eligible
else:
    print("You are not eligible to vote.")
