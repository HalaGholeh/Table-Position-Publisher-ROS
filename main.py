from tkinter import *
from frames import setupFrames
from functions import allFunctions
from icons import addIcon,removeIcon

#main view
myView = Tk()
myView.title("Restaurant")
myView.attributes("-fullscreen", True)

#button and table frames
buttonFrame, tableFrame = setupFrames(myView)

#call icons
add = addIcon()
remove = removeIcon()


# Call allFunctions to set up buttons and functions
allFunctions(myView, buttonFrame, tableFrame, add, remove)

# Bind the Escape key to exit fullscreen
myView.bind("<Escape>", lambda event: myView.attributes("-fullscreen", False))

myView.mainloop()
