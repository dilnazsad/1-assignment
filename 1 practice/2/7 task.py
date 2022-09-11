word = input("enter the word:\n")
number = int(input("enter the number:\n"))

for x in word:
    for n in range(0, number):
        print(x, end="")
    print()
