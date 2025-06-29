# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# Predefined spam phrases
p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

# Taking user comment as input
message = input("Enter your comment: ")

# Optional: Convert message to lowercase to make the check case-insensitive
message = message.lower()

# Checking if the message contains any spam phrase
if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This comment is a spam.")
else:
    print("This comment is not a spam.")
