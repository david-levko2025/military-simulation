from lessens_exersice_in_the_army.week3.day4.military_simulation.army_inventory import Weapon

class StrikeOption:
    def __init__(self,name:str,ammo:int):
        self.name = name
        self.ammo = ammo
    def strike(self):
        print("we have a strike")
        self.ammo -= 1
        if self.ammo == 0:
            print("out of ammo")

class Tank(StrikeOption):
    def strike(self):
        print("the strike from the tank pass good")
        self.ammo -= 1
        if self.ammo == 0:
            print("out of ammo")

class Drone(StrikeOption):
    def strike(self):
        print("the strike from the drone pass good")
        self.ammo -= 1
        if self.ammo == 0:
            print("out of ammo")
