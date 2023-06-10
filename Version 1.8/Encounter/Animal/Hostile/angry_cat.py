# angry_cat.py
from Encounter.Animal.Hostile.Control.animal_enemy import Animal
import random

class AngryCat(Animal):
    def __init__(self):
        super().__init__('Angry Cat')
        self.confidence = random.randint(1, 20)
        self.anger = random.randint(1, 20) #shoud not be random and should be affected when the enemy is attacked by the player
        self.fear = random.randint(1, 20) #should not be random and should be affected by the players level or the enemies health
        self.luck = random.randint(1, 20)
        self.health = self.level * 5  # specific health calculation for Angry Cat
        self.attack_value = self.level * 2.5  # specific attack value calculation for Angry Cat

    def attack(self, player):
        super().attack(player) 
        if self.health < 75:
            self.confidence -= 5
        if self.health < 50:
            self.confidence -= 10
