# the_river.py
from Control.LocationControl.location import Location
import random
from Control.FightControl.fight import fight
from Encounter.Animal.Hostile.dragon import Dragon
from Encounter.Animal.Hostile.angry_cat import AngryCat
from Encounter.Foliage.tree import Tree
from Encounter.Animal.Hostile.Control.animal_enemy import Animal


class the_river(Location):
    def __init__(self):
        super().__init__('the_river', ["the_bush"]) #Add vistable locations here

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

        action = input("Do you want to 1. Continue exploring 2. leave the river? ")
        if action == '2':
            self.visitable_locations = ["the_bush"] #Add vistable locations here
        else:
            self.visitable_locations = ["the_river"] #Add vistable locations here

    def visit_location(self, player=None):
        if player is not None:
            self.explore(player)
        else:
            super().visit_location()
