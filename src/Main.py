import pygame
from src.State import State
from pygame import Vector2
from src.Util import Color, Const

def vecPos(v: Vector2):
    return [int(v.x), int(v.y)]

def stopEvent(state: State):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            state.ballPos.x = pos[0]
            state.ballPos.y = pos[1]
    return False

def lineReachedBall(state: State):
    dist = state.linePos.distance_to(state.ballPos)
    # print('dist ' + str(dist))
    if dist < Const.WIN_DIST:
        return True
    return False

def draw(state: State, screen):
    screen.fill(Color.BLACK)
    state.addLine()
    # for i, line in enumerate(lines):
    for line in state.lines:
        pygame.draw.line(screen, Color.GREEN, line['from'], line['to'], Const.LINE_WIDTH)
    pygame.draw.circle(screen, Color.BLUE, vecPos(state.ballPos), 10)
    pygame.display.flip()

def gameLoop(state: State, screen, clock):
    clock.tick(Const.CLOCK_TICK)
    if stopEvent(state):
        return False
    if lineReachedBall(state):
        print('WIN MOTHERFUCKER!')
        return False
    draw(state, screen)
    return True

def start():
    pygame.init()
    state = State()
    screen = pygame.display.set_mode(Const.WINDOW)
    pygame.display.set_caption(Const.TITLE)
    clock = pygame.time.Clock()
    while 1:
        if not gameLoop(state, screen, clock):
            break
    pygame.quit()

if __name__ == '__main__':
    start()
