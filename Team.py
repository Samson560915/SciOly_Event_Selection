from Player import Player
import heapq


class Team:
    def __init__(self, list_of_players=[]):
        self.players = set(list_of_players)
        self.events = {
            "Anatomy and Physiology": 2,
            "Botany": 2,
            "Designer Genes": 2,
            "Disease Detectives": 2,
            "Water Quality": 2,
            "Astronomy": 2,
            "Dynamic Planet": 2,
            "Remote Sensing": 2,
            "Rocks and Minerals": 2,
            "Chemistry Lab": 2,
            "Circuit Lab": 2,
            "Forensics": 2,
            "Hovercraft": 2,
            "Protein Modeling": 2,
            "Thermodynamics": 2,
            "Boomilever": 2,
            "Electric Vehicle": 2,
            "Mission Possible": 2,
            "Wright Stuff": 2,
            "Codebusters": 3,
            "Engineering CAD": 2,
            "Experimental Design": 3,
            "Ping-Pong Parachute": 2
            }
        self.events_people = { #holds people NAMES
            "Anatomy and Physiology": [],
            "Botany": [],
            "Designer Genes": [],
            "Disease Detectives": [],
            "Water Quality": [],
            "Astronomy": [],
            "Dynamic Planet": [],
            "Remote Sensing": [],
            "Rocks and Minerals": [],
            "Chemistry Lab": [],
            "Circuit Lab": [],
            "Forensics": [],
            "Hovercraft": [],
            "Protein Modeling": [],
            "Thermodynamics": [],
            "Boomilever": [],
            "Electric Vehicle": [],
            "Mission Possible": [],
            "Wright Stuff": [],
            "Codebusters": [],
            "Engineering CAD": [],
            "Experimental Design": [],
            "Ping-Pong Parachute": []
            }
        self.events_players = { #holds player values
            "Anatomy and Physiology": [],
            "Botany": [],
            "Designer Genes": [],
            "Disease Detectives": [],
            "Water Quality": [],
            "Astronomy": [],
            "Dynamic Planet": [],
            "Remote Sensing": [],
            "Rocks and Minerals": [],
            "Chemistry Lab": [],
            "Circuit Lab": [],
            "Forensics": [],
            "Hovercraft": [],
            "Protein Modeling": [],
            "Thermodynamics": [],
            "Boomilever": [],
            "Electric Vehicle": [],
            "Mission Possible": [],
            "Wright Stuff": [],
            "Codebusters": [],
            "Engineering CAD": [],
            "Experimental Design": [],
            "Ping-Pong Parachute": []
            }
        self.number_of_seniors = 0

    def get_score(self):
        total = 0
        for p in self.players:
            total += p.get_player_happiness()
        return total

    def add_player(self, p):
        self.players.add(p)

    def decrease_event(self, p, e):
        if self.events.get(e) < 1:
            return False
        else:
            self.events[e] -= 1
            self.events_people[e].append(p.name)
            self.events_players[e].append(p)
            p.add_event(e)
            return True

    def add_and_decrease(self, p, e):
        if len(self.players) >= 15 and p not in self.players or p in set(self.events_people.get(e)) or p.grade == 12 and self.number_of_seniors > 6:
            return False
        if p.grade == 12:
            self.number_of_seniors += 1
        self.add_player(p)
        self.decrease_event(p, e)
        return True

    def finish_events(self):
        for key, value in self.events.items():
            tiebreak = 0
            if value != 0:
                pq = []
                for p in (self.players - set(tuple(self.events_players.get(key)))):
                    heapq.heappush(pq,(-p.get_event_happiness(key), tiebreak, p))
                    tiebreak += 1
                while self.events.get(key) != 0:
                    self.decrease_event(heapq.heappop(pq)[2], key)

    def __str__(self):
        return(f"{self.events_people}")

                    