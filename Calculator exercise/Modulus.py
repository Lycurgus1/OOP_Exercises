from Division import Division

class Modulus(Division):
    # Intialising the class
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def modulus(self):
        return self.num1 % self.num2