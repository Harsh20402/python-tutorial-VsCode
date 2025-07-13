# Open the file 'test_file.txt' using the traditional way
f = open("test_file.txt")

# Read and print the entire content of the file
print(f.read())

# Close the file manually to free resources
f.close()


# The same can be written using a 'with' statement:
with open("test_file.txt", "r") as file:
    # Read and print the entire content of the file
    print(file.read())

# You don't have to explicitly close the file.
# The 'with' block automatically handles closing, even if an error occurs.
