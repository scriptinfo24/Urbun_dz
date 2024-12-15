class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Имя дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")  # Проверка на существование этажа
        else:
            for floor in range(1, new_floor + 1):
                print(floor)  # Вывод этажей от 1 до new_floor включительно

# Создание объекта класса House
my_house = House('ЖК Эльбрус', 30)


h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)