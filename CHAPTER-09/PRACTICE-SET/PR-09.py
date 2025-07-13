# Write a program to find out whether a file is identical & matches the content of another file.

# Function to read content from a file
def file_read(filename):
    with open(filename, "r") as file_content:
        return file_content.read()

# Function to check if contents of two files are identical
def compare_files(file_list):
    content_list = []

    for i in range(len(file_list)):
        fileName = file_list[i]
        content = file_read(fileName)
        content_list.append(content)

    if content_list[0] == content_list[1]:
        print("Yes, these files' contents are identical.")
    else:
        print("No, these files' contents are not identical.")

# Collect filenames from user
input_file_list = []

for x in range(1, 3):
    file_name = input(f"Enter the file name {x}: ").strip()
    input_file_list.append(file_name)

# Print file list for reference
print(f"Files to compare: {", ".join(input_file_list)}")

# Call the comparison function
compare_files(input_file_list)
