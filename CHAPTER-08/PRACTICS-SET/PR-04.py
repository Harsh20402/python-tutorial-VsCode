# Write a recursive function to calculate the sum of first n natural numbers. 

# Function to take user input
def takeInput():
    userInput = int(input("Enter a number: ").strip())
    return userInput

# Recursive function to calculate the sum of first n natural numbers
def sumOfNatural(param1):
    # Base case for negative input
    if param1 < 0:
        return 0  # Can also raise an error if preferred
    # Base case: sum of first 1 number is 1
    elif param1 == 1:
        return 1
    # Recursive case
    return param1 + sumOfNatural(param1 - 1)

# Taking input from the user
inputResult = takeInput()

# Displaying the result
print(f"The sum of the first {inputResult} natural number(s) is {sumOfNatural(inputResult)}.")
