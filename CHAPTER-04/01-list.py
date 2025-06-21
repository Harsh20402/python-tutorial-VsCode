# Python lists are containers used to store a collection of items.
# These items can be of any data type: strings, integers, floats, booleans, etc.

_variableOne = ["Apple", "Medicine", 22, 32.23, True, False, "Harsh"]  # A list with mixed data types

# Print the whole list
print(_variableOne)

# Access and print the first element of the list using indexing
print(_variableOne[0])  # Output: Apple

# Modify the first element of the list (Lists are mutable, unlike strings)
_variableOne[0] = "Orange"

# Print the modified list
print(_variableOne)

# Print the updated first element
print(_variableOne[0])  # Output: Orange

# A list can be indexed just like a string to access specific elements
print(f"Index number: 0 -> {_variableOne[0]}")  # Orange
print(f"Index number: 1 -> {_variableOne[1]}")  # Medicine
print(f"Index number: 2 -> {_variableOne[2]}")  # 22
print(f"Index number: 3 -> {_variableOne[3]}")  # 32.23
print(f"Index number: 4 -> {_variableOne[4]}")  # True
print(f"Index number: 5 -> {_variableOne[5]}")  # False
print(f"Index number: 6 -> {_variableOne[6]}")  # Harsh

# List Slicing allows extracting a portion of the list
print("\nList Slicing: ")
print(_variableOne[1 : 5])  # Output: ['Medicine', 22, 32.23, True]
# This prints elements from index 1 to 4 (5 is excluded)