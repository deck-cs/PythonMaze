import tkinter
import tkinter as tk

master = tk.Tk()

w = tk.Canvas(master, width=200, height=100)

w.create_rectangle(0, 0, 25, 25, fill="black", outline="white")
w.create_rectangle(25, 0, 50, 25, fill="black", outline="white")
w.pack()
tk.mainloop()
