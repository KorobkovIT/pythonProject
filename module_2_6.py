#Слишком древний шифр
import random
w = 0
result = []
first_insert = list(range(3, 21)) #[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in first_insert:
    first_insert_new = random.choice(first_insert)
    break
print(f'Число в первом поле: {first_insert_new}')
second_insert = list(range(1, 21)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
q = 1
while w < 10:
    if first_insert_new % (second_insert[w]+second_insert[w+q])==0 and (w+q) <= 18:
        result.append(f'{second_insert[w]}{second_insert[w+q]}')
        q += 1
    elif (w+q) <= 18:
        q += 1
        continue
    else:
        w += 1
        q = 1
result = ''.join(map(str, result))
print(f'Сгенерированный пароль, для ввода во втором поле: {result}')