# Write a program to sum a list with 4 numbers.

# Initialize an empty list to store the numbers
numberList = []

# Take 4 numbers as input from the user and convert them to integers
# Use .strip() to remove extra spaces if any

# Input 1
userInput = int(input("Enter the number: ").strip())
numberList.append(userInput)

# Input 2
userInput = int(input("Enter the number: ").strip())
numberList.append(userInput)

# Input 3
userInput = int(input("Enter the number: ").strip())
numberList.append(userInput)

# Input 4
userInput = int(input("Enter the number: ").strip())
numberList.append(userInput)

# Calculate the sum of all numbers in the list
sumOfList = sum(numberList)

# Print the total sum
print(f"The sum of number is : {sumOfList}")
