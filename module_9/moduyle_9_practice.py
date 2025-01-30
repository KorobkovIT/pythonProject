#1 - написать функцию, которая возвращает функцию повторения двух первых символов n раз
#2 - создать массив функций и применить все функции поочередно к аргументу
#3 - применить все функции поочередно к массиву аргументов

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
