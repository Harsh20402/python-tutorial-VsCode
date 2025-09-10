# Using the walrus operator (:=) to assign and check 'n' in a single line.
# The expression (n := len([...])) assigns the length of the list to 'n'
# and then immediately compares it to 10 in the 'if' condition.
if (n := len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) <= 10:
    # If n (length of list) is less than or equal to 10, this block executes.
    print(f"The list is too short ({n} elements, expected <= 10).")
else:
    # If n is greater than 10, this block executes.
    print(f"The list is too long ({n} elements, expected <=10).")


