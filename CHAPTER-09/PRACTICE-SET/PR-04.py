# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

# Donkeys (also known as asses) are intelligent, social, and resilient members of the horse family, characterized by their long ears, strong build, and cautious nature, which often leads to their undeserved reputation for stubbornness. They are known for their exceptional memory, ability to form strong social bonds, and unique communication methods including braying that can be heard from miles away.

# Define the word to be censored
word = "Donkey"

# Function to write censored content back into the file
def write_in_file(param1):
  # Open the file in write mode to overwrite its content
  with open("donkey.txt", "w") as file_overwrite:
    
    # Check if the word "donkey" (in lowercase) exists in the input content
    if(word.lower() in param1):
      # Replace all occurrences of "donkey" with "#####"
      new_content = param1.replace(word.lower(), "#####")
      
      # Capitalize the first letter of the updated content
      file_overwrite.write(new_content.capitalize())
      
      # Print confirmation message
      print("Replace.")
    else:
      # If the word isn't present, write the original content back
      file_overwrite.write(param1)
      
      # Print message indicating no match found
      print("Not Present.")

# Function to read the original file content and pass it to the write function
def open_file():
  # Open the file in read mode
  with open("donkey.txt", "r") as file_open:
    # Read the content and convert it to lowercase
    content = file_open.read().lower()
    
    # Call the function to perform the replacement and update the file
    write_in_file(content)

# Run the main function to start the process
open_file()
