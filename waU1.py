from tkinter import *
 
window = Tk()

fTop = Frame(window)
fTop.pack()

fBot= Frame(window)
fBot.pack(side=BOTTOM)
lbl1= Label(fTop,text="krishnadev is hacker")
lbl2= Label(fTop,text="Cybersecurity")
Lbl3= Label(fBot,text="Data scientist")
lbl1.pack()
lbl2.pack()
Lbl3.pack()

window.mainloop()