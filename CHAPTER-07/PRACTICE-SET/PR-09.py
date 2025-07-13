# Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 

# Take input from the user for the size of the square
n = int(input("Enter the number: "))

# Loop through each row from 1 to n
for i in range(1, n + 1):
    # If it's the first or last row, print all stars
    if i == 1 or i == n:
        print("*" * n, end="")  # Print n stars in a row
    else:
        # Print first star, then spaces, then last star
        print("*", end="")               # First star
        print(" " * (n - 2), end="")     # Middle spaces
        print("*", end="")               # Last star
    print("")  # Move to the next line
