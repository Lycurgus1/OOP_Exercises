from Modulus import Modulus

class Mutiplication(Modulus):
    # Intialising the class

    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def multiplication(self):
        return self.num1 * self.num2

obj1 = Mutiplication(12, 3)

print(obj1.multiplication())