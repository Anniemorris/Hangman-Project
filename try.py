import random 
word_list = ["strawberry", "pineapple", "watermelon", "orange", "raspberry"]
print(word_list)

word = random.choice(word_list)
print(word)
word_guessed = ["_"] * len(word)
print(word_guessed)

num_letters = set(word)
print(len(set(word)))