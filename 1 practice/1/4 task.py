import math

a = float(input('enter a value of a:\n'))
y = ((a ** 2) / 3) + (((a ** 2) + 4) / 6) + (math.sqrt((a ** 2) + 4) / 4) + (math.sqrt(((a ** 2) + 4) ** 3) / 4)
print('Y = ', format(y))