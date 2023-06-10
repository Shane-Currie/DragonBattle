import importlib

class Map:
    def __init__(self):
        self.locations = {
            "burrows_home": "WorldMap.KekistanCity.BurrowsNeighbourhood.burrows_home",
            "burrows_neighbourhood": "WorldMap.KekistanCity.BurrowsNeighbourhood.burrows_neighbourhood",
            "the_bush": "WorldMap.TheBush.the_bush",
            "burrows_park": "WorldMap.KekistanCity.BurrowsNeighbourhood.burrows_park",
            "kekistan_city": "WorldMap.KekistanCity.kekistan_city",
            "the_river": "WorldMap.TheBush.the_river"
        }

    def get_location(self, location_name):
        if location_name in self.locations:
            try:
                module = importlib.import_module(self.locations[location_name])
                location = getattr(module, location_name)()
                print(f"Retrieved location: {location.name}")
                return location
            except ImportError:
                print(f"Module '{location_name}' not found.")
                return None
        else:
            print(f"Location '{location_name}' not found.")
            return None
