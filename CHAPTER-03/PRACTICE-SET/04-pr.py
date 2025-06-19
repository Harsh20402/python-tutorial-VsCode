# Replace the double space from problem with single space

# Take user input
_userInput = input("Enter a string: ")

# Replace all double spaces with single space
_updatedString = _userInput.replace("  ", " ")

# Print the updated string
print("\nString after replacing double spaces:")
print(f'"{_updatedString}"')