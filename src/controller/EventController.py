import pygame
from src.model.Vector import Vector
from src.controller.MenuController import MenuController
from src.controller.SkillController import SkillController
from src.controller.StateController import StateController

class EventController:
    __instance = None

    @staticmethod
    def getInstance():
        if EventController.__instance is None:
            EventController.__instance = EventController()
        return EventController.__instance

    menu: MenuController = MenuController.getInstance()
    skill: SkillController = SkillController.getInstance()
    state: StateController = StateController.getInstance()

    def stopEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if self.menu.isShowMenu():
                self.handleMenuEvent(event)
            else:
                self.handleGameEvent(event)
        return False

    def handleGameEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.menu.showMainMenu()
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.state.player.moveTo = Vector(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            self.skill.useSkill(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            self.skill.useSkill(1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            self.skill.useSkill(2)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            self.skill.useSkill(3)

    def handleMenuEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.menu.hideMenu()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.menu.click(pygame.mouse.get_pos())
