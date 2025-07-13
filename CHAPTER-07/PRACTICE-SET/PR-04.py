# Write a program to find whether a given number is prime or not. 

# Take a number as input from the user and convert it to integer
userInput = int(input("Enter a number: ").strip())

# Loop through numbers starting from 2 up to (but not including) the entered number
for i in range(2, userInput):
  # Check if the number is divisible by any number in the range
  if(userInput % i == 0):
    # If divisible, it's not a prime number
    print(f"{userInput} is not a prime number.")
    break  # Exit the loop as we found a factor
else:
  # This else block runs only if the loop is not terminated by 'break'
  print(f"{userInput} is a prime number.")
