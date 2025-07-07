# Open the file named 'test_file.txt' in read mode ('r')
file_name = open("test_file.txt", "r")

# Read the entire contents of the file into the variable 'read'
read = file_name.read()

# Print the content that was read from the file
print(read)

# Close the file to free up system resources
file_name.close()