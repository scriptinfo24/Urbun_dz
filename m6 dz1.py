class Figure:
    sides_count = 0

    def __init__(self, color):
        self.__sides = [1] * self.sides_count  # Инициализация сторон
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)
        self.__sides = [1]  # Одна сторона
        self.__radius = circumference / (2 * 3.14159)  # Рассчитываем радиус

    def get_square(self):
        return 3.14159 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.set_sides(a, b, c)

    def get_square(self):
        s = sum(self.__sides) / 2
        return (s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color)
        self.__sides = [side_length] * self.sides_count  # 12 одинаковых сторон

    def get_volume(self):
        return self.__sides[0] ** 3  # Объем куба


# Пример использования
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())

