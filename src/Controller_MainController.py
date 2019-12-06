import Controller_SubController as sCon
# from Controller import SubController as sCon
mazesArray = []


class MainController:
    def __init__(self, sizesList, amount):
        self.sizesList = sizesList
        self.amount = amount
        self.c1 = sCon.SubController(self.amount, self.sizesList)
        self.mazesArray = []

    def runMain(self):
        self.c1.makeMazesWithStats()
        self.mazesArray = self.c1.getMazes()

    def getMazes(self):
        self.mazesArray = self.c1.loadFromJSON("Mazes")
        return self.mazesArray


if __name__ == "__main__":
    mc = MainController([5, 10], 5)
    mc.runMain()
