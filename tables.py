from tkinter import *

myView = Tk()
myView.title("Restaurant")
myView.attributes("-fullscreen", True)

# Frame for buttons (add/remove) and table grid
buttonFrame = Frame(myView)
tableFrame = Frame(myView)

# Variables
columns = 5
rowCounter = 0
colCounter = 0
counter = 0
tables = [] 
removeFlag = False 
#____________________Functions Part_______________________#

# Add a new table
def addTable():
    global rowCounter, colCounter, counter
    counter += 1
    table = Button(tableFrame, text=counter, width=15, height=4,
                   bg="#851717", font="David 15 bold", command=lambda: selectTable(table))
    table.grid(row=rowCounter, column=colCounter, padx=30, pady=30, sticky=NSEW)
    
    tables.append(table) 
    
    colCounter += 1
    if colCounter == columns:
        colCounter = 0
        rowCounter += 1
    
    for i in range(columns):
        tableFrame.grid_columnconfigure(i, weight=1)

# Activate remove mode
def removeMode():
    global removeFlag
    removeFlag = True
    removeButton.config(bg="red")

# Handle table selection for removal
def selectTable(table):
    global removeFlag
    if removeFlag:
        removeTable(table)
        removeFlag = False
        removeButton.config(bg="#dbe6d3")  # Reset remove button color
    #else to send the position 

# Remove the selected table
def removeTable(table):
    table.grid_forget()  # Remove the button from the grid
    tables.remove(table)  # Remove the table from the list

#_______________________End of Functions Part_____________________#
        
# Add and remove table buttons
addButton = Button(buttonFrame, text="Add Table", fg="#851717", bg="#dbe6d3", 
                   font="David 20 bold", padx=10, pady=3, command=addTable)

removeButton = Button(buttonFrame, text="Remove Table", fg="#851717", bg="#dbe6d3", 
                      font="David 20 bold", padx=10, pady=3, command=removeMode)

# Pack buttons in the frame
addButton.pack(side=LEFT, padx=20, pady=30)
removeButton.pack(side=LEFT, padx=20, pady=30)

# Show Frames
buttonFrame.pack(pady=10)
tableFrame.pack(pady=10)

# Bind the Escape key to exit fullscreen
myView.bind("<Escape>", lambda event: myView.attributes("-fullscreen", False))

myView.mainloop()
