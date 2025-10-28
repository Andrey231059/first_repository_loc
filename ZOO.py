# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
# # 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например,
# различный звук для `make_sound()`).
# # 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.
# # 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных
# и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# # 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# rom pyclbr import Class


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.animals = []

    def make_sound(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, like_food):
        super().__init__(name, age)
        self.like_food = like_food

    def make_sound(self):
        print("чик-чирик")

class Elephant(Animal):
    def __init__(self, name, age, like_food):
        super().__init__(name, age)
        self.like_food = like_food

    def make_sound(self):
        print("Yyyy")

class Reptile(Animal):
    def __init__(self, name, age, like_food):
        super().__init__(name, age)
        self.like_food = like_food

    def make_sound(self):
        print("Шииии")


class Staff():
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.staffs = []

class ZooKeeper(Staff):
    def __init__(self, name, age, profession):
        super().__init__(name, age, profession)

    def work(self):
        print(f" сотрудник - {self.name} - кормит животных")

class Veterinarian(Staff):
    def __init__(self, name, age, profession):
        super().__init__(name, age, profession)

    def work(self):
        print(f" сотрудник - {self.name} - лечить животных")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staffs = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_animals(self):
        for animal in self.animals:
            print(f" питомец - {animal.name} ")

    def add_staff(self, staff):
        self.staffs.append(staff)

    def print_staffs(self):
        for staff in self.staffs:
            print(f" работник - {staff.name}  - {staff.profession}")

bird = Bird("воробей", "1 год", "Зерно")
elephant = Elephant("Геракл", "3 года", "Морковка")
reptile = Reptile("Кобра", "2 года", "лягушка")
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(elephant)
zoo.add_animal(reptile)
zoo.print_animals()

veterinarian = Veterinarian("Владимир", "35", "Ветеринар")
zooKeeper = ZooKeeper("Петрович", "62", "смотритель")
zoo.add_staff(veterinarian)
zoo.add_staff(zooKeeper)
zoo.print_staffs()
veterinarian.work()
zooKeeper.work()

animals = [bird, elephant, reptile]
for animal in animals:
    animal.make_sound()