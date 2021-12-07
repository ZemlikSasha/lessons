"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""


class Cat:
    def __init__(self, heigth, weight, name, age):
        self.heigth = heigth
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"Run {self.name}")

    def meow(self):
        print(f"Meow {self.name}")


if __name__ == "__main__":
    cat = Cat(100, 100, "Tima", 10)
    cat.jump()

    print(cat.name)
    print(cat.age)
    print(cat.weight)
    print(cat.heigth)