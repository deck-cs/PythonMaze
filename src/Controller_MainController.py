import Controller_SubController as sCon
# from Controller import SubController as sCon


class MainController:
    def __init__(self, sizesList, amount):
        self.sizesList = sizesList
        self.amount = amount

    def runMain(self):
        c1 = sCon.SubController(self.amount, self.sizesList)
        c1.makeMazesWithStats()


if __name__ == "__main__":
    mc = MainController([5], 5)
    mc.runMain()
