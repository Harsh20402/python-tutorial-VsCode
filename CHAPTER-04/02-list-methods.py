# A list with mixed data types: strings, numbers, booleans
_variableOne = ["Apple", "Medicine", 22, 32.23, True, False, "Harsh"]
print("Original List:", _variableOne)
# Output: ['Apple', 'Medicine', 22, 32.23, True, False, 'Harsh']

# 1. append()
# Syntax: list.append(item)
print("\n1. append() Method:")
_variableOne.append("NewItems")  # Adds 'NewItems' at the end
print(f"After append: {_variableOne}")
# Output: ['Apple', 'Medicine', 22, 32.23, True, False, 'Harsh', 'NewItems']

# 2. insert()
# Syntax: list.insert(index, item)
print("\n2. insert(index, item) Method:")
_variableOne.insert(2, "InsertedItem")  # Inserts at index 2
print("After insert at index 2:", _variableOne)
# Output: ['Apple', 'Medicine', 'InsertedItem', 22, 32.23, True, False, 'Harsh', 'NewItems']

# 3. remove()
# Syntax: list.remove(item)
print("\n3. remove(item) Method:")
_variableOne.remove("InsertedItem")  # Removes the item by value
print(f"After removing 'InsertedItem': {_variableOne}")
# Output: ['Apple', 'Medicine', 22, 32.23, True, False, 'Harsh', 'NewItems']

# 4. pop()
# Syntax: list.pop()
print("\n4. pop() Method:")
_newPopVariableOne = _variableOne.pop()  # Removes and returns the last item
print(f"After pop: {_variableOne}")
print(f"Popped Item: {_newPopVariableOne}")
# Output: ['Apple', 'Medicine', 22, 32.23, True, False, 'Harsh']
#         Popped Item: NewItems

# 5. index()
# Syntax: list.index(item)
print("\n5. index(item) Method:")
_indexOfHarsh = _variableOne.index("Harsh")  # Gets index of 'Harsh'
print(f"Index of 'Harsh': {_indexOfHarsh}")
# Output: Index of 'Harsh': 6

# 6. count()
# Syntax: list.count(item)
print("\n6. count(item) Method:")
_variableOne.append(22)  # Adding another 22
print("List after appending 22:", _variableOne)
_count22 = _variableOne.count(22)  # Counts how many times 22 appears
print(f"Count of 22: {_count22}")
# Output: Count of 22: 2
_variableOne.pop()  # Remove the extra 22 added above

# 7. reverse()
# Syntax: list.reverse()
print("\n7. reverse() Method:")
_variableOne.reverse()  # Reverses the list in-place
print(f"After reverse: {_variableOne}")
# Output: ['Harsh', False, True, 32.23, 22, 'Medicine', 'Apple']

# 8. sort()
# Syntax: list.sort()
print("\n8. sort() Method:")
numeric_list = [5, 2, 9, 1]
print("Original numeric list:", numeric_list)
numeric_list.sort()  # Sorts in ascending order
print(f"Sorted list: {numeric_list}")
# Output: [1, 2, 5, 9]

# Also demonstrating reverse sort
numeric_list.reverse()
print(f"After reverse sort: {numeric_list}")
# Output: [9, 5, 2, 1]

# 9. copy()
# Syntax: list.copy()
print("\n9. copy() Method:")
copied_list = _variableOne.copy()  # Creates a shallow copy
print("Copied list:", copied_list)
# Output: Same as current _variableOne

# 10. clear()
# Syntax: list.clear()
print("\n10. clear() Method:")
temp_list = _variableOne.copy()  # Copy before clearing
temp_list.clear()  # Removes all elements
print("After clear:", temp_list)
# Output: []
