def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)
    # Получаем первую цифру
    first = int(str_number[0])

    if len(str_number) > 1:
        # Если оставшиеся цифры есть, вызываем функцию рекурсивно
        return first * get_multiplied_digits(int(str_number[1:]))
    else:

        return first



result = get_multiplied_digits(40203)
print(result)  # Ожидаемый вывод: 24

result2 = get_multiplied_digits(4020301)
print(result2)  # Ожидаемый вывод: 24

