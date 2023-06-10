# burrows_park.py
from Control.LocationControl.location  import Location

class burrows_park(Location):
    def __init__(self):
        super().__init__('burrows_park', ["burrows_neighbourhood"]) #Add vistable locations here

    def visit_location(self, player=None):
        if player is not None:
            print("You walk around the park!")
        else:
            super().visit_location()
