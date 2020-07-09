# Exercise brief
# Create animal class
# Create mammal class
# Create bird class
# Create eagle class

class Animal:

    # Intialising the class
    def __init__(self, alive, eyes):
        self.alive = alive
        self.eyes = eyes

    def breathe(self):
        return "Oxygen is useful"

    def eat(self):
        return "Food is important"

    def procreate(self):
        pass

    def move(self):
        return "To get more food"
