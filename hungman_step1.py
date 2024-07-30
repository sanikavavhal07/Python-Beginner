import random
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
name_list = ["sanika", "siddhi", "saksham"]
choosen_word = random.choice(name_list)
#print(choosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess the alphabet : ")
guess = guess.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in choosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")