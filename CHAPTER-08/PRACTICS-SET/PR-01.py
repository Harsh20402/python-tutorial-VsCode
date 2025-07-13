# Write a program using functions to find greatest of three numbers. 

# Function to take input from the user
def userInput():
    # Prompt the user to enter three numbers
    num1 = int(input("Enter first number: ").strip())
    num2 = int(input("Enter second number: ").strip())
    num3 = int(input("Enter third number: ").strip())
    
    # Return all three numbers as a tuple
    return num1, num2, num3

# Function to find the greatest of three numbers
def greatestNumber(param1, param2, param3):
    # Compare each number to find the greatest
    if param1 >= param2 and param1 >= param3:
        return param1
    elif param2 >= param1 and param2 >= param3:
        return param2
    else:
        return param3  # The remaining case where param3 is the greatest

# Call userInput() to get the three numbers from the user
inputNumber = userInput()

# Call greatestNumber() with unpacked tuple values and display result
print(f"The greatest number among {inputNumber[0]}, {inputNumber[1]} and {inputNumber[2]} is {greatestNumber(inputNumber[0], inputNumber[1], inputNumber[2])}.")
