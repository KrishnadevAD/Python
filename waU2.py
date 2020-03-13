from tkinter import * #  the * select all the attributes of tkinter
 
window = Tk() # it is for the window
def clickhandle(): # to click the button
 print("you have clicked button")# to print out the message after clicking the button

btn=Button(window,bd=2,bg="red",fg="green",
            text="click",command=clickhandle)
btn.place(x=10,y=10)
window.mainloop() # for window  main