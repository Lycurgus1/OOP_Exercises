# Make army class
class Army:

    # Intialising class
    def __init__(self, name, army_size, composition, supplies):
        self.name = name
        self.army_size = int(army_size)
        self.compostion = composition
        self.supplies = int(supplies)

    # Method to increase army size
    def recruit(self):
        # Getting user input and converting to integer, to prevent errrors integrating with integer variables
        increase = int(input("How many troops would you like to add to the army(In thousands)?\n"))
        self.army_size = self.army_size + increase
        print("Your army has got {}k troops".format(self.army_size))

    # Method to increase supplies
    def resupply(self):
        # Getting user input and converting to integer, to prevent errrors integrating with integer variables
        increase = int(input("How many supplies are added(day's worth of rations)?\n"))
        self.supplies = self.supplies + increase
        print("You now have supplies to last {} days".format(self.supplies))

    # Battle cry method. This will be overwritten in child classes
    def battlecry(self):
        return("Gods, I hate Gauls")



# macedonia = Army("Alexander", 15, "Pikemen", 10)
# print(macedonia.battlecry())