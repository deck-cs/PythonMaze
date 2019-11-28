import tkinter as tk
from tkinter import *
CheckVar1 = IntVar
slide_min = 0
slide_max = 0

# todo fix so it is a list in dropmenu
mazeGeneratorOptions = ["one", "two", "three"]
mazeSolverOptions = ["one", "two", "three"]

############ CANVAS - Setup ############
HEIGHT = 600
WIDTH = 1200

MAZE_SIZE_RELX = 0.25
MAZE_SIZE_RELY = 0.15
WIDGET_SIZE_RELWIDTH = 0.6
WIDGET_SIZE_RELHEIGHT = 0.08

root = tk.Tk()
root.title('The amazing MAZE solver')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='landscape.gif')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

############ FRAMES ############

left_frame = tk.Frame(root, bg='grey')
left_frame.place(relwidth=0.25, relheight=1)

right_frame = tk.Frame(root, bg='grey')
right_frame.place(relx=0.75, relwidth=0.25, relheight=1)

top_frame = tk.Frame(root, bg='grey', bd='5')
top_frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='black', bd='10')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.50,
                  relheight=0.75, anchor='n')

lower_label = tk.Label(lower_frame)
lower_label.place(relwidth=1, relheight=1)


############ FUNCTIONS ############


def helloCallBack(entry):
    print("This is the entry:", entry)
    # msg = messagebox.showinfo("CheckVar", CheckVar1.get())

# Placeholder function


def slide_valueMin(value_slideMin):
    global slide_min
    slide_min = value_slideMin
    print("slide_valueMin: ", value_slideMin)


def slide_valueMax(value_slideMax):
    global slide_max
    slide_max = value_slideMax
    print("slide_valueMax: ", value_slideMax)


def setMazeData():
    # a = entry_MazeSizeX.get()
    # b = entry_MazeSizeY.get()
    c = spinbox_SolveItterations.get()
    d = slide_min
    e = slide_max
    print('Button set maze data, data is:', a,
          b, c, "min size: ", d, "max size: ", e)


def saveMazeCheckbox(IntVar):
    print('Checkbox: save maze solution is:', CheckVar1)


def startMazeSolve():
    print('Button: maze solve start pushed')


def TBD():
    pass

# this function should import the graphical maze


def MazeVar():
    pass

############ DropDown Menu ############


variable = StringVar()
variable.set("Choose Maze Generator")  # default value
dropDown_chooseMazeGenerator = OptionMenu(
    right_frame, variable, mazeGeneratorOptions)
dropDown_chooseMazeGenerator.place(
    relx=0.2, rely=0.25, relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.1)

variable2 = StringVar()
variable2.set("Choose Maze Solver")  # default value
dropDown_chooseMazeGenerator = OptionMenu(
    right_frame, variable2, "one", "two", "three")
dropDown_chooseMazeGenerator.place(
    relx=0.2, rely=0.4, relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.1)

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

checkbox_saveData = tk.Checkbutton(top_frame, text="Save data to file", command=lambda: saveMazeCheckbox(IntVar),
                                   variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=15)
checkbox_saveData.place(relx=0.5, relwidth=0.25, relheight=1)

############ INPUTS // ENTRY ############


# entry_MazeSizeX = tk.Entry(left_frame, bd=1)
# entry_MazeSizeX.insert(0, 'Length of maze')
# entry_MazeSizeX.place(relx=0.1, rely=0.25, relwidth=0.6, relheight=0.06)

# entry_MazeSizeY = tk.Entry(left_frame, bd=1)
# entry_MazeSizeY.insert(0, 'Hight of maze')
# entry_MazeSizeY.place(relx=0.1, rely=0.35, relwidth=0.6, relheight=0.06)

# entry_SolveItterations = tk.Entry(left_frame, bd=1)
# entry_SolveItterations.insert(0, 'How many time to solve?')
# entry_SolveItterations.place(relx=0.1, rely=0.2, relwidth=0.6, relheight=0.06)

spinbox_SolveItterations = tk.Spinbox(left_frame, from_=0, to=40)
spinbox_SolveItterations.place(
    relx=MAZE_SIZE_RELX, rely=0.3, relwidth=WIDGET_SIZE_RELWIDTH, relheight=WIDGET_SIZE_RELHEIGHT)


############ LABELS ############

left_label = tk.Label(left_frame, text='Select minimum size of maze')
left_label.place(relx=MAZE_SIZE_RELX, rely=0.38, relwidth=WIDGET_SIZE_RELWIDTH,
                 relheight=WIDGET_SIZE_RELHEIGHT)

left_label = tk.Label(left_frame, text='Select maximum size of maze')
left_label.place(relx=MAZE_SIZE_RELX, rely=0.54, relwidth=WIDGET_SIZE_RELWIDTH,
                 relheight=WIDGET_SIZE_RELHEIGHT)

# left_label = tk.Label(left_frame, bg='blue', text='LEFT LABEL FRAME')
# left_label.place(relwidth=1, relheight=0.2)

# right_label = tk.Label(right_frame, bg='red', text='RIGHT LABEL FRAME')
# right_label.place(relwidth=1, relheight=1)


############ BUTTONS ############

buttonStartMaze = tk.Button(top_frame, text='Solve maze(s)', bd=5,
                            command=lambda: startMazeSolve())
buttonStartMaze.place(relx=0.19, relwidth=0.3, relheight=1)

buttonStartMaze = tk.Button(left_frame, text='Set data', bd=5,
                            command=lambda: setMazeData())
buttonStartMaze.place(relx=MAZE_SIZE_RELX, rely=MAZE_SIZE_RELY,
                      relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.1)

############ Main Loop ############
root.mainloop()
