from itertools import count
from time import sleep

print('Введите три числа, программа выведет кол-во одинаковых чисел среди 3-х введённых: ')
sleep(1)
first = int(input('first: '))
second = int(input('second: '))
third = int(input('third: '))
if first == second == third:
    print('Количество одинаковых чисел среди 3-х введённых:', 3)
elif first == second or first == third or second == third:
    print('Количество одинаковых чисел среди 3-х введённых:', 2)
else:
    print('Количество одинаковых чисел среди 3-х введённых:', 0)

print('Счетчик повторяющихся цифр в составе числа: ')
first = str(first)
second = str(second)
third = str(third)
from collections import Counter
nambers = []
nambers.extend(first)
nambers.extend(second)
nambers.extend(third)
c = Counter(nambers)
print(c)