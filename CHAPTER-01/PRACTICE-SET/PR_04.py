# Write a python program to print the contents of a dictonary using the os modules.

import os  # Importing the os module to interact with the operating system

# Specify the directory path whose contents you want to list
directory_path = '/'  # Change this to your actual directory path

# Use os.listdir() to get the list of files and folders in the specified directory
contents = os.listdir(directory_path)

# Print the contents of the directory
print(contents)  # This will output a list of file and folder names