"""
Задача "Найдёт везде"
"""

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в виде кортежа

    def get_all_words(self):
        all_words = {}  # Создаем пустой словарь для хранения слов
        for file_name in self.file_names:
            # Предполагаем, что файл существует
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []  # Список для хранения слов из текущего файла
                for line in file:
                    line = line.lower()  # Приводим строку к нижнему регистру
                    # Убираем пунктуацию
                    line = ''.join(char for char in line if char.isalnum() or char.isspace() or char == '-')
                    words.extend(line.split())  # Разбиваем строку на слова и добавляем в список
                all_words[file_name] = words  # Добавляем в словарь
        return all_words

    def find(self, word):
        all_words = self.get_all_words()  # Получаем все слова
        result = {}
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1  # +1 для позиционирования с 1
        return result

    def count(self, word):
        all_words = self.get_all_words()  # Получаем все слова
        result = {}
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        for name, words in all_words.items():
            result[name] = words.count(word)  # Считаем количество вхождений слова
        return result

if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')

    # Вывод всех слов из файла
    print(finder.get_all_words())  # Все слова

    # Поиск слова 'text'
    print(finder.find('text'))      # Позиция слова 'text'

    # Подсчет количества слова 'text'
    print(finder.count('text'))     # Количество слов 'text' в тексте