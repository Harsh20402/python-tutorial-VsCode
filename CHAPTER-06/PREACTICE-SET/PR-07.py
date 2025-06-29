# Write a program to find out whether a given post is talking about “Harsh” or not.

# Take the post input from the user and remove any leading/trailing whitespace
userPost = input("Enter The Post: ").strip()

# Convert the post to lowercase to make the search case-insensitive
# Then check if the word "harsh" is in the post
if "harsh" in userPost.lower():
    # If "harsh" is found in the post
    print("This post is talking about Harsh.")
else:
    # If "harsh" is not found in the post
    print("This post is not talking about Harsh.")
