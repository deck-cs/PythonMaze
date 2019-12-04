import Controller.MainController as mc
import tkinter as tk
# from tkinter import *
CheckVar1 = tk.IntVar
slide_min = 0
slide_max = 0

# todo fix so it is a list in dropmenu
mazeGeneratorOptions = ["one", "two", "three"]
mazeSolverOptions = ["one", "two", "three"]
Mazes = ["one", "two", "three", "four", "five", "six"]

############ CANVAS - Setup ############
HEIGHT = 700
WIDTH = 1400

MAZE_SIZE_RELX = 0.25
MAZE_SIZE_RELY = 0.15
WIDGET_SIZE_RELWIDTH = 0.6
WIDGET_SIZE_RELHEIGHT = 0.07
# Frame sizes in %
LEFT_FRAME_SIZE = 0.25
RIGHT_FRAME_SIZE = 0.25
TOP_FRAME_SIZE = 0.5
LOWER_FRAME_SIZE = 0.5


BUTTON_COLOR = "#DE3E3E"
BUTTON_TEXT_COLOR = "white"

root = tk.Tk()
root.title('The amazing MAZE solver')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='landscape.gif')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

############ FRAMES ############

left_frame = tk.Frame(root, bg='grey')
left_frame.place(relwidth=LEFT_FRAME_SIZE, relheight=1)

right_frame = tk.Frame(root, bg='grey')
right_frame.place(relx=0.75, relwidth=RIGHT_FRAME_SIZE, relheight=1)

top_frame = tk.Frame(root, bg='grey', bd='5')
top_frame.place(relx=0.5, rely=0, relwidth=TOP_FRAME_SIZE,
                relheight=0.25, anchor='n')

lower_frame = tk.Frame(root, bg='black', bd='10')
lower_frame.place(relx=0.5, rely=0.25, relwidth=LOWER_FRAME_SIZE,
                  relheight=0.75, anchor='n')

lower_label = tk.Label(lower_frame)
lower_label.place(relwidth=1, relheight=1)

listbox_frame = tk.Frame(right_frame)
listbox_frame.place(relx=0.2, rely=0.4,
                    relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.50)

############ FUNCTIONS ############


def mazeSelect():
    selected = Lb1.curselection()
    maze_number = 0
    if selected:
        for value in selected:
            maze_number = value
        print("Maze selected: " + str(maze_number))
    else:
        load_mazeList()


def helloCallBack(entry):
    print("This is the entry:", entry)
    # msg = messagebox.showinfo("CheckVar", CheckVar1.get())

# Placeholder function


def load_mazeList():
    global Mazes
    Lb1.delete(0, tk.END)
    # TODO insert function here that loads file

    i = 1
    for m in Mazes:
        Lb1.insert(tk.END, "Maze number: " + str(i) + " - Maze: " + str(m))
        i += 1
    Lb1.place(relwidth=1, relheight=1)
    scroolbar.config(command=Lb1.yview)


def slide_valueMin(value_slideMin):
    global slide_min
    slide_min = value_slideMin
    print("slide_valueMin: ", value_slideMin)


def slide_valueMax(value_slideMax):
    global slide_max
    slide_max = value_slideMax
    print("slide_valueMax: ", value_slideMax)


def setMazeData():
    a = spinbox_SolveItterations.get()
    b = slide_min
    c = slide_max
    print('Button set maze data, data is:',
          a, "min size: ", b, "max size: ", c)


def saveMazeCheckbox(IntVar):
    print('Checkbox: save maze solution is:', CheckVar1)


def startMazeSolve():
    a = spinbox_SolveItterations.get()
    b = slide_min
    c = slide_max
    print('Button: maze solve start pushed')
    load_mazeList()
    mc.MainController([a, b], c)


def TBD():
    pass

# this function should import the graphical maze


def MazeVar():
    pass

############ DropDown Menu ############


variable = tk.StringVar()
variable.set("Choose Maze Generator")  # default value
dropDown_chooseMazeGenerator = tk.OptionMenu(
    right_frame, variable, mazeGeneratorOptions)
