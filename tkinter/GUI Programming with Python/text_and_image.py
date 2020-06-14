import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="lena-color-small.png")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root, 
              justify=tk.RIGHT,  # justify within the label
              padx = 10, 
              text=explanation).pack(side="left")

root.mainloop()