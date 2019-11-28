import SubController as sCon

class MainController:
    def __init__(self, sizesList, amount):
        self.sizesList = sizesList
        self.amount = amount

    def runMain(self):
        print("Runing Main")
        c1 = sCon.SubController(self.amount, self.sizesList)
        c1.makeMazesWithStats()

if __name__ == "__main__":
    mc = MainController([5,10,15,20],5)
    mc.runMain()
    print("starting main")