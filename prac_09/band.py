from musician import Musician


class Band:

    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        self.members.append(musician)

    def play(self):
        for musician in self.members:
            if not musician.instruments:
                print(f'{musician.name} needs an instrument')
            else:
                print(f'{musician.name} is playing: {musician.instruments[0]}')

    def __str__(self):
        output = f"{self.name} ("
        for member in self.members:
            output += str(member)
        output += ")"
        return output
