from src.Char import Char
from src.Vector import Vector

class Player(Char):
    moveTo: Vector = None

    def __init__(self,  pos: (int, int) = (0, 0)):
        super().__init__(pos)
        self.moveSpeed = 2
        self.attackSpeed = 1
        self.maxHealth = 20
        self.currentHealth = 20
        self.damage = 1
        self.level = 1

    def update(self):
        if self.moveTo is not None:
            self.move(self.moveTo)
