import tkinter as tk
from tkinter import ttk
import webbrowser
# import speech_recognition as sr  # Haven't installed yet!
# from pygame import mixer  # Haven't installed yet!
# from keys import *   # Create your own file to keep API google keys

root = tk.Tk()
root.title("Universal Search Bar")
root.iconbitmap("microphone.ico")
style = ttk.Style()
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
style.theme_use('vista')

photo = tk.PhotoImage(file='microphone.png').subsample(6,6)

ttk.Label(root, text="Query: ").grid(row=0, column=0)
entry = ttk.Entry(root, width=50)
entry.grid(row=0, column=1, columnspan=3)
engine_select = tk.StringVar()

def callback():
    # Skip if not entry
    if entry.get() != '':
        # Open below link in a new tab of default browser
        if engine_select.get() == 'google':
            webbrowser.open("https://www.google.com/search?q=" + entry.get())
        elif engine_select.get() == 'duck':
            webbrowser.open("https://duckduckgo.com/?q=" + entry.get())
        elif engine_select.get() == 'ytb':
            webbrowser.open("https://www.youtube.com/results?search_query=" + entry.get())
        else:
            pass

def get(event):
    if entry.get() != '':
        if engine_select.get() == 'google':
            webbrowser.open("https://www.google.com/search?q=" + entry.get())
        elif engine_select.get() == 'duck':
            webbrowser.open("https://duckduckgo.com/?q=" + entry.get())
        elif engine_select.get() == 'ytb':
            webbrowser.open("https://www.youtube.com/results?search_query=" + entry.get())
        else:
            pass

def voice_search():
    # mixer.init()
    # mixer.music.load('chime1.mp3')
    # mixer.music.play()
    #
    # r = sr.Recognizer()
    # r.pause_threshold = 0.7
    # r.energy_threshold = 400

    # with sr.Microphone() as source:
    #     try:
    #         audio = r.listen(source, timeout=5)  # in second
    #         message = str(r.recognize_google(audio, key=google_api_key))
    #         mixer.music.load('chime2.mp3')
    #         mixer.music.play()
    #         entry.focus()
    #         entry.delete(0, END)
    #         entry.insert(0, message)
    #
    #         if engine_select.get() == 'google':
    #             webbrowser.open("https://www.google.com/search?q=" + message)
    #         elif engine_select.get() == 'duck':
    #             webbrowser.open("https://duckduckgo.com/?q=" + message)
    #         elif engine_select.get() == 'ytb':
    #             webbrowser.open("https://www.youtube.com/results?search_query=" + message)
    #         else:
    #             pass
    #     except sr.UnknownValueError:
    #         print('Google Speech Recognition could not understand audio')
    #     except sr.RequestError as e:
    #         print('Could not request results from Google Speech Recognition Service')
    #     else:
    #         pass

    pass

# Voice search Button
tk.Button(root, image=photo, command=voice_search, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken').grid(row=0, column=4)

# Press the button to trigger the function call
button = ttk.Button(root, text="Search", width=10, command=callback).grid(row=0, column=5)
# Press Return with the entry box, trigger the function call
entry.bind('<Return>', get)

rad1 = ttk.Radiobutton(root, text='Google', value='google', variable=engine_select)
rad1.grid(row=1, column=1, sticky=tk.W)
rad2 = ttk.Radiobutton(root, text='DuckDuckGo', value='duck', variable=engine_select)
rad2.grid(row=1, column=2, sticky=tk.W)
rad3 = ttk.Radiobutton(root, text='YouTube', value='ytb', variable=engine_select)
rad3.grid(row=1, column=3, sticky=tk.E)

# Putting the entry into focus when app starts
entry.focus()
# Keep the search bar stays on top of all windows
root.wm_attributes('-topmost', 1)
# Set google as default engine
engine_select.set('google')

root.mainloop()
