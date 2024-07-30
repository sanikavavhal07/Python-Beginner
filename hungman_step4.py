import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["button", "coffee", "eleven", "animal", "august"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 10

display = ["_" for _ in range(word_length)]

while not end_of_game:
    clear_screen()
    print(f"{' '.join(display)}")
    print(stages[lives])
    
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            clear_screen()
            print(f"The word was: {chosen_word}")
            print("You lose.")
            print(stages[lives])

    if "_" not in display:
        end_of_game = True
        clear_screen()
        print(f"{' '.join(display)}")
        print("You win.")
        print(stages[lives])

    if not end_of_game:
        clear_screen()
        print(f"{' '.join(display)}")
        print(stages[lives])
