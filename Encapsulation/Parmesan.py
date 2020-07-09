# Importing the Cheese class
from Cheeses import Cheeses

# Creating a child class
class Parmesan(Cheeses):

    # Intialising the class and inheriting the attributes of cheeses using super()
    def __init__(self, cheese_type, main_meal, country):
        super().__init__(cheese_type, main_meal)
        self.country = country

    # This uses an if loop to check if the main_meal is in a tuple. This determines the message returned
    # This also uses formatting to insert values into strings.
    def consume(self):
        if self.main_meal.lower() in ("pasta", "spaghetti"):
            return("Parmesan goes really with {}".format(self.main_meal))
        else:
            return("Parmesan doesn't really go with {} well, maybe have pasta instead?".format(self.main_meal))

    # This is another if loop, testing the country variable.
    # The lower method enables checking the user repsonse without worrying about capitals.
    def italian_parmesan(self):
        if self.country.lower() == "italy":
            return("Good choice, Parmesan is best from Italy")
        else:
            return("I didn't know {} made parmesan".format(self.country))

    # Demonstrating that this method is only callable inside the cheeses class
    # print(__yum(max))

# Testing the code.
max = Parmesan("Cheddar", "Pasta" , "Italy")
print(Parmesan.consume(max))
print(Parmesan.italian_parmesan(max))