# Write a program to fill in a letter template given below with name and date.

# Taking user input for name and date
_name = input("Enter your name: ")
_date = input("Enter the date (DD/MM/YYYY): ")

# Template string with placeholders
letter_template = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

# Replace placeholders with actual values
letter_filled = letter_template.replace("<|NAME|>", _name)
letter_filled = letter_filled.replace("<|DATE|>", _date)

# Display the final letter
print("\nGenerated Letter:\n")
print(letter_filled)