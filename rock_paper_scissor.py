import random
print("Welcome to the Rock, Paper and Scissors game!\n")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]
user_choice = int(input("Please enter 0 for Rock, 1 for Paper and 2 for Scissors : "))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice, you lose!")
else:
    print("Your choice: \n" + image[user_choice])
    
computer_choice = random.randint(0, 2)
print("Computer's choice: \n" + image[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")