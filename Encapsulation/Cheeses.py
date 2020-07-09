# Creating the class
class Cheeses:

    # Intialsing the class
    def __init__(self, cheese_type, main_meal):
        self.chese_type = cheese_type
        self.main_meal = main_meal

    # This method has been made private so can only be accessed within the Cheeses class
    def __yum(self):
        return ("I bet you love all types of cheeses")

    # Demonstrating that this method is only callable inside the cheeses class
    print(__yum(max))

# Creating a class object to test
max = Cheeses("Brie", "Sandwich")