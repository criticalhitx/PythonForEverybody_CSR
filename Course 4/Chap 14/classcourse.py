#Basic OOP
class PartyAnimal:
    x = 0
    
    def __init__(self): #Construtor, It will be called when an object is created from this class
        print("I am Constructed")

    def party(self):
        self.x = self.x+1
        print("So Far", self.x)
    
    def __del__(self): #Destructor, will be called when object is destoryed / program ends. rarely be used.
        print("I am distructed", self.x)

an = PartyAnimal() #using PartyAnimal template to make Praty Animal object
print("Type", type(an))
print("Dir", dir(an))

an.party() #So Far 1
an.party() #So Far 2