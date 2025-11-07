import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        #Случайным образом выбираем силу удара
        damage = random.randint(1, 20)
        other.health -= damage
        if other.health < 0:
            other.health = 0
        print(f"{self.name} атакует и наносит удар силой - {damage}! У {other.name} осталось {other.health} % здоровья.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Добро пожаловать в игру 'Битва героев'!")
        print(f"{self.player.name} против {self.computer.name}")
        print("Бой начинается!\n")

        # Случайно определяем, кто ходит первым
        current_turn = random.choice(['player', 'computer'])

        while self.player.is_alive() and self.computer.is_alive():
            if current_turn == 'player':
                self.player.attack(self.computer)
                current_turn = 'computer'
            else:
                self.computer.attack(self.player)
                current_turn = 'player'

            print()  # Пустая строка для читаемости

        # Объявление победителя
        if self.player.is_alive():
            print(f"Победил {self.player.name}!")
        else:
            print(f"Победил {self.computer.name}!")


# Запуск игры
name = input("Введите имя своего героя: ")
game = Game(name)
game.start()