'''Play media using system default player

ref: https://python-forum.io/Thread-dealing-with-spaces-in-file-names
'''
import subprocess
import tkinter as tk
from tkinter import filedialog


# Select file from Window explorer
root = tk.Tk()
root.withdraw()

# Pick the media you would like to play
media_file = filedialog.askopenfilename()
root.destroy()

# Method 1
#subprocess.run(('cmd', '/C', 'start', '', media_file))

# Method 2 - cross-platform trick
import webbrowser

webbrowser.open(media_file)
# or use raw text direct input
#webbrowser.open(r"C:\Users\baba\Music\I'll Be There.mp3")
