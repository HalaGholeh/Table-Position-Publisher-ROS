from tkinter import Button, NSEW

# Global variables to manage table layout
columns = 5
rowCounter = 0
colCounter = 0
counter = 0
tables = []
removeFlag = False

def allFunctions(view, buttonFrame, tableFrame, addImg, removeImg):
    global removeFlag
    
    # Define functions to add, remove, and select tables
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

    def removeMode():
        global removeFlag
        removeFlag = True
        removeButton.config(bg="red")

    def selectTable(table):
        global removeFlag
        if removeFlag:
            removeTable(table)
            removeFlag = False
            removeButton.config(bg="#dbe6d3")

    def removeTable(table):
        table.grid_forget()
        tables.remove(table)

    # Add and remove table buttons
    addButton = Button(buttonFrame, image=addImg, fg="#851717", bg="#dbe6d3", 
                       font="David 20 bold", padx=10, pady=3, command=addTable)

    removeButton = Button(buttonFrame, image=removeImg, fg="#851717", bg="#dbe6d3", 
                          font="David 20 bold", padx=10, pady=3, command=removeMode)

    # Pack buttons in the frame
    addButton.pack(side="left", padx=20, pady=30)
    removeButton.pack(side="left", padx=20, pady=30)
