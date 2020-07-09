# From the Calculator file importing everything
from Calculator import *

# Inheriting the python calculator from the previous page
class More_Methods(Python_Calculator):

    # As per first command self not needed
    def remainder_test():
        # Input commands get the numbers to be used, and they are converted to integers with int
        print("This tests whether there will be a remainder to a divison, returning true and false")
        num1 = int(input("Please enter your first number\n"))
        num2 = int(input("Please enter your second number\n"))
        outcome = num1 % num2
        # Using the outcome we test if it is 0(False in boolean) or not zero(True in boolean).
        # This determines what the user is told with a further message elaborating.
        if bool(outcome) == True:
            print("True")
            return ("This returns a remainder of {}".format(outcome))
        elif bool(outcome) == False:
            print("False")
            return ("This divison has no remainder")

    # As per first command self not needed
    def triangle_area():
        # Input commands get the numbers to be used, and they are converted to integers with int
        height = int(input("Enter triangle height in cm\n"))
        width = int(input("Enter triangle width in cm\n"))
        # This calculates the area of a triangle and returns it in a user friendly string
        area = (width * height) / 2
        return ("The triangle's area is {} cm".format(area))

    # As per first command self not needed
    def inches_to_cm():
        # Input commands get the numbers to be used, and they are converted to integers with int
        inches = int(input("Enter amount of inches to convert here, please \n"))
        # This calculates the conversion and returns it in a user friendly string
        cm = math.ceil(inches * 2.54)
        return("That converts to {} Centimetres".format(cm))

# To test functions
print(More_Methods.remainder_test())
print(More_Methods.inches_to_cm())
