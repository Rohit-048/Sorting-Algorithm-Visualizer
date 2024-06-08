import tkinter as tk
import random as rn
from tkinter import ttk
import time
# from tkinter import ttk

CANVAS_WIDTH, CANVAS_HEIGHT = (450, 250)

def reset():
    global canvas
    canvas.delete('all')
    ls = rn.sample(range(2,100),40)

    ln = len(ls)
    w = CANVAS_WIDTH/ln
    h = CANVAS_HEIGHT/max(ls)

    for i in range(ln):
        x1, x2 = w * i, w * (i+1)
        y1, y2 = 0, h * ls[i]

        canvas.create_rectangle(x1,y1,x2,y2,fill='red')


root = tk.Tk()
root.geometry("500x300")
canvas = tk.Canvas(root, height=CANVAS_HEIGHT,width=CANVAS_WIDTH)
canvas.pack(pady=10)

ttk.Button(root, text="reset",command=reset).pack()


root.mainloop()
# time.sleep(1)
