import os 
from os.path import isfile, join
from os import listdir
  
# import filedialog module
from tkinter import filedialog
from  tkinter import *
from tkinter import filedialog
  
# Function for opening the
# file explorer window
def browseFiles():
    root = Tk()
    root.directory = filedialog.askdirectory()
    # Change label contents
    var.set("File Opened: "+root.directory)
    thepath.set(root.directory)
    print(thepath)


def changeFolder():
    dirpath =  thepath.get()
    strtodelete = stringTodelete.get()   
    files_no_ext = [".".join(f.split(".")) for f in os.listdir(dirpath) if isfile(join(dirpath, f))]
    for i in range(len(files_no_ext)):
        if strtodelete in files_no_ext[i]:
            temp = files_no_ext[i].replace(strtodelete,"")
            old_name = dirpath+"/"+files_no_ext[i]
            new_name = dirpath+"/"+temp
            os.rename(old_name,new_name)

    onlyfiles = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
    print(onlyfiles)


global screen
global stringTodelete
global stringTodelete_entry
global thepath
screen = Tk()
screen.geometry("300x250")
screen.title("Notes 1.0")
stringTodelete = StringVar()
thepath = StringVar()
var = StringVar()
var.set("Lior")

label_file_explorer = Label(screen,textvariable = var, bg = "grey", width = "200", height = "2", font = ("Calibri", 10)).pack()
Label(text = "").pack()
Button(screen,text = "Browse Files", height = "2", width = "20",command = browseFiles).pack()
Label(text = "").pack()
Label(screen, text = "Enter a string to delete : ").pack()
stringTodelete_entry = Entry(screen, textvariable = stringTodelete)
stringTodelete_entry.pack()
Label(text = "").pack()
Button(screen, text = "Submit", width = "10", height = "1", command = changeFolder).pack()
Button(screen,text = "Exit", height = "1", width = "10",command = screen.destroy).pack()
#Button(text = "Login", height = "2", width = "30", command = login).pack()
screen.mainloop()

