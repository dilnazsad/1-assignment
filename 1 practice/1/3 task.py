import math

a = int(input('enter the numbe:\n'))
print(round(math.floor(a) / 100 + (a % 1) * 100, 2))
