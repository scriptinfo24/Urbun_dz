def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с различным количеством аргументов
print_params()  # 1 строка True
print_params(42)  # 42 строка True
print_params(3.14, 'пример')  # 3.14 пример True
print_params(b=25)  # 1 25 True
print_params(c=[1, 2, 3])  # 1 строка [1, 2, 3]

# Распаковка параметров
values_list = [2.5, 'другой текст', False]
values_dict = {'a': 10, 'b': 'новая строка', 'c': None}

print_params(*values_list)  # 2.5 другой текст False
print_params(**values_dict)  # 10 новая строка None

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # 54.32 Строка 42
