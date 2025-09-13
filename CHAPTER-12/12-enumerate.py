# A list of numbers
lst = [12, 23, 34, 45, 56, 67, 78, 89, 90]

# (OLD WAY) – Manually counting index
# index = 0
# for i in lst:
#     index += 1
#     print(f"The item number at {index} is {i}.")

# (BETTER WAY) – Use enumerate() to get index and item together
for index, item in enumerate(lst):
    # index → automatically generated index (starts from 0 by default)
    # item  → the actual value from the list
    print(f"The item number at index {index} is {item}.")
