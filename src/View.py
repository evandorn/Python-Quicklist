"""
    View.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

import Tkinter as tkinter
import tkMessageBox
import ttk

# View : User interface elements.
#       -- Controller can send messages to it.
#       -- View can call methods from Controller via the view controller when an event happens.
#       -- NEVER communicates with Model.
#       -- Has setters and getters to communicate with controller

class MyView(object):
    
    def __init__(self, viewController):
        
        self.frame = tkinter.Frame()
        self.frame.grid(row = 0, column = 0)
        
        self.viewController = viewController
        self.wishlistFrame = tkinter.Frame()                # master
        self.wishlistFrame.grid()
        
        # self.loadView()
        self.entryText = tkinter.StringVar()
        self.entryText.set('nil')
        addButton = tkinter.Button(self.frame, text = 'Add', command = self.viewController.addButtonPressed).grid(row = 1, column = 0)
        saveButton = tkinter.Button(self.frame, text = 'Save', command = self.viewController.saveButtonPressed).grid(row = 1, column = 1)
        quitButton = tkinter.Button(self.frame, text = 'Quit', command= self.viewController.quitButtonPressed).grid(row = 1,column = 2)
        entry = tkinter.Entry(self.frame, textvariable = self.entryText).grid(row = 0, column = 1, columnspan = 3, sticky = "w")
    
        exportButton = tkinter.Button(self.frame, text = 'Export To CSV', command=self.viewController.exportButtonPressed).grid(row = 1, column = 3)

    # clear entry text after insertion
    def clearText(self):
        self.entryText.set(' ')

    def getWishlistFrame(self):
        return self.wishlistFrame

    # returns a string of the entry text
    def getEntryText(self):
        return self.entryText.get()
    
    # sets the entry text given a string
    def setEntryText(self, text):
        self.entryText.set(text)
