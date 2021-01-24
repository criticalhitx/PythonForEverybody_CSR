class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")
    
    def party(self):
        self.x = self.x+1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal): #This will inherit parent class function, including party()
    points = 0
    def touchdown(self): #Additional method definition in child object
        self.points = self.points + 7
        self.party() #Call party() on main Class
        print(self.name, "points", self.points)

s = PartyAnimal("Sally") #construct PartyAnimal object
s.party()

j = FootballFan("Jim") #Will Create Jim as nam parameter
j.party()
j.touchdown()

"""Result
Sally constructed
Sally party count 1
Jim constructed    
Jim party count 1
Jim party count 2
Jim points 7
"""