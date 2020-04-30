class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print("constructed: ", self.name)

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    def __del__(self):
        print('destructed', self.name)


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7 
        self.party()
        print( self.name, "points", self.points )



s = FootballFan('Sunzid')
s.party()


j = FootballFan('Shahrin')
j.party()
j.touchdown()
