import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="lena-color-small.png")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

# TOP, BOTTOM, LEFT, RIGHT, CENTER
w = tk.Label(root, 
             justify=tk.LEFT,      
             compound = tk.RIGHT,  # effective have image on right
             text=explanation, 
             image=logo).pack(side="right")

root.mainloop()