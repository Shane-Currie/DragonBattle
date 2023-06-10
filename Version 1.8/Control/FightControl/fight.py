# fight.py
import random 

# fight.py
import random 

def fight(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f"\nPlayer's Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}\n")

        action = input("Do you want to attack, defend, ignore, flee, or view stats? ")
        if action.lower() == "attack":
            player.attack(enemy)
            print(f"You attacked the {enemy.name}!")
        elif action.lower() == "defend":
            player.defend(enemy)
            print("You defended yourself!")
        elif action.lower() == "ignore":
            enemy.attack(player)
            print(f"The {enemy.name} attacked you!")
        elif action.lower() == "flee":
            print("You managed to flee!")
            return
        elif action.lower() == "view stats":
            enemy.display_stats()
        else:
            print("Invalid action, please try again.")
            continue

       #enemy action decision based on emotions and luck (will chaange to emotions and confidence)
        #will need to look at also including a  atatck decision randint value, such as a attion_decision_draw
        #Emeny action value could be affected by the confidence, emotional and the action_decision_draw
        #luck will affect if the enemy action is successfull of unsucessfull
        luck_draw = random.randint(1, 20) 
        if luck_draw > enemy.luck and enemy.confidence > 10:
            # High confidence leads to attack (will change to the value of the decision draw, a higher number in the decision draw can result in successfull attack)
            print(f"The {enemy.__class__.__name__} is feeling confident!")
            enemy.attack(player)
        elif enemy.fear > 10:
            # High fear leads to inaction (fear value will increase if the player is a higher level then the enemy)
            print(f"The {enemy.__class__.__name__} is too scared to do anything!")
        elif enemy.anger > 10:
            # High anger leads to reckless attack
            print(f"The {enemy.__class__.__name__} is furious!") #include a condition where the enemy will take minor damage due to a reckless attack
            enemy.attack(player)
        else:
            # Default action is to attack (will change to flee, a successfull flee action depends on the value of the action_decision_draw and a enemies agility skill and confidence skill)
            enemy.attack(player)
        print(f"The {enemy.__class__.__name__} attacked you!")

    # Print final health status after battle
    print(f"\nFinal Health Status:")
    print(f"Player's Health: {player.health}")
    print(f"{enemy.__class__.__name__}'s Health: {enemy.health}\n")
    #should include a condition where the player will gain experience points after the battle, these experience points will level up the player

    if player.is_alive():
        print(f"You defeated the {enemy.__class__.__name__}!")
    else:
        print(f"You were defeated by the {enemy.__class__.__name__}!")
