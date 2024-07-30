import random

name_list = ["sanika", "siddhi", "saksham"]
chosen_word = random.choice(name_list)
print(chosen_word)

display = ["_" for _ in chosen_word]  # Initialize display with underscores
print(display)

guess = input("Guess the alphabet: ").lower()

# Update the display list in place
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)
