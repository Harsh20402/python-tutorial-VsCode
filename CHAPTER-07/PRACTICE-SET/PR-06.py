# Write a program to calculate the factorial of a given number using for loop

# Take input from the user and convert it to an integer
userInput = int(input("Enter a number: ").strip())

# Initialize product to 1 (because factorial starts with multiplication identity)
product = 1

# Loop from 1 to userInput (inclusive)
for i in range(1, userInput + 1):
  product = product * i   # Multiply each number with the product

# Print the final factorial result
print(f"The factorial of {userInput} is: {product}")
