from random import Random

class MapGenerator:
    # the size of the map
    width: int = 20
    height: int = 20
    # the map indicating if cells are alive
    cellmap: [[bool]] = [[]]
    # how dense the initial grid is with living cells [0, 100]
    chanceToStartAlive: float = 45
    # the lower neighbour limit at which cells start dying
    starvationLimit: int = 1
    # the upper neighbour limit at which cells start dying
    deathLimit: int = 3
    # the number of neighbours that cause a dead cell to become alive
    birthLimit: int = 2
    # the number of times we perform the simulation step
    stepLimit: int = 5
    # number of hidden treasures
    treasureHiddenLimit: int = 5
 
    def initialiseMap(self, map: [[bool]]) -> [[bool]]:
        r = Random()
        for x in range(0, self.width):
            for y in range(0, self.height):
                if r.randint(0, 100) < self.chanceToStartAlive:
                    map[x][y] = True
        return map

    def initMap(self) -> [[bool]]:
        return [[False for i in range(self.width)]
                       for j in range(self.height)]

    def doSimulationStep(self, oldMap: [[bool]]) -> [[bool]]:
        newMap: [[bool]] = self.initMap()
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
                        neighbour_x >= map.length or \
                        neighbour_y >= len(map[0]):
                    count += 1
                elif map[neighbour_x][neighbour_y]:
                    count += 1
        return count

    def generateMap(self) -> [[bool]]:
        self.cellmap = self.initMap()
        self.cellmap = self.initialiseMap(self.cellmap)
        for i in range(0, self.stepLimit):
            self.cellmap = self.doSimulationStep(self.cellmap)

    def placeTreasure(self, world: [[bool]]):
        for x in range (0, self.width):
            for y in range(0, self.height):
                if not world[x][y]:
                    nbs: int = self.countAliveNeighbours(world, x, y)
                    if nbs >= self.treasureHiddenLimit:
                        self.placeLoot(x, y)

    def placeLoot(self, x: int, y: int):
        print('placing loot at '+str(x)+','+str(y))
