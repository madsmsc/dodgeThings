import pygame, threading
from src.model.State import State
from src.Util import Color, Const
from src.controller.SkillController import SkillController
from src.controller.GuiController import GuiController
from src.controller.MapController import MapController
from src.model.Vector import Vector

class Main:
    gc: GuiController = GuiController.getInstance()
    mc: MapController = MapController.getInstance()
    sc: SkillController = SkillController.getInstance()
    state = State()
    screen = None
    clock = None

    def stopEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.state.player.moveTo = Vector(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.sc.useSkill(0)
            # fix skills paa keys press
            # pygame.KEYDOWN and event.button == 'q'
            # threading.
            #myThread = threading.Thread(None, self.myFace)
            #myThread.start()
        return False

    #def myFace(self):
    #    cond = threading.Condition()
    #    cond.wait(timeout=100)

    def draw(self):
        self.screen.fill(Color.BLACK)
        self.blockolize()
        facePos = (self.state.player.pos.x - 25, self.state.player.pos.y - 23)
        self.screen.blit(self.gc.iconPlayer, facePos)
        for enemy in self.state.enemies:
            self.screen.blit(self.gc.iconBully, enemy.int())
        self.gc.render()
        pygame.display.flip()

    def blockolize(self):
        for x in range(self.mc.blocks):
            for y in range(self.mc.blocks):
                self.screen.fill(self.mc.map[x][y],
                                 pygame.Rect((x * self.mc.blocksize,
                                              y * self.mc.blocksize),
                                 (self.mc.blocksize, self.mc.blocksize)))

    def gameLoop(self):
        self.clock.tick(Const.CLOCK_TICK)
        if self.stopEvent():
            return False
        if self.state.player.curHealth <= 0:
            print('you lose!')
            return False
        self.state.update(1.0 / Const.CLOCK_TICK)
        self.draw()
        return True

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Const.WINDOW)
        self.gc.setup(self.state, self.screen)
        pygame.display.set_caption(Const.TITLE)
        self.clock = pygame.time.Clock()
        self.mc.makeMap()
        self.sc.setup(self.state.player)
        while 1:
            if not self.gameLoop():
                break
        pygame.quit()

if __name__ == '__main__':
    Main().start()
