"""
Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы"
"""
from time import sleep

def wite_words(word_count, file_name):  #word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
    n = 0
    with open(file_name, 'a', encoding='utf-8') as file:
        while n != word_count:
            n += 1
            file.write(f'Какое-то слово № {n}\n')




wite_words(10, 'example1.txt')
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
