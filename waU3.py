from tkinter import*
window = Tk()
window.title("krishnadev")

mainMenu = Menu(window) #main menu inside the window

window.config(menu=mainMenu) #configuring the main menu inside the  window

fileMenu=Menu(mainMenu) # creting the child menu ( file menu ) of the main menu 
mainMenu.add_cascade(label="file", menu=fileMenu)
fileMenu.add_command(label="open")
fileMenu.add_separator() # .add_separator is used to add the separate line betwn the  dropdown menu
fileMenu.add_command(label="save")
fileMenu.add_separator()
fileMenu.add_command(label="Delete")

editMenu=Menu(mainMenu)# editmenu is the child  menu of the mani menu
mainMenu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redu")
editMenu.add_command(label="Edit file")

def test():# definig the test function to print out the command 
   print("do what i said")
selectiionMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Selection",menu=selectiionMenu)
selectiionMenu.add_command(label="Select all" ,command=test)
selectiionMenu.add_separator()
selectiionMenu.add_command(label="Expand")
selectiionMenu.add_separator()
selectiionMenu.add_command(label="Shrink")


window.mainloop()