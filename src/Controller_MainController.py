import Controller_SubController as sCon
# from Controller import SubController as sCon
mazesArray = []


class MainController:
    def __init__(self, sizesList, amount):
        self.sizesList = sizesList
        self.amount = amount
        self.mazesArray = []

    def runMain(self):
        global mazesArray
        c1 = sCon.SubController(self.amount, self.sizesList)
        c1.makeMazesWithStats()
        mazesArray = c1.loadFromJSON("Mazes")

    def getMazes(self):
        print("From Controller_MainController.getMazes")
        print(self.mazesArray)
        return self.mazesArray


if __name__ == "__main__":
    mc = MainController([5], 5)
    mc.runMain()
