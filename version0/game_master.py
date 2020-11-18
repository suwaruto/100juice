# Game master is a ruler of game logic, map and creatures. An omnipotent being.
import dynamic
import random

class GameMaster(object):
    
    def __init__(self, Map):
        self._Map = Map
        self._players = []
        self._npcs = []
        self.running = True

    def RegisterCreature(self, creature):
        x = creature._x
        if type(creature) is dynamic.Player:
            self._players += [creature]
        else:
           self._npcs += [creature]
        self._Map.PlaceCreature(creature, x)

    def ThrowDice(self, dice):
        return dice[0] * random.randint(1, dice[1])
    
    def GetPlayers(self):
        return self._players

    def GetStatus(self):
        s = "Players:\n"
        for player in self._players:
            s += player._name + ": x = " + str(player._x) + '\n'
            s += "hp = " + str(player._hp) + '\n'
        return s

    def GetTileStatus(self, x, y = 0):
        status = "Creatures on the {0} tile are:\n".format(x)
        for i in range(len(self._Map._field[x]._childs)):
            status += str(i) + " | " + self._Map._field[x]._childs[i]._name + '\n'
        return status

    def MoveCreature(self, creature, dx, dy = 0):
        if not self._Map.MoveCreature(creature, creature._x + dx, creature._y + dy):
            print(creature._name + ": Encountered enemies!")
            print(self.GetTileStatus(creature._x, creature._y))
            action_id = creature.QueryAction()
            if action_id == 0:
                pass
            elif action_id == 1:
                self.AttackCreature(creature, self._Map._field[creature._x]._childs[creature.QueryAction()])
            else:
                pass

    def AttackCreature(self, attacker, defender):
        if self.ThrowDice((1, 20)) > defender._ac:
            dmg = self.ThrowDice(attacker._attack)
            print(attacker._name + " hitted " + defender._name + " for {0} hp!".format(dmg))
            defender._hp -= dmg
            defender.OnAttack()
        else:
            print("Miss!")

    def PerformAction(self, action_id, creature, *args):
        if action_id == 0:
            steps = self.ThrowDice(creature._velocity)
            print("Moving {0} steps ahead".format(steps))
            for i in range(1, steps):
                self.MoveCreature(creature, 1) 
        elif action_id == 1:
            pass
        else:
            pass
