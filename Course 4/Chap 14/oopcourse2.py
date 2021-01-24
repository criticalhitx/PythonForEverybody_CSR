class PartyAnimal:
    x = 0
    name = ""
    
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally") # Parameter required because it is defined on __init__ of the Class
s.party()

j = PartyAnimal("Jim")
j.party()

s.party()
j.party()

"""Result
Sally constructed
Sally party count 1
Jim constructed
Jim party count 1
Sally party count 2
Jim party count 2
"""