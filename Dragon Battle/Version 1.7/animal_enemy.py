# animal_enemy.py
import random

class Animal:
    def __init__(self, name):
        self.name = name
        self.level = random.randint(1,10)
        self.skill_points = self.level * 3
        self.attack_skill = random.randint(1, self.skill_points)
        self.agility_skill = self.skill_points - self.attack_skill

    def is_alive(self):
        return self.health > 0

    def attack(self, player):
        player.health -= self.attack_value

    def display_stats(self):
        print(f"{self.name}'s stats:")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack_skill}")
        print(f"Agility: {self.agility_skill}")
