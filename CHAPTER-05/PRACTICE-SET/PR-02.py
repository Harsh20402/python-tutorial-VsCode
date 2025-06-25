# Write a python program to input eight numbers from the user and display all the unique numbers (onece).

# Create an empty set to store unique numbers
userNumber = set()

# Take 8 inputs from the user, one by one
userInput = int(input("Enter 1st number: "))
userNumber.add(userInput)

userInput = int(input("Enter 2nd number: "))
userNumber.add(userInput)

userInput = int(input("Enter 3rd number: "))
userNumber.add(userInput)

userInput = int(input("Enter 4th number: "))
userNumber.add(userInput)

userInput = int(input("Enter 5th number: "))
userNumber.add(userInput)

userInput = int(input("Enter 6th number: "))
userNumber.add(userInput)

userInput = int(input("Enter 7th number: "))
userNumber.add(userInput)

userInput = int(input("Enter 8th number: "))
userNumber.add(userInput)

# Print unique numbers
print(f"Unique numbers are: {userNumber}")