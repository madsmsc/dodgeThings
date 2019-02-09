from src.model.Char import Char
from src.model.Vector import Vector

class Player(Char):
    moveTo: Vector = None
    powerGainTime: int = 0
    maxPowerGainTime: int = 100

    def __init__(self,  pos: (int, int) = (0, 0)):
        super().__init__(pos)
        self.moveSpeed = 2
        self.attackSpeed = 1
        self.maxHealth = 20
        self.curHealth = self.maxHealth
        self.maxPower = 10
        self.curPower = self.maxPower
        self.damage = 1
        self.level = 1

    def update(self):
        if self.moveTo is not None:
            self.move(self.moveTo)
        self.powerGain()

    def powerGain(self):
        if self.curPower >= self.maxPower:
            return
        if self.powerGainTime < self.maxPowerGainTime:
            self.powerGainTime += 1
        else:
            self.powerGainTime = 0
            self.curPower += 1
