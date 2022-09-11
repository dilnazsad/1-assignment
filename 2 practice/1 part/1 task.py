import math
a = int(input("Value of a: \n"))
b = int(input("Value of b: \n"))
h = int(input("Value of h: \n"))
S = ((math.sqrt(a) + b) * h) / (2*(a-b) + 4)
print("Answer: S = " + format(S))