import pygame
from src.Util import Const, Color
from enum import Enum
from src.controller.Singleton import Singleton

class Menu(Enum):
    NO = 0,
    MAIN = 1,
    SETTINGS = 2

class Button():
    upperLeft: (int, int) = (0, 0)
    lowerRight: (int, int) = (0, 0)
    action = None

    def __init__(self, upperLeft: (int, int), lowerRight: (int, int), action):
        self.upperLeft = upperLeft
        self.lowerRight = lowerRight
        self.action = action

    def isInside(self, pos: (int, int)):
        return pos[0] > self.upperLeft[0] and \
               pos[0] < self.lowerRight[0] and \
               pos[1] < self.upperLeft[1] and \
               pos[1] > self.lowerRight[1]

    def click(self):
        self.action()

class MenuController(Singleton):
    mainMenuButtons: [Button] = []
    settingsMenuButtons: [Button] = []
    menu: Menu = Menu.NO

    def __init__(self, state, screen):
        self.state = state
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
        
    def draw(self):
        self.showFilter()
        if self.menu == Menu.Main:
            self.drawMainMenu()
        if self.menu == Menu.Settings:
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
        width, height = 100, 400
        s = pygame.Surface(width, height)
        s.set_alpha(200)
        s.fill((0, 0, 0))
        pos = (Const.WINDOW[0] / 2 - width / 2,
               Const.WINDOW[1] / 2 - height / 2)
        self.screen.blit(s, ())
        # label
        headerFont = pygame.font.SysFont("Comic Sans MS", 28)
        header = headerFont.render('Main Menu', 1, Color.GREEN)
        self.screen.blit(header, (pos[0], pos[1]+50))
        itemFont = pygame.font.SysFont("Comic Sans MS", 28)
        item1 = itemFont.render('item 1', 1, Color.GREEN)
        item2 = itemFont.render('item 2', 1, Color.GREEN)
        item3 = itemFont.render('item 3', 1, Color.GREEN)
        pos1 = (pos[0], pos[1]+50)
        self.mainMenuButtons.append(Button(pos1,
                (pos1[0]+90, pos1[1]+30), self.button1))
        self.screen.blit(item1, pos1)
        pos2 = (pos[0], pos[1]+100)
        self.mainMenuButtons.append(Button(pos2,
                (pos2[0] + 90, pos2[1] + 30), self.button2))
        self.screen.blit(item2, pos2)
        pos3 = (pos[0], pos[1]+100)
        self.mainMenuButtons.append(Button(pos3,
                (pos3[0] + 90, pos3[1] + 30), self.button3))
        self.screen.blit(item3, pos3)

    def button1(self): print('button1')

    def button2(self): print('button2')

    def button3(self): print('button3')

    def drawSettingsMenu(self):
        print('settings menu not yet implemented')
