import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk


class PageThree(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    label = tk.Labek(self, text='Graph Page!', font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = ttk.Button(self, text = 'Back to Home', command=lambda: print('homebutton pushed'))
    button1.pack




# def makePlots(self):
#         fig1, ax1 = plt.subplots()
#         plt.xticks(rotation=45)
#         ax1.set_ylabel('Time for solve', color='tab:blue')
#         # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
#         ax1.bar(self.tryList, self.theTimes, width=0.5, align='center')
#         ax2 = ax1.twinx()
#         ax2.bar(self.tryList, self.pvListFinal,
#                 width=0.3, align='edge', color='orange')
#         ax2.set_ylabel('Attempts', color='tab:orange')
#         ax2.tick_params(axis='y')
#         # plt.ticklabel_format(useOffset=False)
#         #  plt.axis([0, len(solvingTimes)+1, 0, max(theTimes)+0.01])  # axis(x-min, x-max, y-min, y-max)
#         plt.title("Barplot Time to solve and places visited", fontsize=10)
#         plt.xlabel("Attempt", fontsize=10)
#         #plt.ylabel("TimeSolved", fontsize=10)
#         plt.tick_params(axis='both', which='major', labelsize=10)
#         # Plot 2
#         fig2, ax3 = plt.subplots()
#         plt.xticks(rotation=45)
#         plt.title("Time over places visited")
#         plt.xlabel("Attempt", fontsize=10)
#         ax3.bar(self.tryList, self.relatedValues, width=0.3, align='center')
#         ax3.set_ylabel('Time pr. move', color='tab:red')
#         ax3.tick_params(axis='y')
#         plt.show()
