from random import Random
from src.model.Vector import Vector
from enum import Enum

class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    ANCIENT = 4

class Loot:
    pos: Vector = Vector((0, 0))
    amount: int = 1
    stackSize: int = 0
    name: str = ''
    desc: str = ''
    dropChance: float = 0  # [0, 100]

class Item(Loot):
    scrappable: bool = True

class Currency(Loot):
    def __init__(self, name: str, desc: str, dropChance: int):
        self.stackSize: int = 20
        self.name = name
        self.desc = desc
        self.dropChance = dropChance

class Identify(Currency):
    def __init__(self):
        super().__init__('Scroll of identify', 'Reveals the properties of an item', 20)

class Portal(Currency):
    def __init__(self):
        super().__init__('Portal scroll', 'Opens transportation device to your currenct base', 15)

class MakeGreen(Currency):
    def __init__(self):
        super().__init__('Scroll of elders', 'Convert any item to uncommen rarity', 10)

class RandomRarity(Currency):
    def __init__(self):
        super().__init__('Tome of luck', 'Convert any item to a random rarity', 6)

class MakeBlue(Currency):
    def __init__(self):
        super().__init__('Hidden tome', 'Convert any item to rare rarity', 6)

class RerollBlue(Currency):
    def __init__(self):
        super().__init__('Forgotten scroll', 'Roll new modifiers for an rare item', 4)

class MakeYellow(Currency):
    def __init__(self):
        super().__init__('Ancient scroll', 'Convert any item to ancient rarity', 2)

class RerollYellow(Currency):
    def __init__(self):
        super().__init__('Ancient tome', 'Roll new modifiers for an ancient item', 1)

class LootController:
    __instance = None

    @staticmethod
    def getInstance():
        if LootController.__instance is None:
            LootController.__instance = LootController()
        return LootController.__instance

    inventory: [[Loot]] = [[None for x in range(10)] for y in range(5)]

    currencies = [Identify, Portal, MakeGreen, RandomRarity,
                  MakeBlue, RerollBlue, MakeYellow, RerollYellow]

    levelMultMap = {
     -5: 0.1,
     -4: 0.2,
     -3: 0.4,
     -2: 0.6,
     -1: 0.8,
     0: 1.0,
     1: 1.2,
     2: 1.5,
     3: 1.8,
     4: 2.0,
     5: 3.0}

    def levelMult(self, level: int) -> int:
        if level < -5:
            return 0
        if level > 5:
            return 5
        return self.levelMultMap.get(level, 0)

    def roll(self, level: int) -> [Currency]:
        drops = []
        r = Random()
        rolls = r.randint(0, 100) * self.levelMult(level)
        for i in range(0, int(rolls / 100)):
            roll = r.randint(0, 100)
            for currency in self.currencies:
                if roll >= 100 - currency.dropChance:
                    print('dropping currency')
                    drops.append(currency())
        return drops
                        
"""
make a poolController that can instantiate all objects for me
  and it holds lists of objects that it recycles.
  it will have methods for instantiating:
  bullets, drops, enemies, map cells, etc.

what about the skills/abilities? the number should scale with rarity

# standard white mob drops:
item                     chance   upgrade
-----------------------------------------
identify item        	 40	      256
town portal	     	 20	      128
make item green	     	 10	      64
reroll green	     	 6	      32
add second stat	     	 5	      16	
make item random rarity	 4	      8
make item blue	     	 3	      4
make item yellow	 2	      2
reroll yellow		 1	      1 


# roll bonus pr mob level compared to you:
level diff     	multiplier
----------------------------------
-5			    0.1
-4			    0.2
-3			    0.4
-2			    0.6
-1			    0.8
0			    1.0
1			    1.2
2			    1.5
3			    1.8
4			    2.0
5			    3.0 


# item rarity:
type			affixes
-------------------------------
white			0
green			1
blue			2
yellow			3 

"""
