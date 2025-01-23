"""
Цель: понять как работают исключения внутри функций и как обрабатываются эти исключения на практике при помощи try-except.
Задача "План перехват"
"""

def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for element in numbers:
        try:
            result += element
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {element}")
    return result, incorrect_data

def calculate_average(numbers): #Среднее арифметическое - сумма всех данных делённая на их количество
    summ = 0
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        total_numbers = len(numbers) - incorrect_data
        return total_sum / total_numbers
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

if __name__ == "__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать


