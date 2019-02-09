from src.controller.LootController import Loot
from src.model.Char import Node
from src.Util import Const
from src.controller.Singleton import Singleton
import random


class MapController(Singleton):
    loot: [Loot] = []
    enemies: [Node] = []

    def addLoot(self, loot: [Loot]):
        self.loot.append(loot)

    def addEnemy(self, enemy: Node):
        self.enemies.append(enemy)

    blocksize = 0
    blocks = 0

    colors = list({
        'green': (100, 170, 100),
        'blue': (100, 100, 170),
        'red': (170, 100, 100)
    }.values())
    map = [[]]

    def makeMap(self):
        self.blocksize = 30
        winSize = Const.WINDOW[0]
        self.blocks = int(winSize / 30) + 1
        for x in range(self.blocks):
            self.map.append([])
            for y in range(self.blocks):
                self.map[x].append(random.choice(self.colors))
