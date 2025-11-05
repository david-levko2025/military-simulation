from lessens_exersice_in_the_army.week3.day4.military_simulation.army_inventory import Unit

class Army:
    total_attacks = 0
    def __init__(self,units:list[Unit]):
        self.units = units

    def attack_all(self):
        for i in self.units:
            i.attack()
            Army.total_attacks += 1