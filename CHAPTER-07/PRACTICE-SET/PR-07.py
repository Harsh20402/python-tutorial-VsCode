# Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3

# Take input from the user (number of rows)
n = int(input("Enter the number: "))

# Loop through 1 to n (inclusive)
for i in range(1, n+1):
    # Print (n - i) spaces to align the stars to the center
    print(" " * (n - i), end="")

    # Print (2*i - 1) stars to create the pyramid shape
    print("*" * (2 * i - 1), end="")

    # Move to the next line
    print("")
