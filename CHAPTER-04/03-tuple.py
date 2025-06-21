# Creating a tuple with mixed data types: integers, string, float, booleans
_newTuple = (1, 2, "Harsh", 22.22, True, False)

# Print the full tuple and its type
print(f"New Tuple: {_newTuple}, and the type is {type(_newTuple)}")
# Output: New Tuple: (1, 2, 'Harsh', 22.22, True, False), and the type is <class 'tuple'>

# Demonstrating the difference between a number and a tuple
a = (1)  # This is NOT a tuple, just a number with parentheses
print(type(a))  # Output: <class 'int'>

a = ("Harsh")  # This is NOT a tuple, just a string with parentheses
print(type(a))  # Output: <class 'str'>

_aa = (1,)  # This is a tuple with a single element
print(type(_aa))  # Output: <class 'tuple'>

# Tuple Indexing (similar to lists, but tuples are immutable)
print("\nTuple Indexing:")
print(f"Index number 0 : {_newTuple[0]}")  # Output: 1
print(f"Index number 1 : {_newTuple[1]}")  # Output: 2
print(f"Index number 2 : {_newTuple[2]}")  # Output: Harsh
print(f"Index number 3 : {_newTuple[3]}")  # Output: 22.22
print(f"Index number 4 : {_newTuple[4]}")  # Output: True
print(f"Index number 5 : {_newTuple[5]}")  # Output: False

# Note: Tuples support indexing and slicing like lists,
# but they cannot be changed (immutable)
