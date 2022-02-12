import random


class World():

    def __init__(self, width, height):
        self.grid = Grid(width, height)
        self.generations = 0

    def flip(self):
        for cell in self.grid.cells.values():
            cell.toggleAlive()


    def randomize(self):
        chance = random.randint(0,100)
        for cell in self.grid.cells.values():
            roll = random.randint(0,100)
            if roll < chance:
                cell.toggleAlive()


    def countLiveNeighbours(self, x, y):
        aliveCount = 0
        neighbours = [(-1,-1), (0,-1), (1,-1),(-1, 0), (1, 0),(-1,1),(0,1), (1,1)]

        for neighbour in neighbours:
            coord=(x+neighbour[0],y+neighbour[1])
            if coord in self.grid.cells.keys():
                if self.grid.cells[coord].isAlive:
                    aliveCount += 1

        return aliveCount


    def update(self):
        newGrid = Grid(self.grid.width, self.grid.height)
        for cell in self.grid.cells.keys():
            live = self.countLiveNeighbours(cell[0], cell[1])

            if self.grid.cells[cell].isAlive:
                if live < 2:
                    newGrid.cells[cell].isAlive = False
                elif live == 2 or live == 3:
                    newGrid.cells[cell].isAlive = True
                elif live > 3:
                    newGrid.cells[cell].isAlive = False
            elif live == 3:
                newGrid.cells[cell].isAlive = True

        self.generations += 1
        self.grid.update(newGrid.cells)

    def nukeAll(self):
        self.__init__(self.grid.width, self.grid.height)


    def getDimensions(self):
        return (self.grid.width, self.grid.height)

class Grid():

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = {}

        for y in range(height):
            for x in range(width):
                self.cells[(x,y)]=Cell()

    def update(self, newCells):
        self.cells = newCells

class Cell:

    def __init__(self, alive=False):
        self.isAlive = alive

    def toggleAlive(self):
        self.isAlive = not self.isAlive
