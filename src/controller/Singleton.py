class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance
