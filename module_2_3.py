print("Нули ничто, отрицание недопустимо!")
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
q = 0
while q < len(my_list):
    if my_list[q] > 0:
        print(my_list[q])
        q = q + 1
    elif my_list[q] == 0:
        q = q + 1
        continue
    else:
        break

if q < len(my_list):
    print('Встретилось отрицательное число.')
else:
    print('Закончился список.')