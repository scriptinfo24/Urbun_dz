def find_pairs(target_number):
    # Результирующий список для пар
    pairs = []

    # Перебираем все пары чисел от 1 до 19 (включительно)
    for i in range(1, 20):
        for j in range(1, 20):
            sum_of_pairs = i + j

            # Проверяем, кратно ли target_number сумме пары
            if sum_of_pairs != 0 and target_number % sum_of_pairs == 0:
                pairs.append((i, j))  # Сохраняем пару

    return pairs


# Пример использования с числом из первого поля
import random

# Генерируем случайное число в диапазоне [3, 20]
random_number = random.randint(3, 20)
print(f"Случайное число: {random_number}")

# Ищем пары
pairs = find_pairs(random_number)

# Выводим результат
print("Подходящие пары (a, b):")
for pair in pairs:
    print(pair)
