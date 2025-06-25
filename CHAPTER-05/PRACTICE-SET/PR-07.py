# Can you change the values inside a list which is contained in set s?
#  s = {8, 7, 12, "Harsh", [1, 2]}

# ❌ No, you cannot include a list inside a set in Python — because lists are mutable and unhashable, which makes them invalid as set elements.

s = {8, 7, 12, "Harsh", [1, 2]}  # ❌ This will raise an error

# Output: TypeError: unhashable type: 'list'

s = {8, 7, 12, "Harsh", (1, 2)}  # ✅ This works
print(s)

# Output: {8, 7, 12, 'Harsh', (1, 2)}