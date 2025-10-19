import random

class Pokemon:
    pokemons = {}

    def __init__(self, name, trainer):
        self.name = name
        self.pokemon_trainer = trainer
        self.hp = random.randint(50, 100)
        self.power = random.randint(10, 20)
        self.exp = 0
        self.level = 1

    def info(self):
        return (f"Имя: {self.name}\n"
                f"Тренер: {self.pokemon_trainer}\n"
                f"Здоровье: {self.hp}\n"
                f"Сила: {self.power}\n"
                f"Уровень: {self.level}\n"
                f"Опыт: {self.exp}\n")

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = random.randint(1, 5)
            if chance == 1:
                return f"{enemy.name} применил магический щит! Урон не прошёл!"

        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"{self.name} атакует {enemy.name} и наносит {self.power} урона!"
        else:
            enemy.hp = 0
            self.exp += 10
            self.level_up()
            return f"{self.name} побеждает {enemy.name} и получает 10 опыта!"

    def heal(self):
        heal_amount = random.randint(10, 30)
        self.hp += heal_amount
        return f"{self.name} восстановил {heal_amount} здоровья! Теперь HP: {self.hp}"

    def level_up(self):
        if self.exp >= 20:
            self.level += 1
            self.exp = 0
            self.hp += 10
            self.power += 3

class Wizard(Pokemon):
    def __init__(self, name, trainer):
        super().__init__(name, trainer)
        self.hp += 20
        self.power -= 3

    def info(self):
        return "🧙 У тебя покемон-волшебник!\n" + super().info()

class Fighter(Pokemon):
    def __init__(self, name, trainer):
        super().__init__(name, trainer)
        self.hp -= 10
        self.power += 5

    def attack(self, enemy):
        super_power = random.randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\n🥊 Боец применил супер-атаку силой: {super_power}!"

    def info(self):
        return "🥊 У тебя покемон-боец!\n" + super().info()
