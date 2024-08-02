import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans to cover the wall")
paint_calc(height=test_h, width=test_w, cover=coverage)
