class Map:
    def __init__(self):
        self.locations = ["burrows_home", "burrows_neighbourhood", "the_bush", "burrows_park","kekistan_city","the_river"]


    def get_location(self, location_name):
        if location_name in self.locations:
            module = __import__(location_name)
            location = getattr(module, location_name)()
            print(f"Retrieved location: {location.name}")
            return location
        else:
            print(f"Location '{location_name}' not found.")
            return None
