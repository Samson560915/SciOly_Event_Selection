from utils import dot_product, avr_lists

import math

class Player:
    # Life, Personal & Social Science
    anatomy              = (0.9, 0.6, 0.2, 0.0, 0.0, 0.0, 0.1, 0.2)
    astronomy            = (0.0, 0.0, 0.1, 0.9, 0.0, 0.1, 0.5, 0.2)
    boomilever           = (0.0, 0.0, 0.0, 0.7, 1.0, 0.0, 0.4, 1.0)
    botany               = (0.1, 0.9, 0.2, 0.0, 0.0, 0.0, 0.1, 0.3)
    chemistry_lab        = (0.0, 0.0, 1.0, 0.3, 0.0, 0.0, 0.5, 0.8)
    circuit_lab          = (0.0, 0.0, 0.1, 0.9, 0.6, 0.0, 0.4, 0.9)
    codebusters          = (0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.8, 0.1)
    designer_genes       = (0.3, 0.9, 0.3, 0.0, 0.0, 0.0, 0.3, 0.3)
    disease_detectives   = (0.7, 0.6, 0.1, 0.0, 0.0, 0.0, 0.5, 0.2)
    dynamic_planet       = (0.0, 0.2, 0.3, 0.4, 0.0, 0.0, 0.3, 0.2)
    electric_vehicle     = (0.0, 0.0, 0.1, 0.8, 1.0, 0.1, 0.4, 1.0)
    engineering_cad      = (0.0, 0.0, 0.0, 0.3, 0.9, 0.2, 0.5, 0.6)
    experimental_design  = (0.1, 0.3, 0.3, 0.3, 0.1, 0.0, 0.6, 0.7)
    forensics            = (0.2, 0.3, 0.7, 0.2, 0.0, 0.0, 0.3, 0.7)
    hovercraft           = (0.0, 0.0, 0.0, 0.8, 1.0, 0.0, 0.3, 1.0)
    mission_possible     = (0.0, 0.0, 0.1, 0.7, 1.0, 0.0, 0.2, 1.0)
    ping_pong_parachute  = (0.0, 0.0, 0.1, 0.8, 0.8, 0.0, 0.3, 1.0)
    protein_modeling     = (0.3, 0.8, 0.5, 0.1, 0.2, 0.1, 0.2, 0.7)
    remote_sensing       = (0.0, 0.2, 0.1, 0.4, 0.1, 0.4, 0.5, 0.3)
    rocks_and_minerals   = (0.0, 0.0, 0.5, 0.2, 0.0, 0.0, 0.1, 0.5)
    thermodynamics       = (0.0, 0.0, 0.3, 1.0, 0.6, 0.0, 0.5, 0.8)
    water_quality        = (0.0, 0.6, 0.5, 0.1, 0.0, 0.0, 0.3, 0.3)
    wright_stuff         = (0.0, 0.0, 0.0, 0.9, 0.8, 0.0, 0.3, 1.0)

    times = {
    "Anatomy and Physiology": 1,
    "Botany": 3,
    "Designer Genes": 6,
    "Disease Detectives": 2,
    "Water Quality": 5,
    "Astronomy": 3,
    "Dynamic Planet": 6,
    "Remote Sensing": 2,
    "Rocks and Minerals": 4,
    "Chemistry Lab": 4,
    "Circuit Lab": 5,
    "Forensics": 1,
    "Hovercraft": 0,
    "Protein Modeling": 5,
    "Thermodynamics": 6,
    "Boomilever": 0,
    "Electric Vehicle": 0,
    "Mission Possible": 0,
    "Wright Stuff": 0,
    "Codebusters": 2,
    "Engineering CAD": 1,
    "Experimental Design": 3,
    "Ping-Pong Parachute": 0
    }

    events = {
        "Anatomy and Physiology": anatomy,
        "Botany": botany,
        "Designer Genes": designer_genes,
        "Disease Detectives": disease_detectives,
        "Water Quality": water_quality,
        "Astronomy": astronomy,
        "Dynamic Planet": dynamic_planet,
        "Remote Sensing": remote_sensing,
        "Rocks and Minerals": rocks_and_minerals,
        "Chemistry Lab": chemistry_lab,
        "Circuit Lab": circuit_lab,
        "Forensics": forensics,
        "Hovercraft": hovercraft,
        "Protein Modeling": protein_modeling,
        "Thermodynamics": thermodynamics,
        "Boomilever": boomilever,
        "Electric Vehicle": electric_vehicle,
        "Mission Possible": mission_possible,
        "Wright Stuff": wright_stuff,
        "Codebusters": codebusters,
        "Engineering CAD": engineering_cad,
        "Experimental Design": experimental_design,
        "Ping-Pong Parachute": ping_pong_parachute
        }
    

    def __init__(self, name, picks, grade, e1 = None, e2 = None, e3 = None, e4 = None):
        self.name = name
        self.grade = grade
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.e4 = e4
        self.picks = set(picks)
        self.avr = avr_lists(picks)
        temp_dot = {}
        self.softmax = {}
        total = 0
        for i,j in Player.events.items():
            temp = dot_product(self.avr, j)
            temp_dot = temp_dot | {i: temp}
            total += math.exp(temp)
        for i,j in temp_dot.items():
            self.softmax = self.softmax | {i: math.exp(j)/total}

    def add_event(self, event):
        if self.e1 is None:
            self.e1 = event
            return True
        
        if self.e2 is None:
            self.e2 = event
            return True
        
        if self.e3 is None:
            self.e3 = event
            return True
        
        if self.e4 is None:
            self.e4 = event
            return True
        
        return False

    def get_event_happiness(self, event):
        val = 0
        if self.e3 is not None:
            val -= 0.5
        if self.e4 is not None:
            val -= 5
        if Player.times.get(event) != 0 and (Player.times.get(self.e1) == Player.times.get(event) or Player.times.get(self.e2) == Player.times.get(event) or Player.times.get(self.e3) == Player.times.get(event)):
            val -= 5
        if tuple(Player.events.get(event)) in self.picks:
            val += 1
        
        return self.softmax.get(event) + val
    
    def get_player_happiness(self):
        happiness = 0
        count = 2
        if Player.events.get(self.e1) in self.picks:
            happiness += 1
        else:
            happiness += self.softmax.get(self.e1)

        if Player.events.get(self.e2) in self.picks:
            happiness += 1
        else:
            happiness += self.softmax.get(self.e2)

        if self.e3 is not None:
            if Player.events.get(self.e3) in self.picks:
                happiness += 1
            else:
                happiness += self.softmax.get(self.e3)
            count += 1

        if self.e4 is not None:
            if Player.events.get(self.e4) in self.picks:
                happiness += 1
            else:
                happiness += self.softmax.get(self.e4)
            happiness -= 0.6 #We don't want people with more than three events
            count += 1

        return happiness/count

    def __lt__(self, other):
        return self

        
        
        