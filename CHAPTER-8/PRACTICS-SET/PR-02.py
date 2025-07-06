# Write a python program using function to convert Celsius to Fahrenheit. 

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(param1):
  fahrenheit = (param1 * 9 / 5) + 32
  return fahrenheit



# Take user input in Celsius
celsius_input = float(input("Enter temperature in Celsius: ").strip())

# Call the function and store the result
converted_temp = celsius_to_fahrenheit(celsius_input)

# Display the result
# print(f"{celsius_input}°C is equal to {converted_temp:.2f}°F.")
print(f"{celsius_input}°C is equal to {round(converted_temp, 2)}°F.")