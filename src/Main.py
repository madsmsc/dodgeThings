import pygame
from src.State import State
from src.Util import Color, Const
from src.GuiController import GuiController
from src.Vector import Vector

class Main:
    gc = GuiController.getInstance()
    state = State()
    screen = None
    clock = None

    def stopEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.state.player.moveTo = Vector(pygame.mouse.get_pos())
        return False

    def draw(self):
        self.screen.fill(Color.BLACK)
        facePos = (self.state.player.pos.x - 25, self.state.player.pos.y - 23)
        self.screen.blit(self.gc.icons[0][2], facePos)
        for enemy in self.state.enemies:
            pygame.draw.circle(self.screen, Color.BLUE, enemy.int(), 10)
        self.gc.render()
        pygame.display.flip()

    def gameLoop(self):
        self.clock.tick(Const.CLOCK_TICK)
        if self.stopEvent():
            return False
        if self.state.player.currentHealth <= 0:
            print('you lose!')
            return False
        self. state.update(1.0 / Const.CLOCK_TICK)
        self.draw()
        return True

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Const.WINDOW)
        self.gc.setup(self.state, self.screen)
        pygame.display.set_caption(Const.TITLE)
        self.clock = pygame.time.Clock()

        while 1:
            if not self.gameLoop():
                break
        pygame.quit()


if __name__ == '__main__':
    Main().start()
