# dragon.py
from animal_enemy import Animal
import random

class Dragon(Animal):
    def __init__(self):
        super().__init__('Dragon')
        self.confidence = random.randint(1, 20)
        self.anger = random.randint(1, 20)
        self.fear = random.randint(1, 20)
        self.luck = random.randint(1, 20)
        self.health = self.level * 10  # specific health calculation for Dragon
        self.attack_value = self.level * 5  # specific attack value calculation for Dragon

    def attack(self, player):
        super().attack(player)
        if self.health < 75:
            self.confidence -= 5
        if self.health < 50:
            self.confidence -= 10
