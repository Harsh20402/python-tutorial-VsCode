# Assign the string "Harsh" to the variable _name
_name = "Harsh"

# Print the string from index 0 to the end
print(_name[0 : ])  # Output: Harsh

# Print the characters from index -4 to -1 (excluding -1)
# -4 = 'a', -3 = 'r', -2 = 's' => so the result is 'ars'
print(_name[-4 : -1])  # Output: ars

# Print characters from index 1 to 3 (index 4 is excluded)
# index 1 = 'a', index 2 = 'r', index 3 = 's'
print(_name[1 : 4])  # Output: ars


# Assign an integer
_no = 1234567890

# Convert the number to a string for slicing
_no_str = str(_no)

# Print characters from index 1 to 6 with step 2: indices 1, 3, 5
print(_no_str[1 : 7 : 2])  # Output: 35  (indexes 1='2', 3='4', 5='6')

# Print every 3rd character starting from index 0
print(_no_str[0 : : 3])    # Output: 1470 (indexes 0,3,6,9)