#!/usr/bin/env python3
# py Desktop\Notepad++\SnakeLessons\Aliens.py
'''import tkinter
window=tkinter.Tk()
label=tkinter.Label(window, text='hello')
label.place(relx=1, rely=0, anchor='center')
tkinter.mainloop()'''

import tkinter as tk
w=100
h=50    
# get screen width and height


# calculate x and y coordinates for the Tk root window

for i in range(0,10):
    root = tk.Tk() # create a Tk root window
    if i==0:
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
    x = (x+100)%ws
    y = (y-100)%ws

    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label=tk.Label(root, text='hello')
    label.place(relx=.5,rely=.5,anchor='center')
    root.mainloop() # starts the mainloop