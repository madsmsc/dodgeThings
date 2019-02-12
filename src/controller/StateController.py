from src.model.Enemy import Enemy
from src.model.Player import Player
from src.model.Map import Map
from src.Util import Const
from src.controller.LootController import LootController, Currency, Loot

class StateController:
    __instance = None

    @staticmethod
    def getInstance():
        if StateController.__instance is None:
            StateController.__instance = StateController()
        return StateController.__instance

    lc = LootController.getInstance()
    player: Player = None
    enemies = []
    deadEnemies = []
    map: [[int]] = []
    loot: [Loot] = []


    def setup(self):
        self.player = Player((500, 300))
        self.enemies.append(Enemy(Enemy.MobType.SLOW, (100, 250)))
        self.enemies.append(Enemy(Enemy.MobType.SLOW, (60, 220)))
        self.enemies.append(Enemy(Enemy.MobType.SLOW, (400, 420)))
        self.enemies.append(Enemy(Enemy.MobType.SLOW, (360, 380)))
        self.enemies.append(Enemy(Enemy.MobType.SLOW, (220, 300)))

    def update(self, tick: float):
        self.player.update()
        for enemy in self.enemies:
            enemy.update(self.player, tick)
            if enemy.dead:
                self.enemies.remove(enemy)
                self.deadEnemies.append(enemy)
                # drop loot
                c: [Currency] = self.lc.roll(enemy.level)
                self.loot.append(c)
            dist = self.player.pos.distance_to(enemy.pos)
            if dist < Const.WIN_DIST:
                self.player.curHealth -= enemy.doDamage()

    def enemiesTakeNovaDamage(self, radius: int, amount: int):
        for enemy in self.enemies:
            dist = self.player.pos.distance_to(enemy.pos)
            if dist < radius:
                enemy.takeDamage(amount)

    def makeMap(self):
        xSize = 12 * 4
        ySize = 48 * 2
        m = Map()
        m.generateMap(xSize, ySize)
        m.placeTreasure()
        m.printMap()

        for x in range(0, xSize):
            self.map.append([])
            for y in range(0, ySize):
                self.addTileToMap(m, x, y)


    def addTileToMap(self, m, x, y):
        PLAIN = 20
        EMPTY = 40
        GRASS = 6 * 16 + 1
        if m.isTreasure((x, y)):
            self.map[x].append(GRASS)
        elif m.cellmap[x][y]:
            self.map[x].append(PLAIN)
        else:
            self.map[x].append(EMPTY)
