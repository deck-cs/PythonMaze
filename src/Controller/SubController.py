from Controller import MazeController as mazeCon

class SubController:
    def __init__(self, amount, sizes):
        self.amount = amount
        self.sizes = sizes
        self.solvedTimesList = []
        self.attempts = {}
        self.tryList = []
        self.iteration = 0
        self.theTimes = []
        self.relatedValues = []
        self.pvListFinal = []


    def makeMazesWithStats(self):
        for x in range(self.sizes):
            mazes = mazeCon.MazeController(self.amount,self.sizes[x])
            self.makeStatNumbers(mazes.solvedTimesList)
            self.getRelatedValues(mazes.pvList)


    def makeStatNumbers(self, solvedTimesList):
        x = 1
        for aTry in self.solvedTimesList:
            self.attempts.setdefault(x, 0)
            self.attempts[x] = aTry
            x+=1

    def getStatKeys(self):
        min = "min"
        min+=str(self.iteration)
        avg = "avg"
        avg+=str(self.iteration)
        max = "max"
        max+= str(self.iteration)
        self.tryList.append(min)
        self.tryList.append(avg)
        self.tryList.append(max)

    def getStatValues(self):
        self.theTimes.append(min(list(self.attempts.values())))
        self.theTimes.append(sum(list(self.attempts.values()))/len(list(self.attempts.values())))
        self.theTimes.append(max(list(self.attempts.values())))

    def getRelatedValues(self, pvList):
        solveList = list(self.attempts.values())
        minKey = min(self.attempts, key=self.attempts.get)-1
        self.relatedValues.append(min(solveList)/pvList[minKey])
        self.relatedValues.append((sum(solveList)/len(solveList))/((sum(pvList)/len(pvList))))
        maxKey = max(self.attempts, key=self.attempts.get)-1
        self.relatedValues.append(min(solveList)/pvList[maxKey])

    def getPvListFinal(self, pvList):
        self.pvListFinal.append(min(pvList))
        self.pvListFinal.append(sum(pvList)/len(pvList))
        self.pvListFinal.append(max(pvList))