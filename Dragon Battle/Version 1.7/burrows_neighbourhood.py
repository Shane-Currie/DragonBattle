# burrows_neighbourhood.py
from location import Location
from angry_cat import AngryCat

class burrows_neighbourhood(Location):
    def __init__(self):
        super().__init__('burrows_neighbourhood', ["burrows_home", "burrows_park","kekistan_city"])
        

    def visit_location(self, player=None):
        if player is not None:
            print("You are wandering around the Burrows neighbourhood.")
            
        else:
            super().visit_location()
