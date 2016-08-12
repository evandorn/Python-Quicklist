#!/usr/bin/python

import Tkinter as tk
import src.Controller

import Tkinter as tkinter

if __name__ == '__main__':
    root = tkinter.Tk()
    frame = tkinter.Frame(root, bg='#0555ff')
    root.title('QuickList')
    app = src.Controller.MyController(root)
    root.mainloop()
