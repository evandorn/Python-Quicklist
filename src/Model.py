"""
    Model.py
    
    Created by: Evan Dorn
    Created on: 7/15/16
"""

import Tkinter as tk
import Controller
import os
import pickle

#Model: Data Structure.
#   -- Controller can send messages to it, and model can respond to message.
#   -- Uses delegates from view controller to send messages to the Controller of internal change
#   -- NEVER communicates with View
#   -- Has setters and getters to communicate with Controller

class MyModel(object):
    def __init__(self, viewController):
        
        self.viewController = viewController
        self.wishList = []
        self.wishListDict = {}
        self.count = 0
    
    #Delegates-- Model would call this on internal change
    def listChanged(self):
        self.viewController.listChangedDelegate()
    
    # setters and getters
    def getList(self):
        return self.wishList
    
    def initListWithList(self, aList):
        self.wishList = aList

# Start wishlist code add
    def createItemObject(self, itemID, frame):
        newItem = itemID
        self.addItem(newItem, frame)
        self.listAdd(newItem)

    def listAdd(self, itemToAdd):
        self.wishList.append(itemToAdd)

    def addItem(self, itemObject, frame):
        self.count += 1
        singleItem = tk.Checkbutton(frame,text=itemObject,
                        command=lambda:
                        self.removeItem(itemObject, frame, singleItem))

        singleItem.grid(row=self.count,column=1)

    def removeItem(self, itemObject, frame, itemName):
        self.count -= 1
        itemName.grid_forget()
        self.wishList.remove(itemObject)

    def saveItems(self):
        keyCounter = 0
        for item in self.wishList:
            self.wishListDict[keyCounter] = item
            keyCounter += 1
        print self.wishListDict
        saveFile = open(r'savefile.txt','wb')
        saveFile.truncate()
        pickle.dump(self.wishListDict, saveFile)
        saveFile.close()

    def txtFileCreate(self):
        saveFile = 'savefile.txt'
        listPersist = open(saveFile, 'a')
        listPersist.close()

# Will go in main.py
if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root, bg='#0555ff')
    root.title('My List')
    app = Controller.MyController(root)
    root.mainloop()
