import random 
word_list = ["strawberry", "pineapple", "watermelon", "orange", "raspberry"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please guess a letter: ")
print(guess)

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

