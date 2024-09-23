from tkinter import Frame

def setupFrames(view):
    #frame for (add/remove) buttons and grid of tables
    buttonFrame = Frame(view)
    tableFrame = Frame(view)
    
    #show frames
    buttonFrame.pack(pady=10)
    tableFrame.pack(pady=10)

    return buttonFrame, tableFrame
