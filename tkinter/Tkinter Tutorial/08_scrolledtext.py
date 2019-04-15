import tkinter as tk
import tkinter.scrolledtext as tkst

window = tk.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   

# create scrolledtext box
# wrap text at full words only
txt = tkst.ScrolledText(window, width=20, height=10, wrap='word')
txt.grid(column=0, row=0)
msg = '''A quick brown fox jumps over the lazy dog.
A quick brown fox jumps over the lazy dog.
A quick brown fox jumps over the lazy dog.
A quick brown fox jumps over the lazy dog.
A quick brown fox jumps over the lazy dog.
A quick brown fox jumps over the lazy dog.
A quick brown fox jumps over the lazy dog.
A quick brown fox jumps over the lazy dog.
'''
txt.insert('insert', msg)

window.mainloop()
