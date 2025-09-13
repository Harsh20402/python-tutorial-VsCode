#  Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

def table(param1: int):
    """
    Function to generate the multiplication table of a given number.
    :param param1: The number for which the table will be generated
    :return: A list containing the multiplication results from 1 to 10
    """
    no = param1
    # Create a list of multiples using list comprehension
    newLst = [no * i for i in range(1, 11)]
    return newLst   # Return the list


def main():
    """
    Main function to take input from the user, print the table, 
    and store it in a file named 'Tables.txt'.
    """
    # Take number input from the user
    userNumber: int = int(input("Enter a number: "))

    # Generate multiplication table
    result = table(userNumber)

    # Print table in formatted way
    print(f"\nMultiplication table of {userNumber}:")
    for i, val in enumerate(result, start=1):
        print(f"{userNumber} x {i} = {val}")

    # Store table in a file
    with open("Tables.txt", "a") as f:  # 'a' mode appends to file if it exists
        f.write(f"\nMultiplication table of {userNumber}:\n")
        for i, val in enumerate(result, start=1):
            f.write(f"{userNumber} x {i} = {val}\n")
        f.write("\n")  # extra newline for separation

    print("\n✅ Table successfully saved to 'Tables.txt'")


if __name__ == "__main__":
    main()
