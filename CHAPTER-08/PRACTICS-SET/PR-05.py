# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3


# Function to print the inverted triangle pattern
def print_pattern(n):
    for i in range(n, 0, -1):  # Start from n and go down to 1
        print('*' * i)

# Take user input
lines = int(input("Enter number of lines: ").strip())

# Call the function to print pattern
print_pattern(lines)
