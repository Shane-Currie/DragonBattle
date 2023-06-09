class Tree:
    def encounter(self, player):
        print("You walk past a tree.")
        action = input("Do you want to 1. Continue exploring or 2. Return Home? ")
        if action == '1':
            return "TheBush"
        elif action == '2':
            return "PlayerHome"
