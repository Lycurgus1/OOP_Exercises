# Importing parent class
from First_check import Initial_check

# Creating the child class, inheriting the parent class's methods
class More_information(Initial_check):

    # Intialsing class but no attributes needed, so pass prevents errors
    def __init__(self):
        pass

    # This method takes an input of a code
    def more_information(self):
        print("Sometimes websites don't work, have you checked the spelling?")
        code = int(input("What status code do you want to know about?\n"))
        # It then takes that code and prints out a message depending on the code
        if code == 200:
            print("200 means the website is all good")
        if code == 202:
            print("202 means the request is working but has not been acted on yet, just wait a bit!")
        if code == 301:
            print("301 means the URL has been moved, you should receive the new URL!")
        else:
            print("Sorry, I don't know what {} means".format(code))


# Creating object of child class
obj1 = More_information()

# Creating object of parent class
obj2 = Initial_check()

# Testing the code
obj1.intial_check()
obj1.more_information()