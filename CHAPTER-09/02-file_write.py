# Define the sentence that you want to write into the file
sentence = "This is a line for the write file."

# Open the file named 'write-file.txt' in write mode ('w')
# If the file does not exist, it will be created.
# If it does exist, its contents will be overwritten.
file = open("write-file.txt", "w")

# Write the sentence into the file
file.write(sentence)

# Close the file to ensure data is saved and resources are released
file.close()