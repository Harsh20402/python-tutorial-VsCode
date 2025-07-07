# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

# Open the file 'poems.txt' in read mode
with open("poems.txt", "r") as Poem:
    # Read the file content and convert it to lowercase to handle case-insensitive search
    content = Poem.read().lower()
    
    # Check if the word 'twinkle' is present in the content
    if "twinkle" in content:
        print("The word 'twinkle' is present in the content.")
    else:
        print("The word 'twinkle' isn't present in the content.")
