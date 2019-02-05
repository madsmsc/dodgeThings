from pygame import Vector2

class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

class Const:
    LINE_STEP = 1
    LINE_WIDTH = 4
    WIN_DIST = 15
    CLOCK_TICK = 100
    WINDOW = [1200, 900]
    TITLE = 'Follow the ball!'

def vec(x: float, y: float):
    v = Vector2()
    v.x = x
    v.y = y
    return v
