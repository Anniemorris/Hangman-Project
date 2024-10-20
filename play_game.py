

import random 

class Hangman:
    """
    A class representing the Hangman game.

    This class represents an automated version of the game Hangman where players can input a letter to make a guess, uncovering the letter if correct.

    Attributes:
        word_list (list): A list of words from which the game will select a random word which requires 'random' module.
        num_lives (int): The number of lives a player has per game, set to 5 and will decrease with incorrect guesses.
        word (str): The current word to be guessed from word_list.
        word_guessed (list): List of characters of the word representing letters correctly guessed with '_' for letter to be guessed.
        num_letters (int): Number of unique letters in the word which decreases with correct guesses.
        list_of_guesses (list): List of letters that have been guessed by the player. 

    Methods:
        check_guess(guess):
            Checks if the guessed letter is in the word. If correct, the letter is revealed in the word. If incorrect, the player loses a life.
        ask_for_input():
            Asks user to input a letter which is then validated. 

    """
    def __init__ (self, word_list=["strawberry", "pineapple", "watermelon", "orange", "raspberry"], num_lives=5):
        """
        See help(Hangman) for an accurate signature. 
        """
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(self.word_list) 
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word. If correct, the letter is revealed in the word. If incorrect, the player loses a life.

        Args:
            guess (str): The inputted letter from the user. 
        
        Returns:
            None

        Prints:
            If guess is correct, updated state of the word is printed with letter(s) revealed.
            If incorrect, prints number of lives remaining. 
        
        """
        self.guess = guess.lower()
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")   
        
            for i, char in enumerate(self.word):
                if char == self.guess:
                     self.word_guessed[i] = self.guess

            print("Update: ", self.word_guessed)
            self.num_letters -=1
            
        else:
            self.num_lives -=1
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Prompts player to guess a letter and validates the input. 

        The method ensures the guess is a single, unique alphabetical character. Loop continues until input is valid. 

        Returns:
            None. 

        """
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
               print("Oops! Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")  
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """
    Function to play the Hangman game using the Hangman class. 

    This function runs a loop until either the word is guessed and the game is won or the player runs out of lives.

    Args:
        word_list (list): List of words from which the game randomly selects one to be guessed. 

    Returns:
        None.

    Prints:
        A messaging indicating if the game has been won or lost. 

    """
    game = Hangman(word_list)     
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0: 
            game.ask_for_input()
        else:
            print("Congratulations! You won the game.")
            break
            


test_words = ["strawberry", "pineapple", "watermelon", "orange", "raspberry"]
play_game(test_words)


