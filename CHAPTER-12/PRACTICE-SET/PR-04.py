# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

def main():
    """
    Program to divide two numbers.
    If denominator is zero, handle the ZeroDivisionError and display 'infinite'.
    """
    # Take input from the user
    no01: int = int(input("Enter a number (numerator a): "))
    no02: int = int(input("Enter another number (denominator b): "))

    try:
        # Try to divide a by b
        result = no01 / no02
    except ZeroDivisionError:
        # Handle division by zero
        print("Result: infinite (division by zero is not allowed)")
    else:
        # If no exception, print the result
        print(f"Result: {no01} divided by {no02} is {result}")


if __name__ == "__main__":
    main()
