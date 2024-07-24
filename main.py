
import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if self.computer.is_alive():
                self.computer_turn()
        self.declare_winner()

    def player_turn(self):
        self.player.attack(self.computer)
        self.print_status()

    def computer_turn(self):
        self.computer.attack(self.player)
        self.print_status()

    def print_status(self):
        print(f"{self.player.name} здоровье: {self.player.health}")
        print(f"{self.computer.name} здоровье: {self.computer.health}")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")L


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player = Hero(name=player_name)
    computer = Hero(name="Компьютерный Злодей", health=100, attack_power=random.randint(15, 25))

    game = Game(player=player, computer=computer)
    game.start()
