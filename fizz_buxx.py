# `When the number is divisible by 5, then instead of printing the number it should print "Buzz" And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
for number in range(1, 20):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)