# Exercise is imported from the Exercise file
from Exercise import Exercise

# Creating a child class of exercise
class Swimming(Exercise):

    # Intialising the class. int converts the inputs to the correct data type.
    def __init__(self, water_level, tiredness):
        self.water_level = int(water_level)
        self.tiredness = int(tiredness)

    # Specailising the abstract method mentioned in the parent class
    # This command also affects the water level variable
    def drink_water(self):
        water = int(input("How much liters of water would you like to drink?\n"))
        self.water_level = self.water_level + (water/2)

    # Creating a new method that affects tiredness, taking in user input.
    # The user input is correctly formatted to ensure it works with other variables
    def rest(self):
        rest_time = int(input("How many minutes do you rest for?\n"))
        self.tiredness = self.tiredness + (rest_time/20)

    # This prints out the variables changed.
    def check_status(self):
        print("Your water level is {}".format(self.water_level))
        print("Your tiredness is {}".format(self.tiredness))

swim1 = Swimming(5, 5)
Swimming.rest(swim1)
Swimming.check_status(swim1)