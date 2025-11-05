from army_inventory import Unit
from lessens_exersice_in_the_army.week3.day4.military_simulation.army_inventory import Infantry, TankUnit, Sniper
from lessens_exersice_in_the_army.week3.day4.military_simulation.strike_options import Drone,Tank
from main import i1,b1,t1,b2,s1,a1
from abc import ABC
class Agent:
    def __init__(self,codename:str,clearance_level:int):
        self.codename = codename
        self.clearance_level = clearance_level

class Mission(ABC):
    def __init__(self,mission_name:str, target:str, assigned_agent:Agent,assigned_unit:Unit):
        self.mission_name = mission_name
        self.target = target
        self.assigned_agent = assigned_agent
        self.unit = assigned_unit

    def briefing(self):
        print(f"---mission---"
              f"The name of the mission: {self.mission_name}"
              f"the target: {self.target}"
              f"the assigned_agent: {self.assigned_agent.codename}")

class MissionManager:
    def __init__(self):
        self.missions = []

    def add_missions(self,mission):
        self.missions.append(mission)
        return self.missions

    def remove_missions(self,mission):
        self.missions.remove(mission)
        return self.missions

agent1 = Agent("007",1)
mission_to_unit = Mission("mivcha antebe","Uganda",agent1,i1)

class RecoMission(Mission):
    def execute(self):
        Drone.strike(b1),Sniper.attack(s1)

class StrikeMission(Mission):
    def execute(self):
        TankUnit.attack(t1),Drone.strike(b2)

class RescueMission(Mission):
    def execute(self):
        Infantry.attack(i1),Tank.strike(a1)
