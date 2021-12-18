"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает
марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""


from solution_1_1 import Car

def fast_speed(car):
    while car.speed < 100:
        car.increase_speeds()
    car.show_speed()
    return

if __name__ == "__main__":
    car = Car("Mersedes", "E500", 2000, 0)

    fast_speed(car)
    print(car.brand)
    print(car.model)
    print(car.year)
    print(car.speed)


