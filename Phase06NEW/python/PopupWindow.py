##Team Sweet Dreams Diary Management System
##11/16/23
##The following defines a class that creates a popup window using tkinter

import tkinter as tk
from RootWindow import RootWindow



class PopupWindow(RootWindow):
    def __init__(self, title):
        super().__init__(title=title)
        self.root.geometry("500x500")
        
