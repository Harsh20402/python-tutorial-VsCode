# Create an emoty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

# Create an empty dictionary
fav_languages = {}

# Take input from 4 friends
name = input("Enter the name of 1st friend: ").strip().capitalize()
lang = input(f"Enter {name}'s favourite language: ")

fav_languages.update({name : lang})

name = input("Enter the name of 2nd friend: ").strip().capitalize()
lang = input(f"Enter {name}'s favourite language: ")

fav_languages.update({name : lang})

name = input("Enter the name of 3rd friend: ").strip().capitalize()
lang = input(f"Enter {name}'s favourite language: ")

fav_languages.update({name : lang})

name = input("Enter the name of 4th friend: ").strip().capitalize()
lang = input(f"Enter {name}'s favourite language: ")

fav_languages.update({name : lang})

# Display the dictionary
print(f"\nFavorite languages dictionary:\n{fav_languages}")