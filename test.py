word = "strawberry"
#print(word[2])
num_letters = len(set(word))
print(num_letters)

word_guessed = ["_"] * len(word)
print(word_guessed)

guess = input("Please guess a letter: ")
guess = guess.lower()

if guess in word: 
    guess_index = word.index(guess)

    word_guessed[guess_index] = guess 

print("Current state of word guessed", word_guessed)
num_letters -= 1

#replace = ["_" for char in word]
#print(replace)

