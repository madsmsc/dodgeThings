from src.model.Enemy import Enemy
from src.model.Player import Player
from src.model.Map import Map
from src.Util import Const

class StateController:
    __instance = None

    @staticmethod
    def getInstance():
        if StateController.__instance is None:
            StateController.__instance = StateController()
        return StateController.__instance

    player: Player = None
    enemies = []
    deadEnemies = []

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
            dist = self.player.pos.distance_to(enemy.pos)
            if dist < Const.WIN_DIST:
                self.player.curHealth -= enemy.doDamage()

    def enemiesTakeNovaDamage(self, radius: int, amount: int):
        for enemy in self.enemies:
            dist = self.player.pos.distance_to(enemy.pos)
            if dist < radius:
                enemy.takeDamage(amount)

    #colors = [10, 11, 12, 13, 14, 15, 16, 17, 18]
    map = [[]]
    EMPTY = 42
    PLAIN = 20

    def makeMap(self):
        xSize = 12
        ySize = 48
        tiles = Map()
        tiles.generateMap(xSize, ySize)
        tiles.placeTreasure()
        #tiles.printMap()

        for x in range(0, xSize):
            self.map.append([])
            for y in range(0, ySize):
                if tiles.cellmap[x][y]:
                    self.map[x].append(self.PLAIN)
                else:
                    self.map[x].append(self.EMPTY)
