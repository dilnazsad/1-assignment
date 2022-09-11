import math

x = 0.5
y = 2
A = math.asin(math.pow(x, 3.)) - 6 / (8 * (math.cos(4 * y) - math.sin(4 * x)))
print("Answer is: " + format(A))