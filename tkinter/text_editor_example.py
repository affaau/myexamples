'''Text Editor

ref: https://www.youtube.com/watch?v=7PGFin30c4o&t=24s
'''
import tkinter as tk

class Menubar:

	def __init__(self, parent):
		font_specs = ("Helvetica", 14)
		
		menubar = tk.Menu(parent.master, font=font_specs)
		parent.master.config(menu=menubar)
		
		file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
		file_dropdown.add_command(label="New File", command=parent.new_file)
		file_dropdown.add_command(label="Open File", command=parent.open_file)
		file_dropdown.add_command(label="Save", command=parent.save)
		file_dropdown.add_command(label="Save as", command=parent.save_as)
		file_dropdown.add_separator()
		file_dropdown.add_command(label="Exit",
								  command=parent.master.destroy)
		
		menubar.add_cascade(label="File", menu=file_dropdown)
		

class PyText:
	'''main class'''
	def __init__(self, master):
		master.title("Untitled - PyText")
		master.geometry("1200x700")
		
		font_specs = ("Helvetica", 18)
		
		self.master = master

		self.textarea = tk.Text(master, font=font_specs)
		self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
		self.textarea.configure(yscrollcommand=self.scroll.set)
		self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
		
		self.menubar = Menubar(self)
		
	def set_window_title(Self):
		pass
		
	def new_file(self):
		pass
		
	def open_file(self):
		pass
		
	def save(self):
		pass
		
	def save_as(self):
		pass
		

if __name__ == '__main__':
	master = tk.Tk()
	pt = PyText(master)
	master.mainloop()
