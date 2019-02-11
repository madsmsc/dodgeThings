import pygame
from src.controller.StateController import StateController
from src.Util import Const, Color
from enum import Enum

class Menu(Enum):
    NO = 0,
    MAIN = 1,
    SETTINGS = 2

class Button:
    pos: (int, int) = (0, 0)
    dim: (int, int) = (0, 0)
    action = None

    def __init__(self, pos: (int, int), dim: (int, int), action):
        self.pos = pos
        self.dim = dim
        self.action = action

    def isInside(self, pos: (int, int)):
        # print('is ('+str(pos[0])+','+str(pos[1])+') inside pos ('+
        #      str(self.pos[0])+','+str(self.pos[0])+') and width ('+
        #      str(self.dim[0])+','+str(self.dim[0])+')')
        insideX = self.pos[0] < pos[0] < self.pos[0]+self.dim[0]
        insideY = self.pos[1] < pos[1] < self.pos[1]+self.dim[1]
        # print('insideX='+str(insideX)+', insideY='+str(insideY))
        return insideX and insideY

    def click(self):
        self.action()

class MenuController:
    __instance = None

    @staticmethod
    def getInstance():
        if MenuController.__instance is None:
            MenuController.__instance = MenuController()
        return MenuController.__instance

    mainMenuButtons: [Button] = []
    settingsMenuButtons: [Button] = []
    menu: Menu = Menu.NO
    screen = None
    state: StateController = StateController.getInstance()

    def setup(self, screen):
        self.screen = screen

    def isShowMenu(self) -> bool:
        return self.menu != Menu.NO

    def hideMenu(self):
        self.menu = Menu.NO

    def showMainMenu(self):
        self.menu = Menu.MAIN

    def showSettingsMenu(self):
        self.menu = Menu.SETTINGS

    def showFilter(self):
        s = pygame.Surface(Const.WINDOW)
        s.set_alpha(128)
        s.fill((0, 0, 0))
        self.screen.blit(s, (0, 0))

    def click(self, pos: (int, int)):
        if self.menu == Menu.NO:
            return
        elif self.menu == Menu.MAIN:
            self.clickMainMenu(pos)
        elif self.menu == Menu.SETTINGS:
            self.clickSettingsMenu(pos)
        
    def render(self):
        if not self.isShowMenu():
            return
        self.showFilter()
        if self.menu == Menu.MAIN:
            self.drawMainMenu()
        if self.menu == Menu.SETTINGS:
            self.drawSettingsMenu()

    def clickMainMenu(self, pos: (int, int)):
        for button in self.mainMenuButtons:
            if button.isInside(pos):
                button.click()

    def clickSettingsMenu(self, pos: (int, int)):
        for button in self.settingsMenuButtons:
            if button.isInside(pos):
                button.click()

    def drawMainMenu(self):
        # panel
        width: int = 200
        height: int = 400
        s = pygame.Surface((width, height))
        s.set_alpha(200)
        s.fill((0, 0, 0))
        pos = (Const.WINDOW[0] / 2 - width / 2,
               Const.WINDOW[1] / 2 - height / 2)
        self.screen.blit(s, pos)
        # label
        headerFont = pygame.font.SysFont("Comic Sans MS", 28)
        header = headerFont.render('Game Paused', 1, Color.GREEN)
        self.screen.blit(header, (pos[0]+30, pos[1]+50))
        itemFont = pygame.font.SysFont("Comic Sans MS", 28)
        item1 = itemFont.render('[ESC] to resume', 1, Color.GREEN)
        item2 = itemFont.render('Settings', 1, Color.GREEN)
        item3 = itemFont.render('Exit', 1, Color.GREEN)

        self.mainMenuButtons.append(Button((pos[0]+60, pos[1]+100), (90, 30),
                                            lambda: print('button1')))
        self.screen.blit(item1, (pos[0]+60, pos[1]+100))

        self.mainMenuButtons.append(Button((pos[0]+60, pos[1]+150), (90, 30),
                                           lambda: print('button2')))
        self.screen.blit(item2, (pos[0]+60, pos[1]+150))

        self.mainMenuButtons.append(Button((pos[0]+60, pos[1]+200), (90, 30),
                                           lambda: print('button3')))
        self.screen.blit(item3, (pos[0]+60, pos[1]+200))

    def drawSettingsMenu(self):
        print('settings menu not yet implemented')
