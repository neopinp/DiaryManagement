##Team Sweet Dreams Diary Management System
##11/14/2023
##The following code defines the class RootWindow
##represents the root window for the Diary Management System tkinter application

import tkinter as tk


class RootWindow():
    def __init__(self):
        self.root = tk.Tk() ##main window
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()-100
        self.root.resizable(width=True, height=True)
        self.root.geometry(f'{self.screen_width}x{self.screen_height}')
        self.root.title("Diary Managemeny System")
        self.details = {
            'currentPage':None, ##keep track of what page is being shown
            'currentWidgets': self.__getAllWidgets() ##keep track of all widgets currently on the page
            }

        
    def __getAllWidgets(self):
    ##this function references all widgets in a frame
    ##and returns it as a list
    ##it is made to be recursive so another function
    ##can iterate through and destory all widgets but not the entire frame
        _list = self.root.winfo_children() ##list of the bound master's widgets from bottom to top
        for widget in _list:
            if widget.winfo_children():
                _list.extend(self.root.winfo_children()) ## if the widget has embedded widgets, acknowledge them too.
        return _list
    
    def getCurrentPage(self):
        ##returns the page that is currently set to be focused
        return self.details['currentPage']

    def setCurrentPage(self, page):
        ##sets the page that is currently set to be focused
        self.details['currentPage'] = page

    def removeWidgets(self, master=None):
        ##removes all widgets contained within a specified frame
        ##without removing the frame itself
        ##if no frame is specified, the main window is cleared
        ##and the GUI will close.
        if master != None:
            delete = master.winfo_children()
            for i in delete:
                i.destroy()
        else:
            self.root.destroy()



    
    
