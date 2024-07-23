# num_1 = int(input("Enter first number : "))
# num_2 = int(input("Enter second number : "))
# add = num_1 + num_2
# sub = num_1 - num_2
# mult = num_1 * num_2
# div = num_1 / num_2
# expo = num_1 ** num_2 
# rem = num_1 % num_2 
# print("Addition of given numbers is : ", add)
# print("Subtraction of given numbers is : ", sub)
# print("Multiplication of given numbers is : ", mult)
# print("Division of given numbers is : ", div)
# print("Exponential of given numbers is : ", expo)
# print("Remainder of given numbers is : ", rem)

print("For area of SQUARE")
side = float(input("Enter the side in cm : "))
print("Area of square is : ", side*side, "sq cm\n")

print("For area of RECTANGLE")
len = float(input("Enter the length in cm : "))
bre = float(input("Enter the breadth in cm : "))
print("Area of rectangle is : ", len*bre, "sq cm\n")

print("For area of TRIANGLE")
height = float(input("Enter the height in cm : "))
base = float(input("Enter the base in cm : "))
print("Area of triangle is : ", 0.5*base*height, "sq cm\n")

print("For area of CIRCLE")
radius = float(input("Enter the radius in cm : "))
print("Area of circle is : ", round(3.14*radius*radius, 2), "sq cm\n")
