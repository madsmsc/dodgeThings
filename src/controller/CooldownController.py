class CooldownController:
    __instance = None

    @staticmethod
    def getInstance():
        if CooldownController.__instance is None:
            CooldownController.__instance = CooldownController()
        return CooldownController.__instance

# threading.
# myThread = threading.Thread(None, self.myFace)
# myThread.start()

# def myFace(self):
#    cond = threading.Condition()
#    cond.wait(timeout=100)
