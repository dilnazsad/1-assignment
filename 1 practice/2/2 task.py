n1 = int(input('First number: '))
operation = str(input('Operation: '))
n2 = int(input('Second number: '))
if n2 == 0 and operation == "/":
    print('Impossible')
elif operation == "+":
    print(n1 + n2)
elif operation == "-":
    print(n1 - n2)
elif operation == "*":
    print(n1 * n2)
elif n2 != 0 and operation == "/":
    print(n1 / n2)
