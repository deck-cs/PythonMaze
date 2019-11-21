import controller1
from Controller import MazeGenerator
from tkinter import *
from tkinter import messagebox

root = Tk(className="PythonMaze")


def MMaS():
    MazeText = controller1.makeMazeAndSolve(5)
    
    return MazeText



#MakeAndSolveButton
widget = Button(None, text='MakeAndSolve', command = MMaS)
widget.pack()


#TOPMENU
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

button = Button(root, text='Stop', width=25, command=root.destroy) 
button.pack() 

frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
redbutton = Button(frame, text = 'MMaS', fg ='red') 
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown') 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Blue', fg ='blue') 
bluebutton.pack( side = LEFT ) 
blackbutton = Button(bottomframe, text ='Black', fg ='black') 
blackbutton.pack( side = BOTTOM) 


"""
#CANVAS
w = Canvas(root, width=40, height=60) 
w.pack() 
canvas_height=20
canvas_width=200
y = int(canvas_height * 10) 
w.create_line(0, y, canvas_width, y ) 
"""

""" LABEL
w = Label(root, text='GeeksForGeeks.org!') 
w.pack() 
"""



#TEXTBOX - Should it show the same as in terminal?
T = Text(root, height=20, width=30) 
T.pack() 
T.insert(END, MMaS() ) 


root.mainloop()


"""
mb = Menubutton ( top, text="condiments")
mb.menu = Menu (mb)
mb["menu"] = mb.menu
mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton (label="mayo",
variable=mayoVar)
mb.menu.add_checkbutton (label="ketchup",
variable=ketchVar)
mb.pack()
top.mainloop()
"""