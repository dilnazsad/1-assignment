import math
x = 2
y = 2
z = 1
A = (4 * math.fabs(x) - math.pow(x * y * z, 2)) / (x + math.exp(y * x) - 2 * y * z)
print("Answer is: " + format(A))
