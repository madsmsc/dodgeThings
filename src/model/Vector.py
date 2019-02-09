from pygame import Vector2

class Vector(Vector2):
    def __init__(self, pos: (float, float) = (0, 0)):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]

    def set(self, x: int = 0, y: int = 0, pos: (float, float) = (0, 0)):
        self.x = x
        self.y = y
        if pos[0] != 0 or pos[1] != 0:
            self.x = pos[0]
            self.y = pos[1]
