sequence = [6, 85, 4, 5, 12, 0]

sum, n = 0, 0
while sequence[n] != 0:
    sum += sequence[n]
    n += 1
print('the sum of numbers in array', sum)
print('number of elemets is', n + 1)