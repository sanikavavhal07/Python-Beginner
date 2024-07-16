print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Treasure Hunt Game!")
print("Your mission is to find the treasure.")

# Start of the game
choice1 = input("You stand at the edge of a dense forest. Do you choose to enter the forest path or walk along the riverbank? Type 'forest' or 'river' \n").lower()

if choice1 == "forest":
    # First decision point
    choice2 = input("As you venture deeper, you find an old, weathered signpost. One arrow points to a dark cave, and another to a bright clearing. Do you enter the cave or head to the clearing? Type 'cave' or 'clearing' \n").lower()
    
    if choice2 == "clearing":
        # Second decision point
        choice3 = input("In the clearing, you discover an ancient, moss-covered statue. A hidden passage seems to open nearby. Do you examine the statue or enter the passage? Type 'statue' or 'passage' \n").lower()
        
        if choice3 == "passage":
            # Third decision point
            choice4 = input("The passage leads to a tranquil underground lake. A mysterious boat floats gently on the water. Do you row the boat across or swim? Type 'boat' or 'swim' \n").lower()
            
            if choice4 == "boat":
                # Final decision point
                choice5 = input("Reaching the other side, you find three chests: one gold, one silver, and one wooden. Which chest do you open? Type 'gold', 'silver', or 'wooden' \n").lower()
                
                if choice5 == "gold":
                    print("You open the gold chest and find it empty. Game Over.")
                elif choice5 == "silver":
                    print("You open the silver chest and find a trap! Game Over.")
                elif choice5 == "wooden":
                    print("You open the wooden chest and find the treasure! You Win!")
                else:
                    print("You chose a chest that doesn't exist. Game Over.")
            else:
                print("You struggle and drown in the lake. Game Over.")
        else:
            print("The statue comes to life and attacks you. Game Over.")
    else:
        print("You get lost in the darkness of the cave. Game Over.")
else:
    print("You fall into quicksand along the riverbank. Game Over.")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# print("Welcome to the Treasure Hunt Game!")
# print("Your mission is to find the treasure.")

# # Start of the game
# choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' \n").lower()

# if choice1 == "left":
#     # First decision point
#     choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    
#     if choice2 == "wait":
#         # Second decision point
#         choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()
        
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print("You get attacked by an angry trout. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")

