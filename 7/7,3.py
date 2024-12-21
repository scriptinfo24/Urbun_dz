class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем названия файлов в виде кортежа
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Читаем строки, переводим в нижний регистр и убираем пунктуацию
                words = []
                for line in file:
                    line = line.lower()
                    line = line.replace(',', '').replace('.', '').replace('=', '').replace('!', '') \
                               .replace('?', '').replace(';', '').replace(':', '').replace('-', ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()  # Приводим к нижнему регистру для поиска
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1  # Позиция первого слова (1-индексация)
        return result

    def count(self, word):
        word = word.lower()  # Приводим к нижнему регистру для подсчета
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            result[name] = words.count(word)  # Подсчет вхождений слова
        return result

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего