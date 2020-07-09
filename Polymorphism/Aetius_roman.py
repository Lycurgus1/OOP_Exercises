# Importing parent class
from Historical_fight_club import Army

# Creating class
class Aetius_roman(Army):

    # Intialising class
    def __init__(self, name, army_size, composition, supplies, settled):
        # Super inherits the attributes from the parent class
        super().__init__(name, army_size, composition, supplies)
        # Bool converts string statements to true or false
        self.settled = bool(settled)

    # Polymorphic battlecry, battlecry of parent class is supplanted by this
    def battlecry(self):
        return("For the emperor!")

# Testing code
romans = Aetius_roman("Silvanus", 10, "Infantry", 10, True)

print(romans.battlecry())
print(romans.army_size)
romans.recruit()