# Define two dictionaries
dict1 = {'a': 1, 'b': 2, 'd': 4}
dict2 = {'b': 1, 'c': 3, 'd': 5}

# Merge dict1 and dict2 using the union (|) operator
dict_merge = dict1 | dict2

# Print the merged dictionary
print(dict_merge)
# Output: {'a': 1, 'b': 1, 'd': 5, 'c': 3}