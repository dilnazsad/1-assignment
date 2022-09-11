import math
print("Choose your figure:")
print("1: Circle")
print("2: Rectangle ")
print("3: Triangle ")
figure = int(input(""))
if figure == 1:
    radius = float(input("Enter the radius of the Circle: "))
    area = math.pi * pow(radius, 2)
    print("The area is :" + format(area))
if figure == 2:
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))
    area = width * length
    print("The area is :" + format(area))
if figure == 3:
    a, b, c = map(float, input("Enter the 3 sides of triangle:").split())
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area is :" + format(area))
