# Write a program to greet a user with “Good day” using functions. 

# This function greets the user with a "Good Day" message
def GoodDay():
  # Asking the user to enter their name
  # .strip() removes any extra spaces from the beginning or end
  # .capitalize() makes the first letter uppercase (e.g., "harsh" → "Harsh")
  userName = input("Enter Your Name: ").strip().capitalize()

  # Printing the greeting using f-string to include the user's name
  print(f"Hey! {userName}, Good Day.")

# Calling the function to run it
GoodDay()
