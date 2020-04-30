class PartyAnimal:
    x = 0
    name = "" 

    def __init__(self, z):
        self.name = z
        print(self.name, 'I am constructed')

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print('destructed', self.name)

an = PartyAnimal('zayed')
an2 = PartyAnimal('zia')

an.party()
an2.party()

