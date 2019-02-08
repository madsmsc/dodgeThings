
class LootController:
    invSize: int, int = (10, 5)
    inventory: [Loot][Loot] = [invSize[0]][invSize[1]]
    
    class Loot:
        amount: int = 1
        stackSize: int = 0
        name: str = ''
        desc: str = ''
        dropChance: float = 0 # [0, 100]

    class Item(Loot):
        scrappable: bool = True

    class Currency(Loot):
        stackSize: int = 20

    class Identify(Currency):
        name = 'Scroll of identify'
        desc = 'Reveals the properties of an item'
        dropChance = 20

    class Portal(Currency):
        name = 'Portal scroll'
        desc = 'Opens transportation device to your currenct base'
        dropChance = 15

    class MakeGreen(Currency):
        name = 'Scroll of elders'
        desc = 'Convert any item to uncommen rarity'
        dropChance = 10

    class RandomRarity(Currency):
        name = 'Tome of luck'
        desc = 'Convert any item to a random rarity'
        dropChance = 6

    class MakeBlue(Currency):
        name = 'Hidden tome'
        desc = 'Convert any item to rare rarity'
        dropChance = 6

    class RerollBlue(Currency):
        name = 'Forgotten scroll'
        desc = 'Roll new modifiers for an rare item'
        dropChance = 4

    class MakeYellow(Currency):
        name = 'Ancient tome'
        desc = 'Convert any item to ancient rarity'
        dropChance = 2

    class RerollYellow(Currency):
        name = 'Roll new modifiers for an ancient item'
        dropChance = 1

    currencies = [Identify, Portal, MakeGreen, RandomRarity,
                  MakeBlue, RerollBlue, MakeYellow, RerollYellow]

    def levelMult(self, level: int) -> int:
        if level < -5:
            return 0
        if level > 5:
            return 5
        return {
            -5: 0.1
            -4: 0.2
            -3: 0.4
            -2: 0.6
            -1: 0.8
            0: 1.0
            1: 1.2
            2: 1.5
            3: 1.8
            4: 2.0
            5: 3.0
        }.get(level, 0)

    def roll(level: int) -> Currency:
        drops = []
        float rolls = Random.Range(0, 100) * levelMult(level)
        for i in range(0, int(rolls / 100)):
            float random = Random.Range(0, 100);
            for currency in currencies:
                if random >= 100 - currency.dropChance:
                    print('dropping currency')
                    drops.append(
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
