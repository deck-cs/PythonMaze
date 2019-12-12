import Controller_MainController as mc
import tkinter as tk
from tkinter.messagebox import showwarning

############ GLOBAL - Varibels ############
CheckVar1 = tk.IntVar
slide_min = 5
slide_max = 5
Mazes = []
mazesList = []

############ CANVAS - Setup ############
HEIGHT = 800
WIDTH = 1200
MAZE_HEIGHT = 350
MAZE_WIDTH = 500

MAZE_SIZE_RELX = 0.1
MAZE_SIZE_RELY = 0.15
WIDGET_SIZE_RELWIDTH = 0.8
WIDGET_SIZE_RELHEIGHT = 0.07
WIDGET_LABEL_RELHEIGHT = 0.05
# Frame sizes in %
LEFT_FRAME_SIZE = 0.25
RIGHT_FRAME_SIZE = 0.25
TOP_FRAME_SIZE = 0.5
LOWER_FRAME_SIZE = 0.5


BUTTON_COLOR = "#568FE5"  # #DE3E3E -rød
BUTTON_TEXT_COLOR = "white"

root = tk.Tk()
root.title('The amazing MAZE solver')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

############ FRAMES ############

left_frame = tk.Frame(root, bg='grey')
left_frame.place(relwidth=LEFT_FRAME_SIZE, relheight=1)

right_frame = tk.Frame(root, bg='grey')
right_frame.place(relx=0.75, relwidth=RIGHT_FRAME_SIZE, relheight=1)

top_frame = tk.Frame(root, bg='grey', bd='5')
top_frame.place(relx=0.5, rely=0, relwidth=TOP_FRAME_SIZE,
                relheight=0.2, anchor='n')

lower_frame = tk.Canvas(root, bg='white')
lower_frame.place(relx=0.5, rely=0.2, relwidth=LOWER_FRAME_SIZE,
                  relheight=0.75, anchor='n')

bottom_frame = tk.Frame(root, bg='grey')
bottom_frame.place(relx=0.5, rely=0.95, relwidth=LOWER_FRAME_SIZE,
                   relheight=0.05, anchor='n')

listbox_frame = tk.Frame(right_frame)
listbox_frame.place(relx=0.1, rely=0.3,
                    relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.50)

############ FUNCTIONS ############


def clearMazeView():
    lower_frame.delete("all")


def draw_maze(selected_maze):
    print("Draw maze started")

    for y in range(len(selected_maze)):
        for x in range(len(selected_maze[y])):
            # Get the character at each x,y coordinate
            # NOTE the order of y and x in the next line
            character = selected_maze[y][x]
            # Calculate the screen x, y coordinates
            CUBE_SIZE = lower_frame.winfo_width()/len(selected_maze[y])
            screen_x = (x * CUBE_SIZE)
            screen_y = (y * CUBE_SIZE)

            # Check if it is an 0 (representing a wall)
            if character == "0":
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="white")
            # Check if it is an 1 (representing a wall)
            if character == "1":
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="black")

            # Check if it is an 2 (representing a wall)
            if character == "2":
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="gold")
            # Check if it is an 3 (representing a wall)
            if character == "3":
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="green")
            if character == "4":
                lower_frame.create_rectangle(
                    screen_x, screen_y, screen_x+CUBE_SIZE, screen_y+CUBE_SIZE, fill="blue")

    print("maze_draw done")

    lower_frame.place()


def mazeSelect():
    selected = Lb1.curselection()
    maze_number = 0
    if selected:
        for value in selected:
            maze_number = value
        print("Maze selected: " + str(maze_number))
        print(mazesList[0][0])
        clearMazeView()
        draw_maze(mazesList[maze_number][0])
    else:
        mc1 = mc.MainController(0, 0)
        load_mazeList(mc1.getMazes())


def load_mazeList(mazesArray):
    global mazesList
    global Mazes
    mazesList = mazesArray
    Lb1.delete(0, tk.END)
    for maze in mazesArray:
        Mazes.append(maze)
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


def saveMazeCheckbox(IntVar):
    print('Checkbox: save maze solution is:', CheckVar1)


