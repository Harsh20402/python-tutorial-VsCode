# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.  l = ["Harsh", "Soham", "Sachin", "Rahul", "sumit"] 
# List of names
l = ["Harsh", "Soham", "Sachin", "Rahul", "sumit"]

# Loop through each name in the list
for name in l:
  # Check if the name starts with 'S' or 's'
  if name.startswith("S") or name.startswith("s"):
    # Print a greeting with the name capitalized
    print(f"Hello {name.capitalize()}")
