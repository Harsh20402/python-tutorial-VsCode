# Write a list comprehension to print a list which contains the multiplication table of a user entered number. 

def table(param1: int):
    """
    Function to generate the multiplication table of a given number.
    :param param1: The number for which the table will be generated
    :return: A list containing the multiplication results from 1 to 10
    """
    no = param1
    # Create a list of multiples using list comprehension
    # Example: if no = 5 → [5, 10, 15, ..., 50]
    newLst = [no * i for i in range(1, 11)]
    return newLst   # Return the generated list


def main():
    """
    Main function to take input from the user and print the multiplication table.
    """
    # Take number input from the user
    userNumber: int = int(input("Enter a number: "))

    # Print a header message
    print(f"Multiplication table of {userNumber}:")

    # Call the table() function and print the result (list of multiples)
    print(table(userNumber))


# Ensure the program runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
