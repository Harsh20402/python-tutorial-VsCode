# Write a program to print the content of a list using while loop.

# Define a list with different types of elements
_list = [22, 32.23, "Harsh", True, False, None]

# Initialize index variable to start from the first element (index 0)
i = 0

# Loop until 'i' is less than the length of the list
while(i < len(_list)):
  # Print the element at the current index 'i'
  print(_list[i])
  
  # Increment the index to move to the next element
  i += 1
