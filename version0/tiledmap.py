class Tile(object):
    
    def __init__(self):
        self._childs = []

class CircularTileMap(object):
    
    def __init__(self, length):
        self._length = length
        self._field = [Tile() for i in range(length)]
        self._visfield = [0 for i in range(length)] 

    def PlaceCreature(self, creature, x, y = 0):
        self._field[x % self._length]._childs += [creature]
        creature.OnMove(x, y, len(self._field[x % self._length]._childs) - 1)
        
    def MoveCreature(self, creature, x, y = 0):
        del self._field[creature._x % self._length]._childs[creature._ind]
        for ind in range(len(self._field[creature._x % self._length]._childs)):
            self._field[creature._x % self._length]._childs[ind]._ind = ind
        res = (len(self._field[x % self._length]._childs) == 0)
        self._field[x % self._length]._childs += [creature]
        creature.OnMove(x % self._length, y, len(self._field[x % self._length]._childs) - 1)
        return res

    def RemoveCreature(self, creature):
        del self._field[creature._x % self._length]._childs[creature._ind]
        for ind in range(len(self._field[creature._x % self._length]._childs)):
            self._field[creature._x % self._length]._childs[ind]._ind = ind
        creature.OnDeath()
