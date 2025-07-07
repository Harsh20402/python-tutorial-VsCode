# Using While Loop

# Open the file named 'test_file.txt' in read mode ('r')
file_name = open("test_file.txt", "r")

# Read the first line from the file
line = file_name.readline()

# Loop through the file until an empty string is returned (end of file)
while(line != ""):
    # Print the current line
    print(line, end="")
    
    # Read the next line
    line = file_name.readline()

# Close the file after reading all lines
file_name.close()



# Using for Loop
# Open the file named 'test_file.txt' in read mode ('r')
file_name = open("test_file.txt", "r")

# Loop through each line in the file directly using a for loop
for line in file_name:
    # Print each line (line already includes a newline character '\n')
    print(line, end="")  # 'end=""' prevents double newlines

# Close the file after reading
file_name.close()
