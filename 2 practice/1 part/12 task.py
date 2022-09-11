import math
x = 2
y = 2
z = 1
A = math.sqrt(0.6 * x * y * z) + math.pow(math.pow(y, x), 2) - math.exp(math.pow(2 * math.sin(x) * math.cos(x), 2))
print("Answer is: " + format(A))
