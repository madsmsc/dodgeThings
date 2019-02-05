from src.Util import vec, Const

class State:
    linePos = vec(0, 0)
    ballPos = vec(60, 250)
    lines = []

    def nextStep(self):
        normal = vec(self.ballPos.x - self.linePos.x, self.ballPos.y - self.linePos.y)
        normal = normal.normalize()
        normal.x *= Const.LINE_STEP
        normal.y *= Const.LINE_STEP
        self.linePos.x += normal.x
        self.linePos.y += normal.y
        # print('to ' + str(normal.x) + ', ' + str(normal.y))

    def addLine(self):
        newLine = {'from': vec(self.linePos.x, self.linePos.y),
                   'to': vec(0, 0)}
        self.nextStep()
        newLine['to'].x = self.linePos.x
        newLine['to'].y = self.linePos.y
        self.lines.append(newLine)
        # print(f"new line ({newLine['from'].x}), {newLine['from'].y}) , ({newLine['to'].x}, {newLine['to'].y})")
