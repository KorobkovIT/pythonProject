"""
Задача "Записать и запомнить"
"""

def custom_write(file_name, strings):   #название файла для записи, список строк для записи
    n = 0
    elem = {}
    for strings in info:
        file = open(file_name, 'a', encoding='utf-8')
        tell = (file.tell())
        n += 1
        file.write(f'{strings}\n')
        file.close()
        elem.update({(n, tell):strings})
    return elem

if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

