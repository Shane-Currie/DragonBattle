class Location:
    def __init__(self, name, visitable_locations):
        self.name = name
        self.visitable_locations = visitable_locations

    def visit_location(self, player=None):
        print(f"You arrived at {self.name}.")

def visit_location(self, player=None):
    print(f"Travelling to {self.name}...")

    def view_options(self):
        print(f"You are currently at {self.name}.")
        print("You can travel to the following locations:")
        for i, location in enumerate(self.visitable_locations, start=1):
            print(f"{i}. {location}")
