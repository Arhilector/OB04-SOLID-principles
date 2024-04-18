import random
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

class Fighter:
    def __init__(self, health=50):
        self.weapon = None
        self.health = health

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Боец не может атаковать без оружия!"

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "Боец побежден!"
        else:
            return f"Здоровье бойца: {self.health}"

class Monster:
    def __init__(self, health=50):
        self.health = health

    def isDefeated(self):
        return self.health <= 0

    def attack(self):
        return 15  # Монстр наносит 10 урона

def fight(fighter, monster):
    while not monster.isDefeated() and fighter.health > 0:
        if random.choice([True, False]):  # рандомная атака
            # Боец атакует монстра
            attack_result = fighter.attack()
            print(attack_result)
            if fighter.weapon:
                monster.health -= 15
                print(f"Текущее здоровье монстра: {monster.health}")
                if monster.isDefeated():
                    print("Монстр побежден!")
                    break
        else:
            # Монстр атакует бойца
            damage = monster.attack()
            result = fighter.takeDamage(damage)
            print(f"Монстр атакует! {result}")

# Демонстрация работы программы
player = Fighter()
monster = Monster()

player.changeWeapon(Sword())
print("Бой начинается!")
fight(player, monster)

monster = Monster()
player = Fighter()
player.changeWeapon(Bow())
print("Новый бой начинается!")
fight(player, monster)