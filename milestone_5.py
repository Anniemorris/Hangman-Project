import random 

class Hangman:
    def __init__ (self, word_list=["strawberry", "pineapple", "watermelon", "orange", "raspberry"], num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(self.word_list) 
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")   
        
            for i, char in enumerate(self.word):
                if char == self.guess:
                     self.word_guessed[i] = self.guess

            print("Updated word_guessed: ", self.word_guessed)
            self.num_letters -=1
            
        else:
            self.num_lives -=1
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
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
    game = Hangman(word_list)     
    while True:
        if game.num_lives == 0:
            print("You lost!")
        elif game.num_letters > 0: 
            game.ask_for_input()
        else:
            print("Congratulations! You won the game.")


trial = ["strawberry", "pineapple", "watermelon", "orange", "raspberry"]
play_game(trial)




