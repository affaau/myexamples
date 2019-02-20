from tkinter import *

parent = Tk()

l = StringVar()
Label(parent, textvariable=l).pack()
l.set("Enter your Password")

def b_callback():
    l.set(e.get())
    e.set("")

Button(parent, text="Update", command=b_callback).pack()

def toggle():
    if cb.get():
        c['text'] = 'checked'
    else:
        c['text'] = 'unchecked'
    
cb = BooleanVar()
c = Checkbutton(parent, text="unchecked", variable=cb, onvalue=True, offvalue=False, command=toggle)
c.pack()

e = StringVar()
Entry(parent, width=30, textvariable=e).pack()

r = StringVar()
r.set(2)
Radiobutton(parent, text="Male", variable=r, value=1).pack()
Radiobutton(parent, text="Female", variable=r, value=2).pack()

var = StringVar(parent)
var.set("Select Country")
OptionMenu(parent, var, "Select Country", "USA", "UK", "India", "Others").pack()

scrollbar = Scrollbar(parent)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(parent, yscrollcommand=scrollbar.set)
for i in range(50):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

parent.mainloop()
