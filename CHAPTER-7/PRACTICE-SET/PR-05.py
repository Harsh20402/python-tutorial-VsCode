# Write a program to find the sum of first n natural numbers using while loop. 

# Take input from the user and convert it to an integer
userInput = int(input("Enter a number: ").strip())

# Initialize counter and sum
i = 1
sum = 0

# Loop from 1 to userInput
while (i <= userInput):
  sum += i         # Add current value of i to sum
  i += 1           # Increment i by 1 (not i =+ 1, which is a bug)

# Print the result
print(f"The sum of first {userInput} natural numbers is: {sum}.")
