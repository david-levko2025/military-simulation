

class StrikeOption:
    def __init__(self,name:str,ammo:int):
        self.name = name
        self.ammo = ammo
    def strike(self):
        print("we have a strike")

class Tank(StrikeOption):
    def strike(self):
        print("the strike from the tank pass good")

class Drone(StrikeOption):
    def strike(self):
        print("the strike from the drone pass good")
