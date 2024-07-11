print("Welcome to the Tip Calculator!")
amt = float(input("Enter the total amount of the bill: "))
tip = int(input("What percentage of tip would you like to give? "))
ppl = int(input("How many persons are going to split the bill? "))
amt_with_tip = amt + (amt * tip / 100)
split = amt_with_tip / ppl
print(f"Each person's contribution is: {split:.2f}")
