def get_number():
    try:
        # 'try' block: Put the code that might cause an error.
        # Asking the user to enter a number.
        num = int(input("Enter a number: "))
        
        # If the input can be converted to integer successfully,
        # then this line will execute.
        print("You entered:", num)

    except ValueError as e:
        # 'except' block: Handles the error if user input is not a valid integer.
        # For example, if user types "abc", int("abc") raises ValueError.
        # 'e' stores the actual error message.
        print("Error:", e)

    finally:
        # 'finally' block: This block ALWAYS runs,
        # whether or not an exception occurred.
        # Typically used for cleanup (closing files, releasing resources, etc.)
        print("Finally block: Cleaning up resources...")

# Function call to run the above logic
get_number()
