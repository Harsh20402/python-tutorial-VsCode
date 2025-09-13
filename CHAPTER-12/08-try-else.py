try:
    # 'try' block: The code inside this block may cause an exception (error).
    # Asking user to input a number.
    _num: int = int(input("Hey! Enter a number: "))  
    
    # If input is valid (a number), it will be printed.
    print(_num)  

except Exception as e:
    # 'except' block: If any exception occurs in the try block,
    # this block will handle it.
    # 'e' contains the error message (like "invalid literal for int()...").
    print(e)  

else:
    # 'else' block: This part runs only if NO exception occurs in 'try'.
    print("Right now, I'm in the else part.")


# Output:
# Hey! Enter a number: 25
# 25
# Right now, I'm in the else part.