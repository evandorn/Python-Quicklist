"""
    Controller.py
    
    Created by: Evan Dorn
    Created on: 7/15/16
"""

import Tkinter as tk
import tkMessageBox
import tkFileDialog
import sys, os
import pickle
import csv

import Model
import View

#
# Controller: Ties View and Model together.
#       -- Performs actions based on View events.
#       -- Sends messages to Model and View and gets responses
#       -- Has Delegates

class MyController(object):
    def __init__(self, parent):
        self.parent = parent
        self.model = Model.MyModel(self)                # initializes the model
        self.view = View.MyView(self)                   #initializes the view
        
        # initialize objects in view
        self.view.setEntryText('')
        
        self.text = tk.Text(parent)

        parent.bind("<Return>", lambda a:self.addButtonPressed())
                    
        if not os.path.exists('savefile.txt'):
            self.model.txtFileCreate()
        
        try:
            savedFile = open(r'savefile.txt','rb')
            buildList = pickle.load(savedFile)
            savedFile.close()
            for key in buildList:
                value = buildList[key]
                self.model.addItem(value, self.view.getWishlistFrame())
                self.model.listAdd(value)
        except EOFError:
            print 'no previous save'

   # event handlers
    def quitButtonPressed(self):
        if tkMessageBox.askyesno('Verify', 'Do you really want to quit?'):
            self.parent.destroy()                                                   # parent.destroy() will kill the mainloop.
            sys.exit()
        else:
            tkMessageBox.showinfo(' ', 'Okay cool. Keep adding things you want to buy. :)')

    # MARK - need to figure out how to pass a frame
    def addButtonPressed(self):
        self.model.createItemObject(self.view.entryText.get(), self.view.getWishlistFrame())
        self.view.clearText()

    def saveButtonPressed(self):
        tkMessageBox.showinfo(' ', 'Save Successful!')                             # inform the user that the save was a success
        print "Saving data..."
        self.model.saveItems()
    
    def exportButtonPressed(self):
        self.saveCSVFile(self.model.wishListDict)

    def saveCSVFile(self, myDictionary):
        print "Saving CSV file"
        with open('mydata.csv', 'wb') as csvFile:                                    # Just use 'w' mode in 3.x
            w = csv.DictWriter(csvFile, myDictionary.keys())
            w.writeheader()
            w.writerow(myDictionary)
                # inform the user that the save was a success
        tkMessageBox.showinfo('Export Successful!', 'Exported CSV file as mydata.csv.\n\nFile exported to %s' % os.getcwd()+'/mydata.csv')

    def listChangedDelegate(self):
        # model internally chages and needs to signal a change
        print(self.model.getList())

