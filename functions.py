from tkinter import Button, NSEW, simpledialog

# Global variables to manage table layout
columns = 5
rowCounter = 0
colCounter = 0
counter = 0
tables = []
removeFlag = False
table_positions = {}  # Dictionary to store table positions
table_orientations = {}  # Dictionary to store table orientations

def allFunctions(view, buttonFrame, tableFrame, addImg, removeImg, ros_node):
    global removeFlag

    # Define functions to add, remove, and select tables
    def addTable():
        global rowCounter, colCounter, counter
        counter += 1

        # Get position from user
        x = simpledialog.askfloat("Input Position", "Enter X position:")
        y = simpledialog.askfloat("Input Position", "Enter Y position:")
        if x is None or y is None:  # User canceled input
            counter -= 1
            return

        # Get orientation from user
        z_orient = simpledialog.askfloat("Input Orientation", "Enter Z orientation:")
        w_orient = simpledialog.askfloat("Input Orientation", "Enter W orientation:")
        if z_orient is None or w_orient is None:  # User canceled input
            counter -= 1
            return

        # Store the position and orientation
        table_positions[counter] = (x, y, 0.0)
        table_orientations[counter] = (z_orient, w_orient)

        # Add a new table button
        table = Button(tableFrame, text=counter, width=15, height=4,
                       bg="#851717", font="David 15 bold", command=lambda: selectTable(counter))
        table.grid(row=rowCounter, column=colCounter, padx=30, pady=30, sticky=NSEW)
        tables.append(table)
        colCounter += 1
        if colCounter == columns:
            colCounter = 0
            rowCounter += 1

    def removeMode():
        global removeFlag
        if removeFlag:
            removeFlag = False
            removeButton.config(bg="#dbe6d3")  # Reset button color
        else:
            removeFlag = True
            removeButton.config(bg="red")  # Indicate remove mode

    def selectTable(table_number):
        global removeFlag
        if removeFlag:
            removeTable(table_number)
            removeFlag = False
            removeButton.config(bg="#dbe6d3")
        else:
            if table_number in table_positions:
                x, y, z = table_positions[table_number]
                z_orient, w_orient = table_orientations[table_number]
                print(f"Publishing position: x={x}, y={y}, z={z}, orientation: z={z_orient}, w={w_orient}")
                # Publish the position and orientation
                ros_node.publish_position(x, y, z, z_orient, w_orient)

    def removeTable(table_number):
        global rowCounter, colCounter, counter

        # Find and remove the table button from UI and tables list
        table_widget = tables.pop(table_number - 1)
        table_widget.grid_forget()

        # Reset counter to the total number of remaining tables
        counter = len(tables)

        # Clear the grid and re-draw all tables
        for table in tables:
            table.grid_forget()  # Remove all tables temporarily

        # Reset grid counters
        rowCounter = 0
        colCounter = 0

        # Re-draw tables with updated numbers and positions
        for idx, table in enumerate(tables):
            table.config(text=idx + 1)  # Update table number
            table.grid(row=rowCounter, column=colCounter, padx=30, pady=30, sticky=NSEW)
            colCounter += 1
            if colCounter == columns:
                colCounter = 0
                rowCounter += 1

    # Add and remove table buttons
    addButton = Button(buttonFrame, image=addImg, fg="#851717", bg="#dbe6d3",
                       font="David 20 bold", padx=10, pady=3, command=addTable)

    removeButton = Button(buttonFrame, image=removeImg, fg="#851717", bg="#dbe6d3",
                          font="David 20 bold", padx=10, pady=3, command=removeMode)

    # Pack buttons in the frame
    addButton.pack(side="left", padx=20, pady=30)
    removeButton.pack(side="left", padx=20, pady=30)

