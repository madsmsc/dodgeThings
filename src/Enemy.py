import ?

class Enemy{
    moveSpeed: float = 0
    attackSpeed: float = 0
    expWorth: int = 0
    maxHealth: int = 0
    currentHealth: int = 0
    damage: int = 0
    hitCooldown: float = 0
    level: int = 0 # determines the mob level
    lootRolls: int = 0 # determines the "difficulty/rarity" of the mob [0=common, 1=uncommon, 2=rare, 3=epic]

    class Rarity(Enum):
        COMMON = 1
        UNCOMMON = 2
        RARE = 3
        EPIC = 4

    class MobType(Enum):
        SLOW = 1
        FAST = 2

    def __init__(self, type: self.MobType):
        if type == self.MobType.SLOW
          makeSlowMob()
        elif type == self.MobType.FAST
          makeFastMob()
        else
          print('fail...')

    def makeSlowMob():
        self.moveSpeed = 1
        self.attackSpeed = 1
        self.expWorth = 10
        self.maxHealth = 10
        self.currentHealth = 10
        self.damage = 1
        self.level = 1
        self.rarity = self.Rarity.COMMON
        self.mobType = self.MobType.SLOW

    private void FixedUpdate() {
        transform.LookAt(player.transform.position);
        if (currentHealth <= 0) {
            die();
        }
        rigidBody.velocity = transform.forward * moveSpeed;
    }

    private void die() {
        dropLoot();
        # set dead flag and render as dead mob
    }

    private void dropLoot() {
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
    }

    public void hurtEnemy(int damage) {
        currentHealth -= damage;
        healthBar.fillAmount = (float)currentHealth / (float)maxHealth;
    }
}

