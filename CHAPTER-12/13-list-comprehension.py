# Original list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- Method 1: Using normal for loop ---
newLst = []                 # Start with an empty list
for item in lst:            # Loop through each element in lst
    newLst.append(item * item)   # Square the item and add to newLst

# Print original and squared list
print(lst)       # Original list remains unchanged
print(newLst)    # New list contains squares


# --- Method 2: Using list comprehension ---
# [expression for item in iterable]
squaredList = [i * i for i in lst]   # Creates a new list of squares in one line

# Print original and squared list
print(lst)          # Original list remains unchanged
print(squaredList)  # New list contains squares
