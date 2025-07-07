# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi score whenever the game() function breaks the Hi-score. 

import random

# Function to fetch the current high score from the file
def fetch_high_score():
    with open("Hi-score.txt", "r") as score:
        current_score = score.read()
        
        if current_score != "":
            return int(current_score)  # Convert score to integer if file is not empty
        else:
            return 0  # Return 0 if file is blank

# Function to write a new high score into the file
def write_high_score(param1):
    with open("Hi-score.txt", "w") as NewHighScore:
        NewHighScore.write(str(param1))  # Convert integer score to string before writing

# Function to simulate the game
def game():
    rand_number = random.randint(0, 100)  # Generate a random score between 0 and 100
    
    user_name = input("Enter Your Name: ").strip().title()
    print(f"Hey! {user_name}, we're playing a game.........")
    
    print(f"Your Score is {rand_number}.")
    
    high_score = fetch_high_score()  # Get the current high score
    
    if rand_number >= high_score:
        print("🎉 Congratulations! You broke the high score!")
        write_high_score(rand_number)  # Update the high score if beaten
    else:
        print(f"The current high score is {high_score}. Better luck next time!")

# Run the game
game()