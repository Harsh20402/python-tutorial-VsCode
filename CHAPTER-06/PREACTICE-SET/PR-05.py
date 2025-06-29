# Write a program which finds out whether a given name is present in a list or not.

# List of predefined names
nameList = ["Harsh", "Amit", "Rohit", "Arun"]

# Take user's name as input and convert the first letter to uppercase
# (to match the format in the list)
name = input("Enter Your Name: ").capitalize()

# Check if the name exists in the list
if name in nameList:
    print("Your name is in the list.")
else:
    print("Your name is not in the list.")
