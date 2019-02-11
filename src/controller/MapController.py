from src.controller.LootController import Loot
from src.model.Char import Node
import random


class MapController:
    __instance = None

    @staticmethod
    def getInstance():
        if MapController.__instance is None:
            MapController.__instance = MapController()
        return MapController.__instance

    loot: [Loot] = []
    enemies: [Node] = []

    def addLoot(self, loot: [Loot]):
        self.loot.append(loot)

    def addEnemy(self, enemy: Node):
        self.enemies.append(enemy)

    blocksize = 0
    blocks = 0

    colors = [10, 11, 12, 13, 14, 15, 16, 17, 18]
    map = [[]]

    def makeMap(self):
        xSize = 12
        ySize = 48
        for x in range(0, xSize):
            self.map.append([])
            for y in range(0, ySize):
                self.map[x].append(random.choice(self.colors))
