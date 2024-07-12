height = int(input("Please Enter your Height in cm: "))
if height >= 120:
    age=int(input("You can ride the Rollercoaster.\nPlease Enter your Age : "))
    if age <= 12:
        print("Ticket cost for clildren : 200/-")
        bill=200
    elif age > 12 & age <= 18:
        print("Ticket cost for teenager : 300/-")
        bill=300
    else:
        print("Ticket cost for adults : 500/-")
        bill=500
    pic=input(("Do you want to capture your Rollercoaster memory? press Y or N : "))
    if pic == "Y":
        bill = bill+50
        print("Your Total amount is : " +str(bill)+"/-")
    else:
        print("Your Total amount is : " +str(bill)+"/-")
    print("Hope you Enjoy your ride!")
else: 
    print("oops! You need to grow taller before you can ride ")