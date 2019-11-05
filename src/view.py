import controller as cntr
import matplotlib.pyplot as plt

tryList = {}
theTimes = {}
relatedValues = {}
pvList = []

def makePlot():
    fig1, ax1 = plt.subplots()
    plt.xticks(rotation=45)
    ax1.set_ylabel('Time for solve', color='tab:blue')
    # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
    ax1.bar(tryList, theTimes, width=0.5, align='center')
    ax2 = ax1.twinx()
    ax2.bar(tryList, pvList, width=0.3, align='edge',color='orange')
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
    ax3.bar(tryList, relatedValues, width = 0.3, align='center')
    ax3.set_ylabel('Time pr. move', color='tab:red')
    ax3.tick_params(axis='y')
    plt.show()

for x in range(6):  #The range is how many 
    cntr.mainRun((x+1)*5)   #Scales each iteration by 5
    cntr.makeStatNumbers()
    cntr.getStatKeys()
    cntr.getStatValues()
    cntr.getRelatedValues()
    cntr.getPvListFinal()
tryList = list(cntr.tryList)

relatedValues = list(cntr.relatedValues)
theTimes = list(cntr.theTimes)
pvList = list(cntr.pvListFinal)
print(tryList)
print("try")
print(relatedValues)
print("relate")
print(theTimes)
print("time")
print(pvList)
print("placesV")
makePlot()