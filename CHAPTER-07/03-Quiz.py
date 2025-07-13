# Write a program to print 1 to 50 using a while loop.

# Initialize the starting value
itemStart = 1

# Define the ending value
itemEnd = 50

# Start a while loop that continues as long as itemStart is less than or equal to itemEnd
while(itemStart <= itemEnd):
  # Print the current item number using an f-string
  print(f"Item no. {itemStart}")
  
  # Increment itemStart by 1 for the next loop iteration
  itemStart += 1
