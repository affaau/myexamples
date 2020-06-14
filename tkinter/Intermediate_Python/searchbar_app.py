import tkinter as tk
from tkinter import ttk
import webbrowser

root = tk.Tk()
root.title("Universal Search Bar")
root.iconbitmap("search.ico")
style = ttk.Style()
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
style.theme_use('vista')

ttk.Label(root, text="Query: ").grid(row=0, column=0)
entry = ttk.Entry(root, width=50)
entry.grid(row=0, column=1)
engine_select = tk.StringVar()

def callback():
    # Open below link in a new tab of default browser
    if engine_select.get() == 'google':
        webbrowser.open("https://www.google.com/search?q=" + entry.get())
    elif engine_select.get() == 'duck':
        webbrowser.open("https://duckduckgo.com/?q=" + entry.get())

def get(event):
    if engine_select.get() == 'google':
        webbrowser.open("https://www.google.com/search?q=" + entry.get())
    elif engine_select.get() == 'duck':
        webbrowser.open("https://duckduckgo.com/?q=" + entry.get())

# Press the button to trigger the function call
button = ttk.Button(root, text="Search", width=10, command=callback).grid(row=0, column=2)
# Press Return with the entry box, trigger the function call
entry.bind('<Return>', get)

rad1 = ttk.Radiobutton(root, text='Google', value='google', variable=engine_select)
rad1.grid(row=1, column=1, sticky=tk.W)
rad2 = ttk.Radiobutton(root, text='DuckDuckGo', value='duck', variable=engine_select)
rad2.grid(row=1, column=1, sticky=tk.E)

# Putting the entry into focus when app starts
entry.focus()
# Keep the search bar stays on top of all windows
root.wm_attributes('-topmost', 1)
# Set google as default engine
engine_select.set('google')

root.mainloop()
