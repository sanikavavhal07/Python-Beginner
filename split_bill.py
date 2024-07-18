# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# length = len(names)
# person_to_pay = random.randint(0 , length - 1)
# name_of_person = print(names[person_to_pay])
person_to_pay = random.choice(names)
name_of_person = print(person_to_pay + "will pay for the meal today!")

