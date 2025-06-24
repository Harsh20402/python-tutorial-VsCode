# -------------------------------------
# Python Set: Important Methods & Output
# -------------------------------------

# Creating a set with mixed data types and duplicates
_set = {1, 2, 3, 34.34, "Harsh", True, False, None, 1, 2, 3, 4}

# Note:
# - Sets store only unique values.
# - True == 1 and False == 0
# - Duplicates will be removed automatically
# - Sets are unordered

print(f"Initial Set: {_set}")
# Output: Set may look like {False, 1, 2, 3, 34.34, None, 4, 'Harsh'}

# 1. add()
print("\n1. add()")
_set.add("Python")  # Adds a single element
print(_set)
# Output: {False, 1, 2, 3, 34.34, None, 4, 'Harsh', 'Python'}

# 2. update()
print("\n2. update()")
_set.update([10, 20], {30, 40})  # Adds multiple elements || The update() method in Python sets is used to add multiple elements to a set. It can take one or more iterable arguments (like a list, set, tuple, or string) and adds each item individually to the set.
print(_set)
# Output: {False, 1, 2, 3, 34.34, None, 4, 40, 10, 'Harsh', 'Python', 20, 30}

# 3. remove()
print("\n3. remove()")
_set.remove("Python")  # Removes element (throws error if not found)
print(_set)
# Output: {False, 1, 2, 3, 34.34, None, 4, 40, 10, 'Harsh', 20, 30}

# 4. discard()
print("\n4. discard()")
_set.discard("NotExists")  # No error if item not present
print(_set)
# Output: {False, 1, 2, 3, 34.34, None, 4, 40, 10, 'Harsh', 20, 30}

# 5. pop()
print("\n5. pop()")
popped_item = _set.pop()  # Removes and returns a random element
print(f"Popped Item: {popped_item}")
print(_set)
# Output: {1, 2, 3, 34.34, None, 4, 40, 10, 'Harsh', 20, 30}

# 6. clear()
print("\n6. clear()")
_tempSet = _set.copy()  # Copy to preserve original set
_tempSet.clear()        # Removes all elements
print(_tempSet)
# Output: set()

# Using two new sets for remaining methods
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 7. union()
print("\n7. union()")
print(a.union(b))
# Output: {1, 2, 3, 4, 5, 6}

# 8. intersection()
print("\n8. intersection()")
print(a.intersection(b))
# Output: {3, 4}

# 9. difference()
print("\n9. difference()")
print(a.difference(b))
print(b.difference(a))
# Output: {1, 2}
# Output: {5, 6}

# 10. isdisjoint()
print("\n10. isdisjoint()")
print(a.isdisjoint({10, 11}))
# Output: True

# 11. issubset()
print("\n11. issubset()")
print({1, 2}.issubset(a))
# Output: True

# 12. issuperset()
print("\n12. issuperset()")
print(a.issuperset({1, 2}))
# Output: True
