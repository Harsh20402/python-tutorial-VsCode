# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

# Function to write the complete table content to a file
def table_file(param1, param2):
  with open(f"tables/table-of-{param1}.txt", "w") as content:
    content.write(param2)
  
# Function to generate the content of the multiplication table
def table_genarator(param1):
  content = f"Table of {param1}:\n"
  for item in range(1, 11):
    content += f"{param1} X {item} = {item * param1}\n"
    table_file(param1, content)
  print(f"✅ Table of {param1} created successfully.")

# Function to create all tables from 2 to 20
def numbers():
  # Generate tables from 2 to 20
  for item in range(2, 21):
    table_genarator(item)
    
# Run the program
numbers()