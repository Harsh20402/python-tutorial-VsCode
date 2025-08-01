# Write a program to print multiplication table of n using for loops in reversed order.

# Take a number as input from the user and convert it to integer
userInput = int(input("Enter any number: ").strip())

# Use a for loop to print multiplication table from 1 to 10
for x in range(10, 0, -1):
  # Print each line in the format: userInput X x = result
  print(f"{userInput} X {x} = {x * userInput}")

# The else block runs after the for loop completes successfully
else:
  print("Thank You.")