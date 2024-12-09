from PIL import Image, ImageTk

def addIcon():
    # Add button
    addImg = Image.open("images/add.png")
    resized_image = addImg.resize((80, 80), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_image) 
    
def removeIcon():
    #remove button
    removeImg = Image.open("images/remove.png")
    resized_image = removeImg.resize((80,80), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_image) 