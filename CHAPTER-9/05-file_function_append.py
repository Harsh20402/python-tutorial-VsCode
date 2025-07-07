# Define the line to be appended to the file
line = "This is an append line."

# Open the file in append mode ('a')
# If the file doesn't exist, it will be created.
file_name = open("write-file.txt", "a")

# Append the line to the end of the file
file_name.write(line)

# Close the file
file_name.close()
