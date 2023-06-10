# burrows_home.py
from Control.LocationControl.location import Location

class burrows_home(Location):
    def __init__(self):
        super().__init__('burrows_home', ["burrows_neighbourhood", "the_bush","kekistan_city"]) #Add vistable locations here

    def visit_location(self, player=None):
        if player is not None:
            print("Welcome back home!")
        else:
            super().visit_location()
