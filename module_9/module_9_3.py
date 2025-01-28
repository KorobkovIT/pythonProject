"""
Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов.
"""

first = ['Strings', 'Student', 'Computers']
second = ["Строка" ,"Урбан", "Компьютер"]
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))


if __name__ == "__main__":
    print(list(first_result))
    print(list(second_result))
