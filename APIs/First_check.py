# Importing relevant library for API functions
import requests

# Creating the class
class Initial_check:

    # Intialsing class but no attributes needed, so pass prevents errors
    def __init__(self):
        pass

    # Creating second method
    def intial_check(self):
        # The inputted website has its webstatus record
        website = input("What url would you like to check?\n")
        web_status = (requests.get(website)).status_code
        # This if loop uses the web_status to change the message sent
        if web_status == 200:
            print("You got status code {}, it worked!".format(web_status))
        elif web_status == 404:
            print("You got status code {}, this page was not found :(".format(web_status))
        else:
            print("You got status code {}, something went wrong!".format(web_status))

