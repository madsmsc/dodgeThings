from enum import Enum
from src.model.Char import Char
from src.model.Player import Player
from src.controller.LootController import LootController, Currency, Rarity
from src.controller.MapController import MapController

class Enemy(Char):
    class MobType(Enum):
        SLOW = 1
        FAST = 2

    rarity: int = 0
    mobType: MobType = 1
    expWorth: int = 0
    dead: bool = False

    def __init__(self, mobType: MobType, pos: (int, int) = (0, 0)):
        super().__init__(pos)
        if mobType == self.MobType.SLOW:
            self.makeSlowMob()
        elif mobType == self.MobType.FAST:
            self.makeFastMob()
        else:
            print('fail...')

    def makeSlowMob(self):
        self.moveSpeed = 0.2
        self.attackSpeed = 2
        self.expWorth = 10
        self.maxHealth = 5
        self.curHealth = self.maxHealth
        self.damage = 1
        self.level = 1
        self.rarity = Rarity.COMMON
        self.mobType = self.MobType.SLOW

    def makeFastMob(self):
        self.moveSpeed = 0.7
        self.attackSpeed = 1
        self.expWorth = 20
        self.maxHealth = 5
        self.curHealth = self.maxHealth
        self.damage = 1
        self.level = 1
        self.rarity = Rarity.COMMON
        self.mobType = self.MobType.FAST

    def update(self, player: Player, tick: float):
        if self.curHealth <= 0:
            self.die()
        if self.hitCooldown > 0:
            self.hitCooldown -= tick
        self.move(player.pos)

    def die(self):
        self.dead = True
        lc = LootController.getInstance()
        loot: [Currency] = lc.roll(self.level)
        mc = MapController.getInstance()
        mc.addLoot(loot)

    def doDamage(self) -> int:
        if self.hitCooldown <= 0:
            self.hitCooldown = self.attackSpeed
            return self.damage
        return 0

    def takeDamage(self, amount: int):
        self.curHealth -= amount
