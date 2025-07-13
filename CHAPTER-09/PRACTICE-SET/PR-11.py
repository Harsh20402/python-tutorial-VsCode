# Write a python program to rename a file to “renamed_by_python.txt”

import os

# Ask the user to enter the current file name
old_file_name = input("Enter the file name: ").strip()

# Fixed new file name
new_file_name = "renamed_by_python.txt"

# Rename the file
os.rename(old_file_name, new_file_name)

# Confirm the renaming
print(f"File renamed successfully to {new_file_name}")
