import tkinter as tk

root = tk.Tk()
root.resizable(False, False)

label1 = tk.Label(root, text="Height")
label1.grid(sticky=tk.E)

label2 = tk.Label(root, text="Width")
label2.grid(sticky=tk.E)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

checkbutton = tk.Checkbutton(root, text="Preserve aspect")
checkbutton.grid(columnspan=2, sticky=tk.W)

load = tk.PhotoImage(file="cat-icon.png")
image = tk.Label(root, image=load)
image.grid(row=0, column=2, columnspan=2, rowspan=2,
           sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

button1 = tk.Button(root, text="Zoom in")
button1.grid(row=2, column=2)

button2 = tk.Button(root, text="Zoom out")
button2.grid(row=2, column=3)

root.mainloop()
