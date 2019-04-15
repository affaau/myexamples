'''Easily create GUI

https://www.youtube.com/watch?v=-jvDEbw3XOU&index=2&t=0s&list=PLamqrZ7b2mV4DXZsBJcAZK69Cc4suAKMu
'''
import tkinter as tk

window = tk.Tk()

# ("widthxheight")
window.geometry("600x600")

window.title("Hello Tktiner!")

# # width, height
# window.resizable(False, False)

# # to list all available configure keywords
# # >>> pprint(root.config())
# window.configure(background="red")

def first_function():
	text = "Hello World!"
	# create a Label widget
	text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 16))
	# sticky is like align, local the object to [N, E, S, W]
	text_output.grid(row=0, column=1, sticky="W")
	
def second_function():
	text = "New Message! New Function!"
	# create a Label object
	text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
	# 'padx', 'pady' add space externally
	text_output.grid(row=1, column=1, padx = 50, sticky="W")
	
# create Button widget 
first_button = tk.Button(text="Hello!", command=first_function)
# define location
first_button.grid(row=0, column=0, sticky="W")

second_button = tk.Button(text="Second Function", command=second_function)
second_button.grid(row=1, column=0, pady = 20, sticky="W")


if __name__ == "__main__":
	window.mainloop()