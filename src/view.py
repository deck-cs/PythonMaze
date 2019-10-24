import controller as cntr
import matplotlib.pyplot as plt

tryList = {}
theTimes = {}
relatedValues = {}
pvList = {}

def makePlot():
    fig1, ax1 = plt.subplots()
    ax1.set_ylabel('Time for solve', color='tab:blue')
    # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
    ax1.bar(tryList, theTimes, width=0.5, align='center')
    ax2 = ax1.twinx()
    ax2.bar(tryList, pvList, width=0.3, align='edge',color='orange')
    ax2.set_ylabel('Attempts', color='tab:orange')
    ax2.tick_params(axis='y')
    # plt.ticklabel_format(useOffset=False)
    #  plt.axis([0, len(solvingTimes)+1, 0, max(theTimes)+0.01])  # axis(x-min, x-max, y-min, y-max)
    plt.title("Barplot Time to solve", fontsize=12)
    plt.xlabel("Attempt", fontsize=10)
    #plt.ylabel("TimeSolved", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    # Plot 2
    fig2, ax3 = plt.subplots()
    ax3.bar(tryList, relatedValues, width = 0.3, align='center')
    ax3.set_ylabel('Time pr. move', color='tab:red')
    ax3.tick_params(axis='y')
    plt.show()

cntr.mainRun(10)
cntr.pv
cntr.makeStatNumbers()
pvList = cntr.pvList
cntr.getStatKeys()
cntr.getStatValues()
cntr.getRelatedValues()
tryList = list(cntr.tryList)
relatedValues = list(cntr.relatedValues)
theTimes = list(cntr.theTimes)
makePlot()