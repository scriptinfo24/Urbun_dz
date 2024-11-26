# Данные на входе
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в отсортированный список, чтобы сопоставить имена с оценками
sorted_students = sorted(students)

# Создаем словарь для хранения среднего балла
average_grades = {}

# Расчет средних баллов
for student, grade_list in zip(sorted_students, grades):
    average_grades[student] = sum(grade_list) / len(grade_list)

# Вывод результата
print(average_grades)
