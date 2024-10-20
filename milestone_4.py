import random 

class Hangman:
    def __init__ (self, num_lives=None, word_list=["strawberry", "pineapple", "watermelon", "orange", "raspberry"]):
        self.word_list = word_list 
        self.num_lives = 5
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
            
        else:
            self.num_lives -=1
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 and guess.isalpha() == False:
               print("Oops! Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")  
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


test = Hangman()
test_call = test.ask_for_input()
print(test_call)
