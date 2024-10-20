# Hangman Project

This project implements the classic game, hangman, where the computer thinks of a word and the user tries to guess it. The user has 5 lives to guess the word until the game is over. 

###  Installation Instructions:
User requires python3 to run the game and to import __random__ module. 

### Usage:
To run the game in python, run: 
python milestone_5.py

### List of files:
- milestone_2.py > file creates variables for the game i.e. list of fruits for random function to choose from. Allows user to guess a letter through input function with if statement to check it is a valid input. 
- milestone_3.py > files defines functions to ask for users input and check guess is valid and in the randomly chosen word. 
- milestone_4.py > creates a Hangman class to group functions together. Provides print statements for whether or not the guessed letter is in the word. 
- milestone_5.py > puts all functions together and allows game to be played. 

### Functions defined throughout the project:
- Within class Hangman:
    - check_guess > converts the user input to lowercase, indexes and characters in the word are identified and if user guess is in the random word, the word_guessed variable updates with the correct letter in correct position. If letter guess is incorrect, user loses a life and is shown print statement.   
    - ask_for_input > asks user to guess a letter and checks it is a valid guess i.e. unique, single alphabetical character. 
- Other functions:
    - play_game > allows playing of the game tracking number of lives and how many letters in the word remain. 


