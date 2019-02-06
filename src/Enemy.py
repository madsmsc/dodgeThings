from enum import Enum
from src.Node import Node
from src.Player import Player
from src.Vector import Vector

class Enemy(Node):
    class Rarity(Enum):
        COMMON = 1
        UNCOMMON = 2
        RARE = 3
        EPIC = 4

    class MobType(Enum):
        SLOW = 1
        FAST = 2

    rarity: int = 0
    mobType: MobType = 1
    expWorth: int = 0

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
        self.maxHealth = 10
        self.currentHealth = 10
        self.damage = 1
        self.level = 1
        self.rarity = self.Rarity.COMMON
        self.mobType = self.MobType.SLOW

    def makeFastMob(self):
        self.moveSpeed = 0.7
        self.attackSpeed = 1
        self.expWorth = 20
        self.maxHealth = 10
        self.currentHealth = 10
        self.damage = 1
        self.level = 1
        self.rarity = self.Rarity.COMMON
        self.mobType = self.MobType.FAST

    def update(self, player: Player, tick: float):
        if self.currentHealth <= 0:
            self.die()
        if self.hitCooldown > 0:
            self.hitCooldown -= tick
        self.move(player.pos)

    def die(self):
        self.dropLoot()
        # set dead flag and render as dead mob

    def dropLoot(self):
        pass
        """
        playerLevel.currentXP += expWorth;
        for (int i = 0; i < lootRolls; i++) {
            Currency c = lootController.roll(level - playerLevel.level);
            if (c != null) {
                float x = c.transform.position.x + transform.position.x;
                float z = c.transform.position.z + transform.position.z;
                c.transform.position = new Vector3(x, -0.9f, z);
                c.itemName = c.type.ToString();
                c.transform.parent = lootController.lootPool.transform;
                //Debug.Log("dropped loot! "+c.type);
            } else {
                //Debug.Log("didn't drop loot :(");
            }
        }
        """

    def doDamage(self) -> int:
        if self.hitCooldown <= 0:
            self.hitCooldown = self.attackSpeed
            return self.damage
        return 0

    def takeDamage(self, amount: int):
        self.currentHealth -= amount
