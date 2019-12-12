import Controller_MazeController as mazeCon
import matplotlib.pyplot as plt
import json


class SubController:
    def __init__(self, amount, sizesList):
        self.amount = amount
        self.sizesList = sizesList
        self.solvedTimesList = []
        self.attempts = {}
        self.tryList = []
        self.iteration = 0
        self.theTimes = []
        self.relatedValues = []
        self.pvListFinal = []
        self.mazesArray = []

    def makeMazesWithStats(self):
        for x in range(len(self.sizesList)):
            try:
                mazes = mazeCon.MazeController(self.amount, self.sizesList[x])
            except Exception as e: raise
            # self.mazesArray.append(mazes.makeAndSolve())
            try:
                self.mazesArray.append(mazes.threadedMakeAndSolve())
            except Exception as e: raise
            self.iteration = self.sizesList[x]
            self.solvedTimesList = mazes.solvedTimesList
            self.makeStatNumbers()
            self.getStatKeys()
            self.getStatValues()
            self.getRelatedValues(mazes.pvList)
            self.getPvListFinal(mazes.pvList)
        self.makePlots()
        self.saveToJSON("Mazes")

    def saveToJSON(self, filename):
        with open(filename+'.json', "w") as write_file:
            json.dump(self.mazesArray, write_file)

    def loadFromJSON(self, filename):
        with open(filename+'.json') as f:
            self.mazesArray = json.load(f)
            return self.mazesArray

    def makeStatNumbers(self):
        x = 1
        for aTry in self.solvedTimesList:
            self.attempts.setdefault(x, 0)
            self.attempts[x] = aTry
            x += 1

    def getStatKeys(self):
        min = "min"
        min += str(self.iteration)
        avg = "avg"
        avg += str(self.iteration)
        max = "max"
        max += str(self.iteration)
        self.tryList.append(min)
        self.tryList.append(avg)
        self.tryList.append(max)

    def getMazes(self):
        return self.mazesArray

    def getStatValues(self):
        self.theTimes.append(min(list(self.attempts.values())))
        self.theTimes.append(
            sum(list(self.attempts.values()))/len(list(self.attempts.values())))
        self.theTimes.append(max(list(self.attempts.values())))

    def getRelatedValues(self, pvList):
        solveList = list(self.attempts.values())
        minKey = min(self.attempts, key=self.attempts.get)-1
        self.relatedValues.append(min(solveList)/pvList[minKey])
        self.relatedValues.append(
            (sum(solveList)/len(solveList))/((sum(pvList)/len(pvList))))
        maxKey = max(self.attempts, key=self.attempts.get)-1
        self.relatedValues.append(min(solveList)/pvList[maxKey])

    def getPvListFinal(self, pvList):
        self.pvListFinal.append(min(pvList))
        self.pvListFinal.append(sum(pvList)/len(pvList))
        self.pvListFinal.append(max(pvList))

    def makePlots(self):
        fig1, ax1 = plt.subplots()
        plt.xticks(rotation=45)
        ax1.set_ylabel('Time for solve', color='tab:blue')
        # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
        ax1.bar(self.tryList, self.theTimes, width=0.5, align='center')
        ax2 = ax1.twinx()
        ax2.bar(self.tryList, self.pvListFinal,
                width=0.3, align='edge', color='orange')
        ax2.set_ylabel('Attempts', color='tab:orange')
        ax2.tick_params(axis='y')
        # plt.ticklabel_format(useOffset=False)
        #  plt.axis([0, len(solvingTimes)+1, 0, max(theTimes)+0.01])  # axis(x-min, x-max, y-min, y-max)
        plt.title("Barplot Time to solve and places visited", fontsize=10)
        plt.xlabel("Attempt", fontsize=10)
        #plt.ylabel("TimeSolved", fontsize=10)
        plt.tick_params(axis='both', which='major', labelsize=10)
        # Plot 2
        fig2, ax3 = plt.subplots()
        plt.xticks(rotation=45)
        plt.title("Time over places visited")
        plt.xlabel("Attempt", fontsize=10)
        ax3.bar(self.tryList, self.relatedValues, width=0.3, align='center')
        ax3.set_ylabel('Time pr. move', color='tab:red')
        ax3.tick_params(axis='y')
        plt.show()
