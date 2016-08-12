#!/usr/bin/python

import os
import sys
import unittest
sys.path.append('../src')
import Model
import Tkinter as tk

class TestStack(unittest.TestCase):
  root = tk.Tk()
  def setUp(self):
    self.model = Model.MyModel(TestStack.root)
  
  # Testing add functionality
  def testModel(self):
     
     self.model.listAdd("Eggs")
     self.model.listAdd("Milk")
     self.model.listAdd("Bread")
     self.model.listAdd("Butter")
     self.model.listAdd("Coffee")
     self.model.listAdd("Cheese")
     self.model.listAdd("Tea")
     self.model.saveItems()

if __name__ == '__main__':
  unittest.main()
