import math
x = 4
A = math.log1p(math.pow(x - 3, 4)) + math.pow(2, x) * math.pow(math.sin(3 * x), 2)
print("Answer is: " + format(A))
