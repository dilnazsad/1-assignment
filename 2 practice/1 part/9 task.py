import math
x = 0.8
y = 0.1
z = 4
A = math.pow((1 - x + 1 / math.atan(x - 7 * y)) / (4 * x * z) - math.pow(math.log1p(y), 2), 1 / 5)
print("Answer is: " + format(A))
