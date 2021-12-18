"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0). Методы: увеличить скорости
(скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0), отображение скорости, задния
ход (изменение знака скорости).
"""


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speeds(self):
        self.speed += 5
        print(f"Increase_speeds {self.name}")

    def reduction_speeds(self):
        self.speed -= 5
        print(f"Reduction_speeds {self.name}")

    def stop_speeds(self):
        self.speed *= 0
        print(f"Stop_speeds {self.name}")

    def show_speed(self):
        print(self.speed)

    def reverse_speed(self):
        self.speed *= -1



if __name__ == "__main__":

    car = Car("Mercedes", "E500", 2000, 0)

    print(car.brand)
    print(car.model)
    print(car.year)
    print(car.speed)






