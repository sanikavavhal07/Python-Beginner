years = input("What is your current age? ")
age = int(years)
month = round(age * 12)
week = round(age * 52)
days = round(age * 365)
print(f"You have completed {month} months, {week} weeks and {days} days")


age = input("What is your current age? ")
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