dropDown_chooseMazeGenerator.place(
    relx=0.2, rely=0.02, relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.1)

variable2 = tk.StringVar()
variable2.set("Choose Maze Solver")  # default value
dropDown_chooseMazeGenerator = tk.OptionMenu(
    right_frame, variable2, "one", "two", "three")
dropDown_chooseMazeGenerator.place(
    relx=0.2, rely=0.13, relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.1)

############ MAZE PRINT IN MIDDLE ############

maze_label = tk.Label(lower_frame, text="MAZE IS GOING TO BE HERE")
maze_label.place(relwidth=1, relheight=1)

############ SCALE SLIDER ############

minMazeSize_scale = tk.Scale(left_frame, orient='horizontal', from_=5,
                             to=35, resolution=5, command=slide_valueMin)
minMazeSize_scale.place(relx=MAZE_SIZE_RELX, rely=0.44, relwidth=WIDGET_SIZE_RELWIDTH,
                        relheight=WIDGET_SIZE_RELHEIGHT)

maxMazeSize_scale = tk.Scale(left_frame, orient='horizontal', from_=5,
                             to=35, resolution=5, command=slide_valueMax)
maxMazeSize_scale.place(relx=MAZE_SIZE_RELX, rely=0.60, relwidth=WIDGET_SIZE_RELWIDTH,
                        relheight=WIDGET_SIZE_RELHEIGHT)

############ CHECKBOX ############

checkbox_saveData = tk.Checkbutton(top_frame, text="Save data to file", command=lambda: saveMazeCheckbox(tk.IntVar),
                                   variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=15)
checkbox_saveData.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.25)

############ SPINBOX ############

spinbox_SolveItterations = tk.Spinbox(left_frame, from_=0, to=40)
spinbox_SolveItterations.place(
    relx=MAZE_SIZE_RELX, rely=0.3, relwidth=WIDGET_SIZE_RELWIDTH, relheight=WIDGET_SIZE_RELHEIGHT)

############ LISTBOX ############

scroolbar = tk.Scrollbar(listbox_frame)
Lb1 = tk.Listbox(listbox_frame, yscrollcommand=scroolbar.set)

############ LABELS ############

left_label = tk.Label(left_frame, text='Select minimum size of maze')
left_label.place(relx=MAZE_SIZE_RELX, rely=0.38, relwidth=WIDGET_SIZE_RELWIDTH,
                 relheight=WIDGET_SIZE_RELHEIGHT)

left_label = tk.Label(left_frame, text='Select maximum size of maze')
left_label.place(relx=MAZE_SIZE_RELX, rely=0.54, relwidth=WIDGET_SIZE_RELWIDTH,
                 relheight=WIDGET_SIZE_RELHEIGHT)

title_label = tk.Label(top_frame, text='THE AMAZING MAZE SOLVER')
title_label.place(relx=0.25, rely=0.1, relheight=0.25, relwidth=0.5)

title_listbox_label = tk.Label(right_frame, text='List of mazes')
title_listbox_label.place(
    relx=0.2, rely=0.32, relheight=0.07, relwidth=WIDGET_SIZE_RELWIDTH)

############ BUTTONS ############

buttonStartMaze = tk.Button(top_frame, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, text='Solve maze(s)', bd=5,
                            command=lambda: startMazeSolve())
buttonStartMaze.place(relx=0.19, rely=0.6, relwidth=0.3, relheight=0.25)

buttonStartMaze = tk.Button(left_frame, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, text='Set data', bd=5,
                            command=lambda: setMazeData())
buttonStartMaze.place(relx=MAZE_SIZE_RELX, rely=MAZE_SIZE_RELY,
                      relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.1)

buttonSelectMaze = tk.Button(right_frame, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, text='Select maze', bd=5,
                             command=mazeSelect)
buttonSelectMaze.place(relx=0.2, rely=0.92,
                       relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.05)

############ Main Loop ############
root.mainloop()
