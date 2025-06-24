# -------------------------------
# Python Dictionary Methods Demo
# -------------------------------

# A dictionary stores data in key-value pairs. 
# Keys must be unique and are used to access values.

# Creating a dictionary to store student names and their marks
_studentMarks = {
    "Harsh": 89,
    "Amit": 99,
    "Sumit": 65,
    "Rohit": 76
}

# 1. dict.keys()
# Returns a view of all the keys in the dictionary.
print("\n1. dict.keys()")
print(_studentMarks.keys())  # Output: dict_keys(['Harsh', 'Amit', 'Sumit', 'Rohit'])

# 2. dict.values()
# Returns a view of all the values in the dictionary.
print("\n2. dict.values()")
print(_studentMarks.values())  # Output: dict_values([89, 99, 65, 76])

# 3. dict.items()
# Returns a view of all key-value pairs as tuples.
print("\n3. dict.items()")
print(_studentMarks.items())  
# Output: dict_items([('Harsh', 89), ('Amit', 99), ('Sumit', 65), ('Rohit', 76)])

# 4. dict.get(key)
# Returns the value for the specified key. Returns None if the key doesn't exist.
print("\n4. dict.get(key)")
print(_studentMarks.get("Harsh"))    # Output: 89
print(_studentMarks.get("Unknown"))  # Output: None

# Safe vs Unsafe key access
print(_studentMarks["Harsh"])        # Safe: key exists
# print(_studentMarks["Unknown"])    # Unsafe: would raise KeyError if uncommented

# 5. dict.update(other_dict)
# Adds/updates key-value pairs from another dictionary.
print("\n5. dict.update(other_dict)")
_studentMarks.update({"Ravi": 88})
print(_studentMarks)  
# Output includes 'Ravi': 88

# 6. dict.pop(key)
# Removes the key-value pair for the given key.
print("\n6. dict.pop(key)")
_studentMarks.pop("Ravi")  # Removes 'Ravi'
print(_studentMarks)

# 7. dict.clear()
# Clears all items from the dictionary.
print("\n7. dict.clear()")
_studentMarks.clear()
print(_studentMarks)  # Output: {}
