import Controller_MainController as mc
import tkinter as tk
# from tkinter import *
CheckVar1 = tk.IntVar
slide_min = 5
slide_max = 5

# todo fix so it is a list in dropmenu
mazeGeneratorOptions = ["one", "two", "three"]
mazeSolverOptions = ["one", "two", "three"]
Mazes = []
mazesList = []

############ CANVAS - Setup ############
HEIGHT = 700
WIDTH = 1400
MAZE_HEIGHT = 350
MAZE_WIDTH = 500

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

lower_frame = tk.Canvas(root, bg='white')
lower_frame.place(relx=0.5, rely=0.25, relwidth=LOWER_FRAME_SIZE,
                  relheight=0.75, anchor='n')

# lower_label = tk.Label(lower_frame)
# lower_label.place(relwidth=1, relheight=1)

listbox_frame = tk.Frame(right_frame)
listbox_frame.place(relx=0.2, rely=0.4,
                    relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.50)

############ FUNCTIONS ############


def draw_maze(selected_maze):
    print("Draw maze started")

    for y in range(len(selected_maze)):
        for x in range(len(selected_maze[y])):
            # Get the character at each x,y coordinate
            # NOTE the order of y and x in the next line
            character = selected_maze[y][x]
            # Calculate the screen x, y coordinates
            CUBE_SIZE = 25
            screen_x = (x * CUBE_SIZE)
            screen_y = (y * CUBE_SIZE)

            # Check if it is an 0 (representing a wall)
            if character == "0":
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="white", outline="black")
                print(str(character), screen_x,
                      screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE)
            # Check if it is an 1 (representing a wall)
            if character == "1":
                # lower_frame.create_rectangle(
                #     screen_x, screen_y, 24, 24, fill="white")
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="black", outline="white")
                print(str(character), screen_x,
                      screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE)
                # lower_frame.pack()
            # Check if it is an 2 (representing a wall)
            if character == "2":
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="green", outline="white")
                print(str(character), screen_x,
                      screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE)
                # lower_frame.pack()
            # Check if it is an 3 (representing a wall)
            if character == "3":
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="blue", outline="white")
                print(str(character), screen_x,
                      screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE)
                # lower_frame.pack()
    print("maze_draw done")

    lower_frame.place(lower_frame, anchor='n')


def mazeSelect():
    selected = Lb1.curselection()
    maze_number = 0
    if selected:
        for value in selected:
            maze_number = value
        print("Maze selected: " + str(maze_number))
        print(mazesList[0][0])
        draw_maze(mazesList[maze_number][0])
    else:
        mc1 = mc.MainController(0, 0)
        load_mazeList(mc1.getMazes())

# Placeholder function


def load_mazeList(mazesArray):
    global Mazes
    global mazesList
    mazesList = mazesArray
    for maze in mazesArray:
        Mazes.append(maze)
    Lb1.delete(0, tk.END)
    i = 1
    for m in Mazes:
        Lb1.insert(tk.END, "Maze number: " + str(i))
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
    print('Button set selected_maze data, data is:',
          a, "min size: ", b, "max size: ", c)


def saveMazeCheckbox(IntVar):
    print('Checkbox: save maze solution is:', CheckVar1)


def startMazeSolve():
    a = int(slide_min)
    b = int(slide_max)
    c = int(spinbox_SolveItterations.get())
    print('Button: maze solve start pushed')
    mCon = mc.MainController([a, b], c)
    mCon.runMain()
    mazesArray = mCon.getMazes()
    load_mazeList(mazesArray)


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

spinbox_SolveItterations = tk.Spinbox(left_frame, from_=1, to=40)
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
