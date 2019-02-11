from src.model.Vector import Vector
from src.Util import Const
from src.model.Node import Node

class Char(Node):
    moveSpeed: float = 0
    attackSpeed: float = 0
    maxHealth: int = 0
    curHealth: int = 0
    maxPower: int = 0
    curPower: int = 0
    damage: int = 0
    hitCooldown: float = 0
    level: int = 0

    def __init__(self, pos: (int, int) = (0, 0)):
        self.pos = Vector((pos[0], pos[0]))

    def int(self) -> (int, int):
        return int(self.pos.x), int(self.pos.y)

    def move(self, v: Vector):
        if self.pos.distance_to(v) < Const.WIN_DIST/5:
            self.pos = v
        else:
            xLen = v.x - self.pos.x
            yLen = v.y - self.pos.y
            normalPos = (xLen, yLen)
            normal = Vector(normalPos)
            normal = normal.normalize()
            normal.x *= self.moveSpeed
            normal.y *= self.moveSpeed
            self.pos.x += normal.x
            self.pos.y += normal.y
