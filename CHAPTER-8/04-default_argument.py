# This function greets the user with a message
# name and msg have default values:
# - If no name is given, "Unknown" will be used
# - If no message is given, "Thank You." will be used
def greet(name = "Unknown", msg = "Thank You."):
  # Print a greeting with the name
  print(f"Hey! {name}, Good Morning.")

  # Print the message
  print(f"{msg}")

# Call the function without any arguments
# So it uses the default values for both parameters
greet()

# Call the function with both arguments
# Now it uses "Harsh" as name and "Thanks" as msg
greet("Harsh", "Thanks")
