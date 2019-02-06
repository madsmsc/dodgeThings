import pygame
from src.State import State
from src.Util import Color, Const
from src.GUI import GUI
from src.Vector import Vector

def stopEvent(state: State):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            state.player.moveTo = Vector(pygame.mouse.get_pos())
    return False

def draw(state: State, screen, gui):
    screen.fill(Color.BLACK)
    facePos = (state.player.pos.x - 25, state.player.pos.y - 23)
    screen.blit(gui.icons[0][2], facePos)
    for enemy in state.enemies:
        pygame.draw.circle(screen, Color.BLUE, enemy.int(), 10)
    gui.render()
    pygame.display.flip()

def gameLoop(state: State, screen, clock, gui):
    clock.tick(Const.CLOCK_TICK)
    if stopEvent(state):
        return False
    if state.player.currentHealth <= 0:
        print('you lose!')
        return False
    state.update(1.0 / Const.CLOCK_TICK)
    draw(state, screen, gui)
    return True

def start():
    pygame.init()
    screen = pygame.display.set_mode(Const.WINDOW)
    state = State()
    gui = GUI(state, screen)
    pygame.display.set_caption(Const.TITLE)
    clock = pygame.time.Clock()

    while 1:
        if not gameLoop(state, screen, clock, gui):
            break
    pygame.quit()

if __name__ == '__main__':
    start()
