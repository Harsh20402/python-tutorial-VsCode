# Write a program to wipe out the content of a file using python. 

# Function to wipe out (clear) the content of a given file
def wipe_file(param):
    # Open the file in write mode ("w") which automatically clears existing content
    with open(param, "w") as file:
        file.write("")  # Write an empty string to erase file content

    # Notify the user that the file has been wiped successfully
    print(f"Wipe out successfully completed for this file: {param}")

# Ask the user to enter the name of the file to be wiped
user_input = input("Enter the file name: ").strip()

# Call the function with the provided file name
wipe_file(user_input)
