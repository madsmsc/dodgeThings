"""
lav felter til Node:
maxHealth, curHealth
maxPower, curPower
"""

class SkillController:
    __instance = None

    @staticmethod
    def getInstance():
        if SkillController.__instance is None:
            SkillController.__instance = SkillController()
        return SkillController.__instance

    USING_SKILL: str = "Using ";
    NO_POWER: str = "Not enough power to use ";
    equipped: [Skill] = [None, None, None, None, None]
    gui: GUI = None
    player: Player = None

    def __init__(self, gui):
        self.gui = gui
        self.player = player

    def useSkill(self, slot):
        if slot < 0 or slot > 4:
            print('slot outside skill range')
            return
        skill = equipped[slot]
        if player.power < skill.powerCost:
            gui.notify(NO_POWER + skill.name)
        else:
            skill.cast()
            player.power -= skill.powerCost

class Skill:
    name: str = ''
    description: str = ''
    powerCost: int = 0
    damage: int = 0

    def cast(self):
        print('casting ability')
        """
        find ud af hvordan jeg skal caste spells, 
        hvordan det skal ramme fjender og 
        hvordan det skal renderes
        """
    
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
