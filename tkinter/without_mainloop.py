import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title('Without Mainloop')

txt = tk.StringVar()
count = 0
txt.set(count)

label = ttk.Label(root, textvariable=txt)
label.pack()

try:
    while True:
        time.sleep(1)
        count += 1
        txt.set(count)
        #root.update_idletasks()
        root.update()
except:
    print("Program terminated!")
    root.destroy()
