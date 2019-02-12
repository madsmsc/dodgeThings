from random import Random

class Map:
    # the size of the map
    width: int = 0
    height: int = 0
    # list of tuples containing treasure positions
    treasures: [(int, int)] = []
    # the map indicating if cells are alive
    cellmap: [[bool]] = [[]]
    # how dense the initial grid is with living cells [0, 100]
    chanceToStartAlive: float = 45
    # the lower neighbour limit at which cells start dying
    starvationLimit: int = 2
    # the upper neighbour limit at which cells start dying
    deathLimit: int = 4
    # the number of neighbours that cause a dead cell to become alive
    birthLimit: int = 4
    # the number of times we perform the simulation step
    stepLimit: int = 6
    # number of hidden treasures
    treasureHiddenLimit: int = 5
 
    def initialiseMap(self, map: [[bool]]) -> [[bool]]:
        r = Random()
        for x in range(0, self.width):
            for y in range(0, self.height):
                if r.randint(0, 100) < self.chanceToStartAlive:
                    map[x][y] = True
        return map

    def createBlankMap(self) -> [[bool]]:
        return [[False for i in range(self.height)]
                for j in range(self.width)]

    def doSimulationStep(self, oldMap: [[bool]]) -> [[bool]]:
        newMap: [[bool]] = self.createBlankMap()
        for x in range(0, len(oldMap)):
            for y in range(0, len(oldMap[0])):
                nbs: int = self.countAliveNeighbours(oldMap, x, y)
                if oldMap[x][y]:
                    if nbs < self.deathLimit:
                        newMap[x][y] = False
                    else:
                        newMap[x][y] = True
                else:
                    if nbs > self.birthLimit:
                        newMap[x][y] = True
                    else:
                        newMap[x][y] = False
        return newMap
    
    def countAliveNeighbours(self, map: [[bool]], x: int, y: int) -> int:
        count: int = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbour_x: int = x+i
                neighbour_y: int = y+j
                if i == 0 and j == 0:
                    pass
                elif neighbour_x < 0 or neighbour_y < 0 or \
                        neighbour_x >= len(map) or \
                        neighbour_y >= len(map[0]):
                    count += 1
                elif map[neighbour_x][neighbour_y]:
                    count += 1
        return count

    def generateMap(self, width: int = 20, height: int = 20):
        self.width = width
        self.height = height
        self.cellmap = self.createBlankMap()
        self.cellmap = self.initialiseMap(self.cellmap)
        for i in range(0, self.stepLimit):
            self.cellmap = self.doSimulationStep(self.cellmap)

    def placeTreasure(self):
        for x in range (0, self.width):
            for y in range(0, self.height):
                if not self.cellmap[x][y]:
                    nbs: int = self.countAliveNeighbours(self.cellmap, x, y)
                    if nbs >= self.treasureHiddenLimit:
                        self.treasures.append((x, y))

    def printMap(self):
        s: str = ''
        for i in range(self.height):
            for j in range(self.width):
                if self.isTreasure((j, i)):
                    s += 'X'
                elif self.cellmap[j][i]:
                    s += ' '
                else:
                    s += '.'
            s += '\n'
        print(s)

    def isTreasure(self, pos: (int, int)):
        for t in self.treasures:
            if t == pos:
                return True
        return False

if __name__ == '__main__':
    map = Map()
    map.generateMap(12 * 4, 48 * 2)
    map.placeTreasure()
    map.printMap()
