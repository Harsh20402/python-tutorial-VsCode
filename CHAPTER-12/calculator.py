def pnt_msg():
    # A simple function that prints a welcome message.
    print("Welcome Message.")

# This block only runs if THIS file (calculator.py) 
# is executed directly (not when imported).
if __name__ == "__main__":
    print("We are directly running this code.")
    
    # Call the function
    pnt_msg()
