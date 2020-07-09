# Importing parent class
from Historical_fight_club import Army

# Creating class
class Attila_nomad(Army):

    # Intialising class
    def __init__(self, name, army_size, composition, supplies, nomadic):
        # Super inherits the attributes from the parent class
        super().__init__(name, army_size, composition, supplies)
        # Bool converts string statements to true or false
        self.nomadic = bool(nomadic)

    # Polymorphic battlecry, battlecry of parent class is supplanted by this
    def battlecry(self):
        return("Ululululu")

# Testing code
hunnic_hordes = Attila_nomad("Buda", 15, "Cavalry", 5, True)
print(hunnic_hordes.battlecry())
print(hunnic_hordes.supplies)
hunnic_hordes.resupply()
