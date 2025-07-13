# Open the file named 'test_file.txt' in read mode ('r')
file_name = open("test_file.txt", "r")

# Read all the lines of the file into a list, where each line is one list element
file_data = file_name.readlines()

# Print the list of lines read from the file
print(file_data)

# Close the file to release system resources
file_name.close()


# Output: ['Hi,\n', '  This is a test file.\n', '\n', 'Thank You.']