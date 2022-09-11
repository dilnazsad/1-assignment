import math

x = int(input("Value of x: \n"))
y = int(input("Value of y: \n"))

H = math.sqrt(math.cos(2 * y) + math.sin(4 * y) + math.sqrt(math.exp(x) + math.exp(-x))) / math.pow((math.exp(x) + math.exp(-x)), 3) * math.pow((math.sin(4 * y) + math.cos(2 * y) - 2), 2)

print('H = ', H)

