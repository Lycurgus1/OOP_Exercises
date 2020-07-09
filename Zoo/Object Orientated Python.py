# Object orientated python

# Inheritance, polymorhpism, encapsulation, abstraction

class Dog:
    amimal_kind = "Canine" # Class variable

    # Init intalizes class
    # Give/find name and color for dog
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        return "woof, woof"

    # create a methods inside for sleep, breath, run, eat

    # Encapsulation. This creates a private method. Abstraction is a expansion on this
    def __sleep(self):
        return "zzzzz"

    # Pas enables this function without error
    def breath(self):
        pass

    # Inheritance. This refers to creating sub classes, but run is using is a
    # previously define attribute
    def run(self):
        return "Come back, {}".format(self.name)

    # Polymorphism. Here the sub class method overrides the methods in the
    # parent class when appropriate. It first searches it its own class, then
    # in its inherited class
    def eat(self):
        print("{} is eating fast".format(self.__class__.__name__))

class Retriever(Dog):
    def eat(self):
        print("Retriever is eating slowly")

class Labrador(Dog):
    pass

# Creating object of our class
jim = Dog("Canine", "White")
peter = Dog("peter", "Brown")
print(jim.name)

# Testing encapsulation
print(peter.__sleep())

# Testing inheritance
print(peter.run())

# Testing polymorphism
jack = Labrador("Bill", "Black")
jill = Retriever("Ben", "Brown")
jack.eat()
jill.eat()
