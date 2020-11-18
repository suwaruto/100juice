def str_list(lst, starting_index = 0):
    res = ""
    for i in range(len(lst)):
        res += str(i + starting_index) + ": " + str(lst[i]) 
        
class Dynamic(object):
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

class Creature(Dynamic):
    
    def __init__(self, x, y, hp, inventory = []):
        Dynamic.__init__(self, x, y)
        self._hp = hp
        self._inventory = inventory
        self._velocity = (1, 4) # tuple[0] d tuple[1]
        self._ac = 10
        self._attack = (1, 4)

    def OnMove(self, x, y, ind):
        self._x = x
        self._y = y
        self._ind = ind

    def OnKill(self, creature):
        self._inventory += creature.GetInventory()

    def OnDeath(self):
        self.__del__()

    def OnAttack(self):
        if self._hp <= 0:
            self.OnDeath()     

    def GetInventory(self):
        return self._inventory

class Player(Creature):
    
    def __init__(self, x, y, hp, name, inventory = [], points = 0):
        Creature.__init__(self, x, y, hp, inventory)
        self._points = points
        self._active = True
        self._name = name

    def OnDeath(self):
       self._active = False 
       self._inventory = []

    def QueryAction(self):
        return int(input(self._name + ": What action would you like to perform? "))
        
    def IsActive(self):
        return self._active
