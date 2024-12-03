def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список 
    for word in other_words:  
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():  # Условие: 
            
            same_words.append(word)  
    return same_words  # Возвращаем список 

# Вызов функции и вывод результата
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # Вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Вывод: ['Able', 'Disable']
