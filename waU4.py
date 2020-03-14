from tkinter import *
 
window = Tk()
 
def callback(event):
    c.create_oval(event.x - 5, event.y - 5, 
    event.x + 5, event.y + 5, fill="#558832")
def draw(event):
    c.create_oval(event.x - 5, event.y - 5, 
    event.x + 5, event.y + 5, fill="#000000")
def drawRectangle(event):
    global draw,x1,y1
    if draw:
        c.create_rectangle(x1, y1, event.x, event.y, fill="Red")
        draw = False
    else:
        x1 = event.x
        y1 = event.y
        draw = True
 
 
c = Canvas(window, width=400, height=400)
c.pack()
c.bind("<Button-1>", callback)
c.bind("<B1-Motion>", draw)
c.bind("<Button-3>", drawRectangle)
draw = False
x1 = 0
y1 = 0
window.mainloop()