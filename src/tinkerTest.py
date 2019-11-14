from tkinter import *
from tkinter import CHECKBUTTON, messagebox
"""
top = Tk()
def helloCallBack():
    msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.pack()
top.mainloop()
"""

"""
top = Tk()
CheckVar1 = IntVar()
def helloCallBack():
    msg = messagebox.showinfo( "CheckVar", CheckVar1.get())
C1 = Checkbutton(top, text = "Music", command = helloCallBack,
variable = CheckVar1, onvalue = 1, offvalue = 0, height=5,
width = 20)
C1.pack()
top.mainloop()
"""

def onclick():
    pass
top = Tk()
text = Text(top)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow",
foreground="blue")
text.tag_config("start", background="black",
foreground="green")
top.mainloop()