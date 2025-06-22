# Write a program to store seven fruits in a list entered by the user.

# Initialize an empty list to store the fruits entered by the user
fruitsList = []

# Take 7 fruit names as input from the user, one by one
# Use .strip() to remove any extra spaces and .capitalize() to format the input

# Input 1
userInput = input("Enter The Fruit Name: ").strip().capitalize()
fruitsList.append(userInput)

# Input 2
userInput = input("Enter The Fruit Name: ").strip().capitalize()
fruitsList.append(userInput)

# Input 3
userInput = input("Enter The Fruit Name: ").strip().capitalize()
fruitsList.append(userInput)

# Input 4
userInput = input("Enter The Fruit Name: ").strip().capitalize()
fruitsList.append(userInput)

# Input 5
userInput = input("Enter The Fruit Name: ").strip().capitalize()
fruitsList.append(userInput)

# Input 6
userInput = input("Enter The Fruit Name: ").strip().capitalize()
fruitsList.append(userInput)

# Input 7
userInput = input("Enter The Fruit Name: ").strip().capitalize()
fruitsList.append(userInput)

# Display the final list of fruits entered by the user
print(f"User entered the fruits: {fruitsList}")
