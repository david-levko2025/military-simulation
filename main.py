from lessens_exersice_in_the_army.week3.day4.military_simulation.army_inventory import Solider,Weapon,Infantry,Sniper,TankUnit
from lessens_exersice_in_the_army.week3.day4.military_simulation.strike_options import Tank,Drone
from lessens_exersice_in_the_army.week3.day4.military_simulation.Battle_Simulation import Army

a1 = Tank("mercava 1", 25)
a2 = Tank("carmel", 100)
a3 = Tank("mercava siman 4", 85)
b1 = Drone("F-16", 900)
b2 = Drone("mig2", 1000)
b3 = Drone("b-2", 3000)
lst = [a1, a2, a3, b1, b2, b3]
c1 = Weapon("scar-l", 300)
c2 = Weapon("kar98k", 30)
c3 = Weapon("ump-45", 200)
c4 = Weapon("m-762", 250)
d1 = Solider("meir", "colonel", c2)
d2 = Solider("david", "rabat", c1)
d3 = Solider("ariel", "seren", c3)
d4 = Solider("moshe", "mefaked", c4)
soldiers = [d1, d2, d3]
s1 = Sniper("kodkod", d3, soldiers, lst)
i1 = Infantry("golani",d4,soldiers,lst)
t1 = TankUnit("miara",d2,soldiers,lst)

vv = Army([s1,i1,t1])
vv.attack_all()



