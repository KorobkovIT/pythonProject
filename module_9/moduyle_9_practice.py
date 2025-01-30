#1 - написать функцию, которая возвращает функцию повторения двух первых символов n раз
#2 - создать массив функций и применить все функции поочередно к аргументу
#3 - применить все функции поочередно к массиву аргументов
<<<<<<< HEAD
#4 - Есть функция, котораяя возвращает результат введения числа А в степень Б. Нужно ускорить ее, чтобы она не делала повторные вычисления
=======
>>>>>>> 80865db0226839c76b6b1b9107bd1f7d66d6c27f

animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']

#1

def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal
    return repeat


test_1 = gen_repeat(1)
test_2 = gen_repeat(2)
print(test_1(animal))
print(test_2(animal))

#2
<<<<<<< HEAD

repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)

#3

fin_result = [func(x) for func in repetitions for x in animals]
print(fin_result)

#4

"""def func(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a**b

print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')"""

def memoize_func(f):
    mem = {}
    def wrapper(*args):
        print(f'Выполнение функции с аргументами = {args}, внутренняя память = {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена раньше, ответ = {mem[args]}'
    return wrapper

@memoize_func
def func(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a**b

print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
=======
>>>>>>> 80865db0226839c76b6b1b9107bd1f7d66d6c27f
