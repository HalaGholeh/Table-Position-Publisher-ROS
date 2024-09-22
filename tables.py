from tkinter import *

myView = Tk()
myView.title("Restaurant")
myView.attributes("-fullscreen" , True)

#Fames of my view button frame for grid and table Frame for add and remove buttons
buttonFrame =Frame(myView)
tableFrame = Frame(myView)

#variables
columns = 5
rowCounter = 0
colCounter = 0
counter = 0

#____________________Functions Part_______________________#
def addTable():
    global rowCounter , colCounter , counter
    counter += 1
    table = Button(tableFrame ,text=counter , width=15 , height=4,
                   bg="#851717", font="David 15 bold")
    table.grid(row=rowCounter , column=colCounter , padx=30 , pady=30, sticky=NSEW)
    
    colCounter += 1
    if colCounter == columns:
        colCounter = 0
        rowCounter += 1
    
    for i in range(columns):
        tableFrame.grid_columnconfigure(i, weight=1)
        

def removeTable():
    exit()

#_______________________End of Functions Part_____________________#
        
    
#buttons add and remove tables
addButton = Button(buttonFrame , text= "Add Table" , fg="#851717" , bg="#dbe6d3" , 
                   font="David 20 bold" , padx=10 , pady=3, command=addTable)

removeButton = Button(buttonFrame , text="Remove Table" , fg="#851717" , bg="#dbe6d3" , 
                   font="David 20 bold" , padx=10 , pady=3,)


addButton.pack(side=LEFT, padx=20,pady=30)
removeButton.pack(side=LEFT, padx=20, pady=30)


#show Frames
buttonFrame.pack(pady=10)
tableFrame.pack(pady=10)


myView.bind("<Escape>", lambda event: myView.attributes("-fullscreen" , False))
myView.mainloop()