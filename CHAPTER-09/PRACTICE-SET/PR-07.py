# Write a program to find out the line number where python is present from ques 6. 

def read_file():
    with open("log.txt", "r") as file_read:
        content = file_read.readlines()
        return content

def check_line(word, lines):
    print("\nLines containing the word:")
    found = False
    for lineno, line in enumerate(lines, start=1):
        if word.lower() in line.lower():
            print(f"Line {lineno}: {line.strip()}")
            found = True
    if not found:
        print("The word was not found in any line.")

# Read file content line by line
file_lines = read_file()

# Get user input
user_input = input("Enter the word to search: ").strip()

# Check which line contains the word
check_line(user_input, file_lines)
