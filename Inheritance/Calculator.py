# The maths module is imported to get the function of rounding from it for a later method
import math

# This creates the class
class Python_Calculator:

    # A method is created, and as it does not need a class object does not mention self.
    def add_values():
        # Input commands get the numbers to be used, and they are converted to integers with int
        num1 = int(input("Please enter your first number\n"))
        num2 = int(input("Please enter your second number\n"))
        # The outcome is calculated then returned with a format placeholder than tells the user the result
        outcome = num1 + num2
        return "Your result is {}".format(outcome)

    # As per first command self not needed
    def subtract_values():
        # Input commands get the numbers to be used, and they are converted to integers with int
        num1 = int(input("Please enter your first number\n"))
        num2 = int(input("Please enter your second number\n"))
        # The outcome is calculated then returned with a format placeholder than tells the user the result
        outcome = num1 - num2
        return "Your result is {}".format(outcome)

    # As per first command self not needed
    def divide_values():
        # Input commands get the numbers to be used, and they are converted to integers with int
        num1 = int(input("Please enter your first number\n"))
        num2 = int(input("Please enter your second number\n"))
        # The outcome is calculated then returned with a format placeholder than tells the user the result
        outcome = num1 / num2
        return "Your result is {}".format(outcome)

    # As per first command self not needed
    def multiply_values():
        # Input commands get the numbers to be used, and they are converted to integers with int
        num1 = int(input("Please enter your first number\n"))
        num2 = int(input("Please enter your second number\n"))
        # The outcome is calculated then returned with a format placeholder than tells the user the result
        outcome = num1 * num2
        return "Your result is {}".format(outcome)

    # As per first command self not needed
    def remainder_values():
        # Input commands get the numbers to be used, and they are converted to integers with int
        num1 = int(input("Please enter your first number\n"))
        num2 = int(input("Please enter your second number\n"))
        # The outcome is calculated then returned with a format placeholder than tells the user the result
        outcome = num1 % num2
        return "Your result is {}".format(outcome)



