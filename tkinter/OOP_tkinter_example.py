# OOP style using tkinter
import tkinter as tk
from PIL import Image, ImageTk

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(tk.Frame):
    def __init__ (self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_Window()
        
    def init_Window(self):
        self.master.title('GUI')
        self.pack(fill=tk.BOTH, expand=1)
        
        # quitButton = tk.Button(self, text='Quit', command=self.client_exit)
        # # Placing the button on window
        # quitButton.place(x=0, y=0)
        
        # Create parent menu
        topbar_menu = tk.Menu(self.master)
        self.master.config(menu=topbar_menu)
        
        # Create sub menu
        file = tk.Menu(topbar_menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        topbar_menu.add_cascade(label='File', menu=file)
        
        edit = tk.Menu(topbar_menu)
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)
        topbar_menu.add_cascade(label='Edit', menu=edit)
        
    def client_exit(self):
        exit()
        
    def showImg(self):
        load = Image.open('./Tkinter Zetcode/lena_color512.jpg')
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        
    def showTxt(self):
        text = tk.Label(self, text='Hey there good lookin!')
        text.pack()
        
root = tk.Tk()
# Define width & height of main window
root.geometry("400x200")
app = Window(root)

root.mainloop()
  