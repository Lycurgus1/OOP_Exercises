# abc is where the abstract method functions come from so must be imported
from abc import *

# Creating the class to be inherited
class Exercise:

    # This defines the abstract method. It is empty so the child classes can modify it per requirements
    # This method effectively acts as a template
    @abstractmethod
    def drink_water(self):
        pass

    # This is a non abstract method so does not need to be included in child classes
    def warm_up(self):
        return("Strech your legs!")
