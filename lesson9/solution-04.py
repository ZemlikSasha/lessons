"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать Dog и Cat от класса Animal и
Удалить в дочерних классах те методы, которые имеются у родительского класса. Создать объект каждого класса и
вызвать все его методы.
"""


class Animal:
    def __init__(self, heigth, weight, name, age):
        self.heigth = heigth
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"Run {self.name}")

    def change_name(self, name):
        self.name == name

class Dog(Animal):

    def __init__(self, heigth, weight, name, age):
        self.heigth = heigth
        self.weight = weight
        self.name = name
        self.age = age

    def bark(self):
        print(f"Bark {self.name}")

class Cat(Animal):

    def __init__(self, heigth, weight, name, age):
        self.heigth = heigth
        self.weight = weight
        self.name = name
        self.age = age

    def meow(self):
        print(f"Meow {self.name}")

if __name__ == "__main__":

    dog = Dog(100, 100, "Bob", 10)
    cat = Cat(100, 100, "Tima", 10)

    dog.bark()
    print(dog.name)
    print(dog.age)
    print(dog.weight)
    print(dog.heigth)

    cat.meow()
    print(cat.name)
    print(cat.age)
    print(cat.weight)
    print(cat.heigth)


