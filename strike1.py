from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self, weapon):
        pass

class Sword(Weapon):
    def attack(self, weapon):
        print("Боец выбрал меч")
        print("Боец наносить удар мечем")
        print("Монстр побежден")

class Bow(Weapon):
    def attack(self, weapon):
        print("Боец выбрал лук")
        print("Боец стреляет из лука")
        print("Монстр побежден")

class Spear(Weapon):
    def attack(self, weapon):
        print("Боец выбрал копьё")
        print("Боец наносить удар копьём")
        print("Монстр побежден")

class Monster():
    def __init__(self, name):
        self.name = name


class Fighter():
    def __init__(self, weapon):
        self.weapon = weapon

    def change_weapon(self):
        self.weapon.attack(self)

fighter = Fighter(Sword())
fighter.change_weapon()

fighter = Fighter(Bow())
fighter.change_weapon()

fighter = Fighter(Spear())
fighter.change_weapon()
