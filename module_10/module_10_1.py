"""
Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы"
"""
from time import sleep
import threading

def wite_words(word_count, file_name):  #word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
    n = 0
    with open(file_name, 'a', encoding='utf-8') as file:
        while n != word_count:
            n += 1
            file.write(f'Какое-то слово № {n}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл{file_name}')



wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

wite_words(0, 'example5.txt')
wite_words(30, 'example6.txt')
wite_words(200, 'example7.txt')
wite_words(100, 'example8.txt')
