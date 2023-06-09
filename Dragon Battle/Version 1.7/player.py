from map import Map

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.map = Map()
        self.location = self.map.get_location("burrows_home")
        print(f"Player's location: {self.location}")


    def is_alive(self):
        return self.health > 0

    def travel_to(self, location_name):
        new_location = self.map.get_location(location_name)
        if new_location:
            self.location = new_location
            self.location.visit_location(self)
        else:
            print(f"The location {location_name} doesn't exist!")
    def defend(self, enemy):
        self.health += 10
        enemy.attack(self)
        self.health -= max(0, enemy.attack_value - 10)

    def attack(self, enemy):
        enemy.health -= 10


    def play(self):
        action = ''
        while action != 'exit' and self.is_alive():
            print(f"You are currently at {self.location.name}.")
            print("You can travel to the following locations:")
            for i, location in enumerate(self.location.visitable_locations, 1):
                print(f"{i}. {location}")
            action = input("Enter the number of the location you want to travel to, or 'exit' to quit: ")
            if action.isdigit():
                action = int(action)
                if 1 <= action <= len(self.location.visitable_locations):
                    self.travel_to(self.location.visitable_locations[action-1])
                else:
                    print("Invalid input, please enter a number.")
            elif action != 'exit':
                print("Invalid input. Please enter a number or 'exit'.")

        if not self.is_alive():
            print(f"{self.name} has fallen. Game Over.")
# END OF player.PY SCRIPT