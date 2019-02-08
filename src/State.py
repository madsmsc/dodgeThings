from src.Enemy import Enemy
from src.Player import Player
from src.Util import Const

class State:
    player: Player = None
    enemies = []

    def __init__(self):
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
            dist = self.player.pos.distance_to(enemy.pos)
            if dist < Const.WIN_DIST:
                self.player.currentHealth -= enemy.doDamage()
