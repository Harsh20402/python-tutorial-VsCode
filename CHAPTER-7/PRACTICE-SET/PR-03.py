# Write a program to print multiplication table of a given number using while loop. 

# Take user input, remove extra spaces, and convert it to an integer
userInput = int(input("Enter a number: ").strip())

# Initialize counter variable i to 1
i = 1

# Start a while loop to print multiplication table from 1 to 10
while(i <= 10):
  # Print the current multiplication result
  print(f"{userInput} X {i} = {i * userInput}")
  
  # Increment i by 1
  i += 1
