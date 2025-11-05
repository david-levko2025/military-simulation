from army_inventory import Unit
from main import i1
class Agent:
    def __init__(self,codename:str,clearance_level:int):
        self.codename = codename
        self.clearance_level = clearance_level

class Mission:
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
class RecoMission:
    def execute(self):
        pass
class StrikeMission:
    def execute(self):
        pass
class RescueMission:
    def execute(self):
        pass