'''Batch execute apps
Save a list of apps you want to execute all when running this script
List of executables are save in appSave.txt
'''
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.geometry("500x500")

apps = []


def fileSelect():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"),
                                                     ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        tk.Label(displayFrame, text=app, bg="yellow").pack()


def runApps():
    for app in apps:
        os.startfile(app)


displayFrame = tk.Frame(root, bg="green")
displayFrame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.2)

tk.Button(root, text="Select Files", command=fileSelect).pack()
tk.Button(root, text="Run Apps", command=runApps).pack()

# Read in previous saved file list, if exist
if os.path.isfile('appSave.txt'):
    with open('appSave.txt', 'r') as f:
        tmp = f.read().strip().split('\n')
        if tmp!="" and tmp!='\n':
            apps = tmp
    print(apps) 
    for app in apps:
        tk.Label(displayFrame, text=app, bg='yellow').pack()

root.mainloop()

# On close, save all executable files listed in the displayFrame 
with open("appSave.txt", "w") as f:
    for app in apps:
        f.write(app+'\n')
