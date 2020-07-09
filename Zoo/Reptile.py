from Animal import Animal

# Mentioning the class to be inherited
class Reptile(Animal):

    # This function intialises the class
    def __init__(self, alive, eyes,cold_blooded, tetrapod, heart_chambers, amniotic_eggs):
        # The super line inherits attributes from the Animal Class
        super().__init__(alive, eyes)
        self.cold_blooded = cold_blooded
        self.tetrapod = tetrapod
        self.heart_chambers = heart_chambers
        self.amniotic_eggs = amniotic_eggs

    def seek_heat(self):
        return "Where is the lamp"

    def hunt(self):
        return "find some food"

    def use_venom(self):
        return

    def attract_mate_through_scent(self):
        pass

max = Reptile(True, 2, False, False, 2, False)

print(max.heart_chambers)
