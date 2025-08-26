import pyjokes  # Importing the pyjokes library to fetch programming jokes.

jokes = pyjokes.get_joke()  # Getting a random joke using get_joke()

print("Printing Jokes......")  # Informative message before printing the joke.
print(jokes)  # This prints the random joke fetched from pyjokes.
