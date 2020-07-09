from Reptile import Reptile

class Snake(Reptile):

    def __init__(self, cold_blooded, forked_tongue, venom, limbs):
        self.cold_blooded = cold_blooded
        self.forked_tongue = forked_tongue
        self.venom = venom
        self.limbs = limbs

    def use_tongue_to_smell(self):
        pass

