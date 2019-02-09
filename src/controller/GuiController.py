import pygame
from src.Util import Color, Const
from src.model.State import State

class GuiController:
    __instance = None

    @staticmethod
    def getInstance():
        if GuiController.__instance is None:
            GuiController.__instance = GuiController()
        return GuiController.__instance

    state: State = None
    screen: pygame.Surface = None
    font = None
    maxLabelTime = 300
    labelTime = 0
    msgLabel = None
    maxNovaDist = 100
    novaDist = maxNovaDist
    novaWidth = 3

    iconBully, iconEvil, iconZombie, iconPlayer = None, None, None, None
    iconHealth, iconPower = None, None

    def setup(self, state, screen):
        self.state = state
        self.screen = screen
        self.font = pygame.font.SysFont("Comic Sans MS", 34)
        self.iconBully = self.loadIcon(Const.ICON_BULLY)
        self.iconEvil = self.loadIcon(Const.ICON_EVIL)
        self.iconZombie = self.loadIcon(Const.ICON_ZOMBIE)
        self.iconPlayer = self.loadIcon(Const.ICON_PLAYER)
        self.iconHealth = self.loadIcon(Const.ICON_HEALTH)
        self.iconPower = self.loadIcon(Const.ICON_POWER)

    def render(self):
        self.renderBottomPabel()
        self.renderNotificationLabel()
        self.renderPlayerNova()

    def renderPlayerNova(self):
        if self.novaDist < self.maxNovaDist:
            self.novaDist += 1
            pygame.draw.circle(self.screen, Color.BLUE, self.state.player.int(), self.novaDist, 3)

    def renderNotificationLabel(self):
        if self.labelTime > 0:
            self.labelTime -= 1
        if self.labelTime <= 0 and self.msgLabel is not None:
            self.msgLabel = None
        if self.msgLabel is not None:
            self.screen.blit(self.msgLabel, (Const.WINDOW[0] / 2 - 100, 100))

    def renderBottomPabel(self):
        hp = self.state.player.curHealth
        pp = self.state.player.curPower
        healthLabel = self.font.render(str(hp), 1, Color.GREEN)
        powerLabel = self.font.render(str(pp), 1, Color.BLUE)
        healthPos = (Const.WINDOW[0] / 2 - 50, Const.WINDOW[1] - 50)

        s = pygame.Surface((300, 70))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        self.screen.blit(s, (healthPos[0]-100, healthPos[1]-5))

        self.screen.blit(healthLabel, healthPos)
        self.screen.blit(self.iconHealth, (healthPos[0]-60, healthPos[1]))

        self.screen.blit(powerLabel, (healthPos[0]+160, healthPos[1]))
        self.screen.blit(self.iconPower, (healthPos[0]+100, healthPos[1]))

    def loadIcon(self, filename) -> pygame.Surface:
        image = pygame.image.load(filename).convert_alpha()
        tile = pygame.transform.scale(image, (50, 47))
        return tile

    def notify(self, msg: str):
        self.msgLabel = self.font.render(msg, 1, Color.BLACK)
        self.labelTime = self.maxLabelTime

    def nova(self, damage: int):
        self.novaDist = self.novaWidth + 1
        self.state.enemiesTakeNovaDamage(self.maxNovaDist, damage)
