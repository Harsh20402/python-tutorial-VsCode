# -------------------------------
# Python Set Basics with Comments
# -------------------------------

# A **set** in Python is an unordered collection of unique elements.
# It automatically removes duplicates and does not allow indexing.

# Creating a set with various data types and some duplicates
_set = {1, 2, 3, 34.34, "Harsh", True, False, None, 1, 2, 3, 4}

# True is treated as 1 and False as 0 in Python
# Duplicate values like 1, 2, 3 are automatically removed

print(f"Set: {_set}, and type is {type(_set)}")
# Output may vary in order, but duplicates will be removed.
# Example: Set: {False, 1, 2, 3, 34.34, None, 4, 'Harsh'}, and type is <class 'set'>


# Creating an empty set using curly braces
_emptSet = {}

# In Python, using {} creates an empty dictionary, not a set
print(f"Type is: {type(_emptSet)}")  # Output: <class 'dict'>


# To correctly create an empty set, use the set() constructor
_newEmpSet = set()

print(f"Type is: {type(_newEmpSet)}")  # Output: <class 'set'>
