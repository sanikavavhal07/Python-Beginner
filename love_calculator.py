print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name = name1.lower()
lower_case_name2 = name2.lower()

true_count = (lower_case_name.count("t") + lower_case_name.count("r") + lower_case_name.count("u") + lower_case_name.count("e") + lower_case_name2.count("t") + lower_case_name2.count("r") + lower_case_name2.count("u") + lower_case_name2.count("e"))

love_count = (lower_case_name2.count("l") + lower_case_name2.count("o") + lower_case_name2.count("v") + lower_case_name2.count("e") + lower_case_name.count("l") + lower_case_name.count("o") + lower_case_name.count("v") + lower_case_name.count("e"))

love_score = int(str(true_count) + str(love_count))
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is: {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <+ 50):
    print(f"Your love score is: {love_score}, you are alright together.")
else:
    print(f"Your score is : {love_score}")
