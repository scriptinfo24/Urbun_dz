def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as f:
        for index, string in enumerate(strings, start=1):
            start_byte = f.tell()  # текущ позиц в байтах
            f.write(string + '\n')  # Запис стр в файл
            strings_positions[(index, start_byte)] = string  # Сохр словарь

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
