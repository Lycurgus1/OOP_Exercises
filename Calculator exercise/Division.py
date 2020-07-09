from Subtraction import Subtraction

class Division(Subtraction):
    # Intialising the class
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def divison(self):
        return self.num1 / self.num2