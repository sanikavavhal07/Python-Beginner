print("Welcome to Python Pizza Delivery!")
size = input("What size pizza do you want? S, M or L: \n")
if size == "S":
    price = 199
elif size == "M":
    price = 299
else:
    price = 399

add_pepperoni = input("Do you want to add pepperoni? Y or N : ")
if add_pepperoni == "Y":
    price = price + 20

add_cheese = input("Do you want to add extra cheese? Y or N : ")
if add_cheese == "Y":
    price = price + 20

print(f"Your total amount is : {price}/-")
    

