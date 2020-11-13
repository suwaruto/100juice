# Game master is a ruler of game logic, map and creatures. An omnipotent being.
import dynamic

class GameMaster(object):
    
    def __init__(self, Map):
        self._Map = Map
        self._players = []
        self._npcs = []
        self.running = True
        self._Actions = [self.MoveCreature]

    def RegisterCreature(self, creature):
        x = creature._x
        if type(creature) is dynamic.Player:
            self._players += [creature]
        else:
           self._npcs += [creature]
        self._Map.PlaceCreature(creature, x)
    
    def MoveCreature(self, creature, x):
        self._Map.MoveCreature(creature, x)

    def GetPlayers(self):
        return self._players

    def GetStatus(self):
        s = "Players:\n"
        for player in self._players:
            s += player._name + ": x = " + str(player._x) + '\n'
        return s

    def PerformAction(self, action_id, creature, *args):
        self.MoveCreature(creature, *args) 
