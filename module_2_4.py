# Всё не так уж просто
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] #только простые числа
not_primes = [] #не простые числа
for i in numbers:
    if i <= 1:
        continue
    if i == 2:
        primes.append(i)
        continue
    if i % 2 == 0:
        not_primes.append(i)
        continue
    k = 0
    for q in range(2, i // 2 + 1):
        if (i % q == 0):
            k = k + 1
    if (k <= 0):
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)