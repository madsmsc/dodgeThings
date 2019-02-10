import pygame
from src.Util import Color, Const
from src.controller.StateController import StateController
from src.controller.SkillController import SkillController
from src.controller.GuiController import GuiController
from src.controller.MapController import MapController
from src.controller.MenuController import MenuController
from src.controller.EventController import EventController

class Main:
    gui: GuiController = GuiController.getInstance()
    map: MapController = MapController.getInstance()
    skill: SkillController = SkillController.getInstance()
    menu: MenuController = MenuController.getInstance()
    event: EventController = EventController.getInstance()
    state: StateController = StateController.getInstance()
    screen = None
    clock = None

    def render(self):
        self.screen.fill(Color.BLACK)
        self.gui.blockolize()
        facePos = (self.state.player.pos.x - 25, self.state.player.pos.y - 23)
        self.screen.blit(self.gui.iconPlayer, facePos)
        for enemy in self.state.enemies:
            self.screen.blit(self.gui.iconBully, enemy.int())
        self.gui.render()
        self.menu.render()
        pygame.display.flip()

    def gameLoop(self):
        self.clock.tick(Const.CLOCK_TICK)
        if self.event.stopEvent():
            return False
        if self.state.player.curHealth <= 0:
            print('you lose!')
            return False
        if not self.menu.isShowMenu():
            self.state.update(1.0 / Const.CLOCK_TICK)
        self.render()
        return True

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Const.WINDOW)
        self.state.setup()
        self.gui.setup(self.screen)
        self.menu.setup(self.screen)
        pygame.display.set_caption(Const.TITLE)
        self.clock = pygame.time.Clock()
        self.map.makeMap()
        while 1:
            if not self.gameLoop():
                break
        pygame.quit()

if __name__ == '__main__':
    Main().start()
