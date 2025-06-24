# A **dictionary** in Python is an unordered collection of key-value pairs.
# Each key must be unique, and is used to access its corresponding value.
# Dictionaries are defined using curly braces {} with key: value pairs.

# Creating a dictionary to store student names and their marks
_studentMarks = {
    "Harsh": 89,
    "Amit": 99,
    "Sumit": 65,
    "Rohit": 76
}

# Printing the entire dictionary and its type
print(f"Dictionary: {_studentMarks}, and type is {type(_studentMarks)}")

# Accessing and printing the marks of each student using their names as keys
print(_studentMarks["Harsh"])   # Output: 89
print(_studentMarks["Amit"])    # Output: 99
print(_studentMarks["Sumit"])   # Output: 65
print(_studentMarks["Rohit"])   # Output: 76