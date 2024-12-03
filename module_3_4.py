def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для подходящих слов
    for word in other_words:  # Перебираем все слова в other_words
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():  # Условие: root_word
            # cодержится в word (игнорируя регистр)
            same_words.append(word)  # Добавляем слово в список, если условие выполнено
    return same_words  # Возвращаем список подходящих слов

# Вызов функции и вывод результата
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # Вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Вывод: ['Able', 'Disable']