def startMazeSolve():
    global Mazes
    try:
        Mazes = []
        a = int(spinbox_SolveItterations.get())
        b = int(slide_min)
        c = int(slide_max)
        print('Button: maze solve start pushed')
        assert (c >= b), "Maximum value must be larger than minimum value"
        print('Button: maze solve start pushed, data is: ',
              a, "min size: ", b, "max size: ", c)
        mazesizes = []
        x = c/5
        for y in range(int(x)):
            g = b * (y+1)
            mazesizes.append(g)
        mazesizes.sort()
        mCon = mc.MainController(mazesizes, a)
        mCon.runMain()
        mazesArray = mCon.getMazes()
        load_mazeList(mazesArray)
    except AssertionError:
        showwarning("Du har fucket op Sonny Boy",
                    "Maximum value must be larger than minimum value")
    except Exception as e:
        showwarning("Du har fucket op Sonny Boy", e)

############ SCALE SLIDER ############


minMazeSize_scale = tk.Scale(left_frame, orient='horizontal', from_=5,
                             to=35, resolution=5, command=slide_valueMin)
minMazeSize_scale.place(relx=MAZE_SIZE_RELX, rely=0.39, relwidth=WIDGET_SIZE_RELWIDTH,
                        relheight=WIDGET_SIZE_RELHEIGHT)

maxMazeSize_scale = tk.Scale(left_frame, orient='horizontal', from_=5,
                             to=35, resolution=5, command=slide_valueMax)
maxMazeSize_scale.place(relx=MAZE_SIZE_RELX, rely=0.53, relwidth=WIDGET_SIZE_RELWIDTH,
                        relheight=WIDGET_SIZE_RELHEIGHT)

############ CHECKBOX ############

checkbox_saveData = tk.Checkbutton(top_frame, text="Save data to file", command=lambda: saveMazeCheckbox(tk.IntVar),
                                   variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=15)
checkbox_saveData.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.25)

############ SPINBOX ############

spinbox_SolveItterations = tk.Spinbox(left_frame, from_=1, to=40)
spinbox_SolveItterations.place(
    relx=MAZE_SIZE_RELX, rely=0.27, relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.05)

############ LISTBOX ############

scroolbar = tk.Scrollbar(listbox_frame)
Lb1 = tk.Listbox(listbox_frame, yscrollcommand=scroolbar.set)

############ LABELS ############
left_label = tk.Label(left_frame, text='Select number of itterations')
left_label.place(relx=MAZE_SIZE_RELX, rely=0.2, relwidth=WIDGET_SIZE_RELWIDTH,
                 relheight=WIDGET_SIZE_RELHEIGHT)

left_label = tk.Label(left_frame, text='Select minimum size of maze')
left_label.place(relx=MAZE_SIZE_RELX, rely=0.33, relwidth=WIDGET_SIZE_RELWIDTH,
                 relheight=WIDGET_LABEL_RELHEIGHT)

left_label = tk.Label(left_frame, text='Select maximum size of maze')
left_label.place(relx=MAZE_SIZE_RELX, rely=0.47, relwidth=WIDGET_SIZE_RELWIDTH,
                 relheight=WIDGET_LABEL_RELHEIGHT)

title_label = tk.Label(top_frame, text='THE AMAZING MAZE SOLVER')
title_label.place(relx=0.25, rely=0.1, relheight=0.25, relwidth=0.5)

title_listbox_label = tk.Label(right_frame, text='List of mazes')
title_listbox_label.place(
    relx=0.1, rely=0.2, relheight=0.07, relwidth=WIDGET_SIZE_RELWIDTH)

bottom_label = tk.Label(bottom_frame, text='DECK-CS © 2019')
bottom_label.place(relx=0.5, rely=0.15, anchor='n')

############ BUTTONS ############

buttonStartMaze = tk.Button(top_frame, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, text='Solve maze(s)', bd=5,
                            command=lambda: startMazeSolve())
buttonStartMaze.place(relx=0.19, rely=0.5, relwidth=0.3, relheight=0.25)

buttonSelectMaze = tk.Button(right_frame, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, text='Select maze', bd=5,
                             command=mazeSelect)
buttonSelectMaze.place(relx=0.1, rely=0.82,
                       relwidth=WIDGET_SIZE_RELWIDTH, relheight=0.05)

############ Main Loop ############
root.mainloop()
