import ModelMaze as mazeCon
import matplotlib.pyplot as plt
import json
import MazeException


class SubModel:
    def __init__(self, amount, sizesList):
        self.amount = amount  # Antal iterationer for hver størrelse
        self.sizesList = sizesList  # Størrelserne der skal itereres igennem
        self.solvedTimesList = []  # Tiderne for de løste mazes
        self.attempts = {}  # dictorinary med tider for alle forsøg(1,2,3,4...)
        # Liste der viser min, avg, og max af hver iteration(Bare en masse string værdier)
        self.tryList = []
        # Værdien af hvilken iteration man er kommet til(5, 10, 15...)
        self.iteration = 0
        self.theTimes = []  # Listen af tider til at løse
        self.relatedValues = []  # Listen af places visited over tid til at løse
        # Den endelige liste over min, max og avg værdier for places visited
        self.pvListFinal = []
        self.mazesArray = []

    def makeMazesWithStats(self):
        for x in range(len(self.sizesList)):
            try:
                mazes = mazeCon.MazeModel(self.amount, self.sizesList[x])
            except MazeException.MazeException as e:
                raise
            except Exception as e:
                raise
            # self.mazesArray.append(mazes.makeAndSolve()) #Unthreaded method
            try:
                self.mazesArray.append(mazes.threadedMakeAndSolve())
            except Exception as e:
                raise
            self.iteration = self.sizesList[x]
            self.solvedTimesList = mazes.solvedTimesList
            self.makeStatNumbers()
            self.getStatKeys()
            self.getStatValues()
            self.getRelatedValues(mazes.pvList)
            self.getPvListFinal(mazes.pvList)
        self.makePlots(1)
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

    # Laver liste af navnene som skal bruges på x-aksen på begge grafer for hver iteration
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

    # Laver en liste med værdierne for min, avg, max for hver iteration
    def getStatValues(self):
        self.theTimes.append(min(list(self.attempts.values())))
        self.theTimes.append(
            sum(list(self.attempts.values()))/len(list(self.attempts.values())))
        self.theTimes.append(max(list(self.attempts.values())))

    # Laver en liste med værdierne for min, avg, max for tid over placevisited
    def getRelatedValues(self, pvList):
        solveList = list(self.attempts.values())
        minKey = min(self.attempts, key=self.attempts.get)-1
        self.relatedValues.append(min(solveList)/pvList[minKey])
        self.relatedValues.append(
            (sum(solveList)/len(solveList))/((sum(pvList)/len(pvList))))
        maxKey = max(self.attempts, key=self.attempts.get)-1
        self.relatedValues.append(max(solveList)/pvList[maxKey])

    def getPvListFinal(self, pvList):
        self.pvListFinal.append(min(pvList))
        self.pvListFinal.append(sum(pvList)/len(pvList))
        self.pvListFinal.append(max(pvList))

    def makePlots(self, figNum):
        fig1 = plt.figure()
        ax1 = fig1.add_subplot()
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
        fig2 = plt.figure()
        ax3 = fig2.add_subplot()
        ax3 = plt
        ax3.xticks(rotation=45)
        ax3.title("Time over places visited")
        ax3.xlabel("Attempt", fontsize=10)
        ax3.bar(self.tryList, self.relatedValues, width=0.3, align='center')
        ax3.ylabel('Time pr. move', color='tab:red')
        ax3.tick_params(axis='y')
        if(figNum == 1):
            return fig1
        elif (figNum == 2):
            return fig2
        return plt
