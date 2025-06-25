# Write a python program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

# Hindi to English Dictionary
hindi_to_english = {
  "Paani" : "Water",
  "Roti" : "Bread",
  "Ghar" : "Home",
  "Dost" : "Friend",
  "Pyaar" : "Love",
  "Kitab" : "Book",
  "Kursi" : "Chair",
  "Kutta" : "Dog",
  "Billi" : "Cat",
  "Aadmi" : "Man"
}

# Welcome message
print("Welcome to the Hindi to English Dictionary!")
print(f"Available Hindi words: {', '.join(hindi_to_english.keys())}")

# Get user input
word = input("Enter a Hindi word to get its English meaning: ").strip().capitalize()

# Lookup and result using f-strings
if word in hindi_to_english:
    print(f"The English translation of '{word}' is: {hindi_to_english.get(word)}")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")