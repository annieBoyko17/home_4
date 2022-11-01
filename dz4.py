class grandparent_pet:
        species = "cat"

class parent_pet(grandparent_pet):
        color = "white"
        character = "playful and kind"

class child_pet(parent_pet):
    size = "small"
    def __init__(self,):
        print(self.species)
        print(self.color)
        print(self.character)
        print(self.size)

julie = child_pet()