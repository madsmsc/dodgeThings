from src.LootController import Loot
from src.Char import Node

class MapController:
    __instance = None

    loot: [Loot] = []
    enemies: [Node] = []

    @staticmethod
    def getInstance():
        if MapController.__instance is None:
            MapController.__instance = MapController()
        return MapController.__instance

    def addLoot(self, loot: [Loot]):
        self.loot.append(loot)

    def addEnemy(self, enemy: Node):
        self.enemies.append(enemy)
