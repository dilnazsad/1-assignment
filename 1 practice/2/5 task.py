number = "458"
counter = 0

print('*** You have only 3 tries to guess the number ***')

while True:
    numb = input("guess the numb: ").lower()
    counter = counter + 1
    if numb == number:
        break
    if numb != number and counter > 2:
        break
