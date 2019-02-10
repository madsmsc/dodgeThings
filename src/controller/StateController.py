from src.model.Enemy import Enemy
from src.model.Player import Player
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
