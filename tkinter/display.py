'''GUI template for ST Baren analysis application

Feel free to reference, improve & enhance it
'''
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


## Window setup
window = tk.Tk()
window.resizable(0, 0)  # not resizable

## Flags initialization
running = False   # flag to show if task is activated
to_stop = False   # flag to request for a stop to analysis
complete = False  # flag to indicate task is done/stopped
count = 0         # for counting task

## Analysis task
def analysis():
    '''Simple counting program is run in this task as example

    Replace it with whatever program to run.
    Program MUST break into recurrsive tasks, allows to check 'to_stop' flag.
    Make use of .after() to call for next iteration or quit.

    ** Suggest to check 'to_stop' before the start of very file **
    '''
    global window, complete, console, to_stop, count
    if to_stop or count==0:  # Cancel button is pressed or task complete
        complete = True
        ##
        window.after(100, to_run)  # quit to prepare for next run after 100ms
        ##
    else:
        ## count down every 500ms
        ## iternate for 10 times
        ## at any time, press Cancel button to terminate the task
        console.config(state=tk.NORMAL)
        console.insert(tk.END, ">> {}\n".format(count))
        console.config(state=tk.DISABLED)
        count -= 1
        ##
        img = mpimg.imread('lena.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        ##
        window.after(500, analysis)  # repeat after 500ms
        ##

######################
## Helper functions ##
######################
def show_selection():
    '''Show the selected format and grouping styles in console'''
    global group, format, console, group_msg, format_msg
    g_value = group.get()
    f_value = format.get()
    select = ">> Style: {},  Format: {}\n".format(group_msg[g_value],
                                                  format_msg[f_value])
    console.config(state=tk.NORMAL)
    console.insert(tk.END, select)
    console.config(state=tk.DISABLED)

def start_running():
    '''Update status and start task'''
    global run_btn, console, window, running, count
    run_btn.config(text='Cancel')
    console.config(state=tk.NORMAL)
    console.insert(tk.END, ">> Running...\n")
    console.config(state=tk.DISABLED)
    running = True
    count = 10  # for counting task use
    ##
    console.config(state=tk.NORMAL)
    selected_directory = filedialog.askdirectory()
    console.insert(tk.END, ">> {}\n".format(selected_directory))
    console.config(state=tk.DISABLED)   
    ##
    window.after(500, analysis)  # start task after 500 ms
    ##

def stopped():
    '''Task is stopped. Updata status and prepare for a next run'''
    global console, to_stop, run_btn, complete, running
    console.config(state=tk.NORMAL)
    if to_stop:  # complete and stop, task is immature stopped
        console.insert(tk.END, "Analysis stopped!\n")
    else:        # complete but not stop, task successfully completed
        console.insert(tk.END, ">> Complete!\n")
    console.config(state=tk.DISABLED)
    run_btn.config(text='   Run  ')
    # reset all flags
    running = False
    complete = False
    to_stop = False

def ask_for_stop():
    '''Requesting a stop to task'''
    global to_stop
    to_stop = True

####################################
## Callback functions for buttons ##
####################################
def on_closing():
    '''Pop up window to confirm on closing'''
    global window
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

def to_run():
    '''To response when Run or Cancel button is pressed'''
    global running, complete
    if running:  # under running stage
        if not complete:     # not complete yet, 'Cancel' button is pressed
            ask_for_stop()   # requesting task comfortablw a stop
        else:
            stopped()        # task is stopped        
    else:  # 'Run' button is just pressed
        show_selection()
        start_running()

def to_quit():
    '''To response when Quit is pressed'''
    global running
    if running:
        pass   # cannot quit if under running stage
    else:
        on_closing()

###########################################
## Preparation of UI and display concole ##
###########################################
format_msg = ['Save as csv',
              'Save as image',
              'Show image only',
              'Show & save image']
group_msg =  ['File',
              'Single Directory',
              'Group directory']

## Radiobutton for selecting output format
format = tk.IntVar()
fmt1 = tk.Radiobutton(window, text=format_msg[0], value=0, var=format)
fmt2 = tk.Radiobutton(window, text=format_msg[1], value=1, var=format)
fmt3 = tk.Radiobutton(window, text=format_msg[2], value=2, var=format)
fmt4 = tk.Radiobutton(window, text=format_msg[3], value=3, var=format)
fmt1.grid(column=0, row=0, sticky=tk.W)
fmt2.grid(column=0, row=1, sticky=tk.W)
fmt3.grid(column=0, row=2, sticky=tk.W)
fmt4.grid(column=0, row=3, sticky=tk.W)
fmt1.select()   # default saving to csv

## Radiobutton for selecting grouping style
group = tk.IntVar()
grp1 = tk.Radiobutton(window, text=group_msg[0], value=0, var=group)
grp2 = tk.Radiobutton(window, text=group_msg[1], value=1, var=group)
grp3 = tk.Radiobutton(window, text=group_msg[2], value=2, var=group)
grp1.grid(column=1, row=0, sticky=tk.W)
grp2.grid(column=1, row=1, sticky=tk.W)
grp3.grid(column=1, row=2, sticky=tk.W)
grp3.select()   # default working on group of directories

## Button to trigger Run or Cancel (halt) task
run_btn = tk.Button(window, text='   Run  ', command=to_run)
run_btn.grid(column=0, row=4)

## Button to terminate the application
quit_btn = tk.Button(window, text='Quit', command=to_quit)
quit_btn.grid(column=1, row=4)

## Console for display messages and status
console = tk.Text(window, width=60)  # height is defined according to 'width'
console.grid(column=0, row=5, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

## Create scrollbar object
v_scrollbar = tk.Scrollbar(window)
v_scrollbar.grid(column=2, row=5, sticky=tk.N+tk.S)

## Binding console with the scrollbar
console.config(yscrollcommand=v_scrollbar.set)
v_scrollbar.config(command=console.yview)

## Prepare callback when window is forced to close
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
