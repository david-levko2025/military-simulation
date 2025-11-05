from lessens_exersice_in_the_army.week3.day4.military_simulation.army_inventory import Solider


class Commander(Solider):
    def __init__(self,name,weapon):
        super().__init__(name,"commander",weapon)