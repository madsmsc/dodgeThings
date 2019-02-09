from src.controller.GuiController import GuiController
from src.controller.Singleton import Singleton
from src.model.Player import Player

class Skill:
    name: str = ''
    description: str = ''
    powerCost: int = 0
    damage: int = 0

class Nanobots(Skill):
    def __init__(self):
        self.name = 'Nanobots'
        self.description = 'Restore health'
        self.powerCost = 2
        self.damage = 3

class PowerNova(Skill):
    def __init__(self):
        self.name = 'PowerNova'
        self.description = 'Cause explosion'
        self.powerCost = 2
        self.damage = 3

class OverDrive(Skill):
    def __init__(self):
        self.name = 'Overdrive'
        self.description = 'Run faster'
        self.powerCost = 4
        self.damage = 0


class SkillController(Singleton):
    NO_POWER: str = 'Not enough power to use '
    equipped: [Skill] = [PowerNova(), None, None, None, None]
    gc: GuiController = GuiController.getInstance()
    player: Player = None

    def setup(self, player):
        self.player = player

    def useSkill(self, slot):
        if slot < 0 or slot > 4:
            print('slot outside skill range')
            return
        skill = self.equipped[slot]
        if self.player.curPower < skill.powerCost:
            self.gc.notify(self.NO_POWER + skill.name)
        else:
            self.player.curPower -= skill.powerCost
            self.gc.nova(self.equipped[0].damage)
