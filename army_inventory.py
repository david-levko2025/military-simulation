from lessens_exersice_in_the_army.week3.day4.military_simulation.strike_options import Tank,Drone
from  abc import ABC,abstractmethod

class Weapon:
    total_weapon = 0
    serial = 0
    def __init__(self, name:str,ammo:int):
        self.name = name
        self.ammo = ammo
        self.total_weapon += 1
        self.serial_number = Weapon.serial

    def __str__(self):
        return f'the weapon: {self.name} and is serial number {self.serial_number}'

    def reload(self,amount):
        amount = 30
        max_capacity = 120
        if self.ammo in Weapon == 30:
            self.ammo += amount
            max_capacity -= amount




class Solider:
    def __init__(self,name:str,rank:str,weapon:Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon
    def report(self):
        print(f"The soldier name: {self.name} \n Is rank: {self.rank} \n His weapon: {self.weapon.name} {self.weapon.ammo}")

class Unit(ABC):
    def __init__(self,unit_name:str,commander:Solider,soldiers:list[Solider],strike_option:list):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers
        self.strike_option = strike_option

    def briefing(self):
        print(f'The unit name: {self.unit_name}')
        self.commander.report()

    @abstractmethod
    def attack(self):
        pass

class Infantry(Unit):
    def attack(self):
        print("infantry unit attack")

class TankUnit(Unit):
    def attack(self):
        print("tank unit attack")

class Sniper(Unit):
    def attack(self):
        print("sniper unit attack")


