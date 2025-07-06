# Write a python function to print multiplication table of a given number.

# Function to print multiplication table of a given number
def multiplication_table(param):
    print(f"\nMultiplication Table of: {param}")
    for item in range(1, 11):  # Loop from 1 to 10
        print(f"\t{param} x {item} = {param * item}")  # Print formatted line

# Take user input and convert to integer
user_input = int(input("Enter the number for the multiplication table: ").strip())

# Call the function with the user input
multiplication_table(user_input)
