# This is a function definition named func1.
# A function is a block of code that we can run when we call it.
def func1():
  # This line prints a welcome message to the user
  print("Hello, Harsh")

# Now we are calling (running) the func1 function.
func1()


# Another function defined here, named endMessage
# This will be used to display a thank-you message at the end
def endMessage():
  print("Thanks.....")


# This function will calculate the average of three numbers
def avg():
  # Asking the user to enter the first number
  # input() takes input as string, so we convert it to int (whole number)
  num1 = int(input("Enter 1st number: ").strip())

  # Asking the user to enter the second number
  num2 = int(input("Enter 2nd number: ").strip())

  # Asking the user to enter the third number
  num3 = int(input("ENter 3rd number: ").strip())

  # Now we calculate the average by adding the three numbers and dividing by 3
  avg = (num1 + num2 + num3) / 3

  # Showing the result using f-string (easy way to add variables inside text)
  print(f"The total average of {num1}, {num2} and {num3} is {avg}.")

  # Call the endMessage() function to show the thank-you message
  endMessage()

# Now we are calling the avg() function to run all the steps above
avg()
