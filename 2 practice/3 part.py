import math
a = float(input('Value of a: '))
b = float(input('Value of b: '))
c = float(input('Value of c: '))
d = (b ** 2) - (4 * a * c)
if d > 0:
    print("The solutions are:")
    print((-b + math.sqrt(d)) / (2 * a))
    print((-b - math.sqrt(d)) / (2 * a))
elif d == 0:
    print("The solution is:")
    print(-b / (2 * a))
else:
    print("No roots")
