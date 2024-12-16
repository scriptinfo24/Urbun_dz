import random

# Родительский класс Animal
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound if self.sound else "Silence")


# Класс Bird, наследующий Animal
class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


# Класс AquaticAnimal, наследующий Animal
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # берём значение по модулю
        self._cords[2] -= dz
        self.speed /= 2  # скорость уменьшается в 2 раза


# Класс PoisonousAnimal, наследующий Animal
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


# Класс Duckbill, наследующий Bird, AquaticAnimal, PoisonousAnimal
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)  # ив


# Пример использования
db = Duckbill(10)

print(db.live)      # True
print(db.beak)      # True

db.speak()          # "Click-click-click"
db.attack()         # "Sorry, i'm peaceful :)"

db.move(1, 2, 3)    # Двигаемся
db.get_cords()      # X: 10, Y: 20, Z: 30

db.dive_in(6)       # Ныряем
db.get_cords()      # X: 10, Y: 20, Z: 24

db.lay_eggs()       #  (X - случайное число от 1 до 4)
