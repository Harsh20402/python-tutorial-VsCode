# Write a program to find whether a given username contains less than 10 characters or not.

# Taking username input from the user
userName = input("Enter Your Name: ")

# Calculating the length of the username
userNameLen = len(userName)

# Checking if the username has 10 or fewer characters
if userNameLen <= 10:
    print("Your username contains 10 or fewer characters.")
else:
    print("Your username contains more than 10 characters.")