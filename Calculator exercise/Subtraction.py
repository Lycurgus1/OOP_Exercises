from Addition import Addition

class Subtraction(Addition):
    # Intialising the class
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def subtraction(self):
        return self.num1 - self.num2