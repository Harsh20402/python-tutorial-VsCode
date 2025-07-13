# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3

# Take input from the user (number of rows)
n = int(input("Enter the number: "))

# Loop through 1 to n (inclusive)
for i in range(1, n+1): 
    # Print i stars (*) on the current line
    print("*" * i, end="")

    # Move to the next line after printing stars
    print("")
