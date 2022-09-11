import math
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
P = a + b + c
S = (a * b) / 2
print("Perimeter is equal to:" + format(P))
print("Area is equal to:" + format(S))
