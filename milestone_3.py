import random 
word_list = ["strawberry", "pineapple", "watermelon", "orange", "raspberry"]
# print(word_list)

word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# while loop to check user guesses are valid 
def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Oops! Invalid letter. Please enter a single alphabetical character.")
    check_guess(guess)


ask_for_input()

