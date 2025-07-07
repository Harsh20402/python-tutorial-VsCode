# Write a program to mine a log file and find out whether it contains ‘python’. 

# Function to read the log file and return its content
def read_file():
  with open("log.txt", "r") as file_read:
    content = file_read.read()
    return content

# Function to check if the word exists in the file content
def check_word(param1, file_content):
  print("Processing......")
  # Compare using lowercase for case-insensitive search
  if param1.lower() in file_content.lower():
    print(f"Yes, the word '{param1}' is present in the content.")
  else:
    print(f"No, the word '{param1}' is not present in the content.")

# Read file once and store it
file_data = read_file()

# Display the file content
print(f"{file_data} \nFind any word from the above content.")

# Get word input from the user
user_input = input("Enter the word: ").strip()

# Call the check function
check_word(user_input, file_data)
