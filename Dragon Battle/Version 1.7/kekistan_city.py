# kekistan_city.py
from location import Location


class kekistan_city(Location):
    def __init__(self):
        super().__init__('kekistan_city', ["burrows_neighbourhood"])
        

    def visit_location(self, player=None):
        if player is not None:
            print("You are wandering around Kekistan City.")
            
        else:
            super().visit_location()
