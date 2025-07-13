# Write a program to make a copy of a text file “this. txt” 

# Initialize an empty string to store the content of the file
content = ""

# Open the original file 'this.txt' in read mode
with open("this.txt", "r") as file_content:
    # Read the entire content of the file and store it in the variable
    content = file_content.read()

# Open (or create) a new file 'this-copy.txt' in write mode
with open("this-copy.txt", "w") as file_content:
    # Write the copied content into the new file
    file_content.write(content)

# Program finished – content successfully copied
