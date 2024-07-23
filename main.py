# Конечно! Давайте начнем с проектирования и создания игры
# "Битва героев" на Python. Я также дам вам пример плана проекта по этапам,
# который позже можно будет перенести в Kanban-доску для управления задачами.
#
# ### План проекта
#
# #### Этап 1: Подготовка
# 1. Определить требования и функциональность игры.
# 2. Создать структуру проекта.
#
# #### Этап 2: Реализация классов
# 1. Создать класс `Hero`.
#     - Атрибуты: `name`, `health`, `attack_power`.
#     - Методы: `attack(other)`, `is_alive()`.
# 2. Создать класс `Game`.
#     - Атрибуты: `player`, `computer`.
#     - Методы: `start()`.
#
# #### Этап 3: Основная логика игры
# 1. Реализовать логику чередования ходов.
# 2. Реализовать вывод информации о каждом ходе.
# 3. Реализовать объявление победителя.
#
# #### Этап 4: Тестирование и отладка
# 1. Провести тестирование игры.
# 2. Исправить найденные ошибки.
#
# #### Этап 5: Завершение
# 1. Добавить комментарии и документацию.
# 2. Провести финальную проверку.
#
# ### Код игры "Битва героев"
#
# Теперь давайте напишем код для игры:
#
# ```python

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
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player = Hero(name=player_name)
    computer = Hero(name="Компьютерный Злодей", health=100, attack_power=random.randint(15, 25))

    game = Game(player=player, computer=computer)
    game.start()
# ```
#
# ### Kanban-доска
#
# Вы можете использовать инструмент для управления проектами, например,
# Trello, чтобы создать Kanban-доску. Пример задач для доски:
#
# #### To Do
# - [ ] Определить требования и функциональность игры.
# - [ ] Создать структуру проекта.
#
# #### In Progress
# - [ ] Реализовать класс Hero.
# - [ ] Реализовать класс Game.
# - [ ] Реализовать логику чередования ходов.
#
# #### Testing
# - [ ] Провести тестирование игры.
# - [ ] Исправить найденные ошибки.
#
# #### Done
# - [ ] Добавить комментарии и документацию.
# - [ ] Провести финальную проверку.
#
# Используйте эту доску для отслеживания прогресса и управления задачами в проекте.
# Удачи в разработке игры!