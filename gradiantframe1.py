from GradiantFrame import GradientFrame
from tkinter import *

root = Tk()
root.geometry("700x700")
gf = GradientFrame(root, colors = ("darkblue", "lightblue"), width = 800, height = 600)
gf.config(direction = gf.left2right)
b1 = Button(root,text="test")
b1.place(x= 50 , y = 50)
gf.pack()
root.mainloop()