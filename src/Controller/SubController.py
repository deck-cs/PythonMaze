from Controller import MazeController as mazeCon

class SubController:
    def __init__(self, amount, sizes):
        self.amount = amount
        self.sizes = sizes
        

    def makeMazesWithStats(self):
        for x in range(self.sizes):
            mazes = mazeCon.MazeController(self.amount,self.sizes[x])



    def makeStatNumbers(self, solvingTimes, relatedValues):
        global solvingTimes
        global relatedValues
        solvingTimes = {}
        x = 1
        for aTry in solvedTimesList:
            solvingTimes.setdefault(x, 0)
            solvingTimes[x] = aTry
            x+=1