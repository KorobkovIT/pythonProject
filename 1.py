def custom_write(file_name, strings):
    # Создаем пустой словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл для записи
    with open(file_name, 'w', encoding='utf-8') as f:
        # Перебираем строки с их индексами
        for index in range(len(strings)):
            string = strings[index]  # Получаем строку по индексу
            byte_position = f.tell()  # Узнаем текущую позицию в байтах

            # Записываем строку в файл
            f.write(string + '\n')

            # Сохраняем позицию и строку в словарь
            strings_positions[(index + 1, byte_position)] = string

    return strings_positions  # Возвращаем словарь


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# Вызываем функцию и сохраняем результат
result = custom_write('test.txt', info)

# Печатаем результаты
for elem in result.items():
    print(elem)