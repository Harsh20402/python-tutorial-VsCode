# -----------------------------------------------------
# Example of map(), filter(), and reduce() in Python
# -----------------------------------------------------

# Import reduce from functools
from functools import reduce

# Sample list
numbers = [1, 2, 3, 4, 5, 6]


# ---------------------------
# 1. map() → Apply a function to each element
# ---------------------------

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print("map() - Doubled numbers:", doubled)
# Output: [2, 4, 6, 8, 10, 12]


# ---------------------------
# 2. filter() → Select elements based on a condition
# ---------------------------

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("filter() - Even numbers:", evens)
# Output: [2, 4, 6]


# ---------------------------
# 3. reduce() → Reduce elements to a single value
# ---------------------------

# Find the sum of all numbers
total_sum = reduce(lambda x, y: x + y, numbers)
print("reduce() - Sum of numbers:", total_sum)
# Output: 21

# Find the maximum number
max_num = reduce(lambda a, b: a if a > b else b, numbers)
print("reduce() - Maximum number:", max_num)
# Output: 6
