import pygame
from src.Util import Color, Const
from src.State import State

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
    icons = []

    def setup(self, state, screen):
        self.state = state
        self.screen = screen
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.loadIcons(Const.PLAYER_ICONS, 200, 188)

    def render(self):
        hp = self.state.player.currentHealth
        text = 'hp=' + str(hp)
        label = self.font.render(text, 1, Color.GREEN)
        self.screen.blit(label, (Const.WINDOW[0] / 2 - 50, Const.WINDOW[1] - 50))

    def loadIcons(self, filename, width, height):
        image = pygame.image.load(filename).convert()
        image_width, image_height = image.get_size()
        for tile_x in range(0, int(image_width/width)):
            line = []
            self.icons.append(line)
            for tile_y in range(0, int(image_height/height)):
                rect = (tile_x*width, tile_y*height, width, height)
                tile = image.subsurface(rect)
                tile = pygame.transform.scale(tile, (50, 47))
                line.append(tile)
        return self.icons
