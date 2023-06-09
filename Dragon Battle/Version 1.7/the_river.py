# the_river.py
from location import Location
import random
from fight import fight
from dragon import Dragon
from angry_cat import AngryCat
from tree import Tree
from animal_enemy import Animal  # import the new Animal class

class the_river(Location):
    def __init__(self):
        super().__init__('the_river', ["the_bush"])

    def explore(self, player):
        encounter_chance = random.randint(1, 3)  
        if encounter_chance == 1:
            print("You encountered a Dragon!")
            fight(player, Dragon())
        elif encounter_chance == 2:
            print("You encountered an Angry Cat!")
            fight(player, AngryCat())
        else:
            print("You encountered a tree.")
            next_location = Tree().encounter(player)
            self.visitable_locations = [next_location]

        action = input("Do you want to 1. Continue exploring or 2. Return to The Bush? ")
        if action == '2':
            self.visitable_locations = ["the_bush"]
        else:
            self.visitable_locations = ["the_river"]

    def visit_location(self, player=None):
        if player is not None:
            self.explore(player)
        else:
            super().visit_location()
