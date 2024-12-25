# Данные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин строк, если они не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример выполнения кода
print(list(first_result))  # Вывод: [1, 2]
print(list(second_result))  # Вывод: [False, False, True]
