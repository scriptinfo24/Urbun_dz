
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [len(s) for s in first_strings if len(s) >= 5]


second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]


third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Пример выполнения кода
print(first_result)  # Вывод: [8, 8, 9]
print(second_result)  # Вывод: [('Elon', 'Task'), ('Musk', 'Task'), ...]
print(third_result)  # Вывод: {'Elon': 4, 'Task': 4, ...}
