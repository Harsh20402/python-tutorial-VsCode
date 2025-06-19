# Write a program to detect double space in a string.

# Take user input
_userInput = input("Enter a string: ")

# Print the original input for reference
print(f'You entered: "{_userInput}"')

# Find the index of the first occurrence of double space
double_space_index = _userInput.find("  ")

# Print the result
if double_space_index != -1:
    print(f"Double space found at index: {double_space_index}")
else:
    print("No double space found in the string.")