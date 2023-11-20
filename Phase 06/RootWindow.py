##Team Sweet Dreams Diary Management System
##created on: 11/14/2023
##last edited: 11/19/2023

##The following code defines the class RootWindow
##represents the root window for the Diary Management System tkinter application

import tkinter as tk
import mysql.connector


class RootWindow():
    def __init__(self, title="Diary Managemeny System"):
        self.root = tk.Tk() ##main window
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()-100
        self.root.resizable(width=True, height=True)
        self.root.geometry(f'{self.screen_width}x{self.screen_height}')
        self.root.title(title)
        self.currentUser_id = None
        ##put this in a config.py file if we have the time!!!
        self.connection = mysql.connector.connect(
            host="localhost", user="root", password='root', database="teamsweetdreams_dms")
        self.cursor = self.connection.cursor()
        self.details = {
            'currentPage':None, ##keep track of what page is being shown
            'currentWidgets': self.__getAllWidgets() ##keep track of all widgets currently on the page
            }

    def getCurrentUserRoleDetails(self):
        if self.currentUser_id:
            self.cursor.execute(f"""SELECT * FROM Roles WHERE role_id=(SELECT role_id FROM Users WHERE user_id={self.currentUser_id});""")
            return self.cursor.fetchall()[0]

    def setCurrentUser(self, user):
        self.currentUser_id = user

    def getCurrentUserDetails(self):
        if self.currentUser_id:
            self.cursor.execute(f"""SELECT * FROM Users WHERE user_id={self.currentUser_id};""")
            return self.cursor.fetchall()[0]

    def getUserDiaryData(self):
        if self.currentUser_id:
            self.cursor.execute(f"""SELECT title, O.org_name, O.org_id FROM Users U
                JOIN UserDiaries UD ON UD.user_id = U.user_id
                JOIN Diaries D ON D.diary_id = UD.diary_id
                JOIN Organizations O ON O.org_id = D.diaryOrg_id
                WHERE U.user_id={self.currentUser_id}
                ORDER BY D.diary_id;""")
    
        return self.cursor.fetchall()


    def getUserOrgData(self):
        if self.currentUser_id:
            self.cursor.execute(f"""SELECT OM.org_id, O.org_name FROM Users U
                INNER JOIN organizationmembers OM ON OM.user_id = U.user_id
                INNER JOIN Organizations O ON O.org_id = OM.org_id
                WHERE U.user_id = {self.currentUser_id}
                ORDER BY U.user_id;""")
    
        return self.cursor.fetchall()
        

    def __getAllWidgets(self):
    ##this function references all widgets in a frame
    ##and returns it as a list
        _list = self.root.winfo_children() ##list of the bound master's widgets from bottom to top
        if _list:
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

    
    def run(self):
        self.root.mainloop()



    
    
