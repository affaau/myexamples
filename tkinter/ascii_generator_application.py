'''Ascii Generator application
            _____  _____ _____ _____    _____                           _             
     /\    / ____|/ ____|_   _|_   _|  / ____|                         | |            
    /  \  | (___ | |      | |   | |   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   / /\ \  \___ \| |      | |   | |   | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  / ____ \ ____) | |____ _| |_ _| |_  | |__| |  __/ | | |  __/ | | (_| | |_ (_) | |   
 /_/    \_\_____/ \_____|_____|_____|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                      

ref: https://www.youtube.com/watch?v=73WpYMulq2k&list=PLamqrZ7b2mV4DXZsBJcAZK69Cc4suAKMu&index=3&t=0s

resource: https://artii.herokuapp.com/
'''
import requests
import tkinter as tk

window = tk.Tk()
window.geometry("900x550")
window.title("ASCII ART DOWNLOADER")
# (column_index 0, expand with weight 1)
# take up the whole space
window.grid_columnconfigure(0, weight=1)

welcome_label = tk.Label(window,
						text="Welcome! Insert a Word or Sentence to Download:",
						font=("Helvetical", 15))
welcome_label.grid (row=0, column=0, sticky="N", padx=20, pady=10)

text_input = tk.Entry()
# take up as much space as possible at W & E
text_input.grid(row=1, column=0, stick="WE", padx=10)

def download_ascii():
	if text_input.get():
		user_input = text_input.get()
		payload = {"text": user_input}
		response = requests.get("https://artii.herokuapp.com/make",
								params=payload)
		text_response = response.text
	else:
		text_response = "Text Input Can't Be Empty!"
	
	textwidget = tk.Text()
	textwidget.insert(tk.END, text_response)
	textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
	
	credits_label = tk.Label(window, text="ascii art by artii.herokuapp.com")
	credits_label.grid(row=4, column=0, sticky="S", padx=10)

download_button = tk.Button(text="DOWNLOAD ASCII ART", command=download_ascii)
download_button.grid(row=2, column=0, stick="WE", padx=10, pady=10)

if __name__ == "__main__":
	window.mainloop()
	