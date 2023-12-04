##Team Sweet Dreams Diary Management System
##created on: 11/14/2023
##last edited: 12/3/2023

##The following code defines the class RootWindow
##represents the root window for the Diary Management System tkinter application

import os
from dotenv import load_dotenv
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector ##import the connector to connect to our mysql database

def getEnvVariables():
    load_dotenv()
    env_vars = {
        "HOST":os.getenv('HOST'),
        "USER":os.getenv('USER'),
        "PASSWORD":os.getenv('PASSWORD'),
        "DATABASE":os.getenv('DATABASE')
        }
    return env_vars

class RootWindow():
    def __init__(self, ENV_VARIABLES=getEnvVariables(), title="Diary Management System"):
        self.root = tk.Tk() ##main window
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()-100
        self.root.resizable(width=True, height=True)
        self.root.geometry(f'{self.screen_width}x{self.screen_height}')
        self.root.title(title)
        self.currentUser_id = None
        ##the following field is used to reference the database connection.
        self.connection = mysql.connector.connect(
            host=ENV_VARIABLES['HOST'],
            user=ENV_VARIABLES['USER'],
            password=ENV_VARIABLES['PASSWORD'],
            database=ENV_VARIABLES['DATABASE'])
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

    def getOrgUserInfo(self, currentOrg):
        userMap=[]
        self.cursor.execute(f"""SELECT DISTINCT diary_id, title, user_id, fullname, org_name FROM diaryinfopgvw WHERE org_name="{currentOrg}";""")
        result=self.cursor.fetchall()
        for i in result:
            if i[3] not in userMap:
                userMap.append({"name":i[3], "user_id":i[2], "title":i[1], "diary_id":i[0], "org":i[4]})
        return userMap

    def getDiaryIdByTitle(self, title):
        try:
            self.cursor.execute(f"""SELECT diary_id FROM Diaries WHERE title="{title}";""")
            return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(f"ERROR: getDiaryIdByTitle:{e}")
    

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
            self.cursor.execute(f"""SELECT OM.org_id, O.org_name, U.user_id, U.fullname FROM Users U
INNER JOIN organizationmembers OM ON OM.user_id = U.user_id
INNER JOIN Organizations O ON O.org_id = OM.org_id
WHERE U.user_id = {self.currentUser_id}
ORDER BY U.user_id;""")
    
        return self.cursor.fetchall()

    def getOrgDataDict(self):
        count=0
        ddd={"Organizations": []}
        orgs= self.getUserOrgData()
        self.cursor.execute(f"""SELECT DISTINCT diary_id, title, subject, owner_id, diaryOrg_id from DiaryInfoPgVW WHERE user_id={self.currentUser_id};""")
        diaries=self.cursor.fetchall()
        for org in orgs:
            ddd['Organizations'].append({"id":org[0], "name":org[1], "diaries":[]})
            for dia in diaries:
                if dia[4] == org[0]:
                    ddd['Organizations'][count]['diaries'].append({"id":dia[0], "name":dia[1], "subject":dia[2], "owner":dia[3], "parentOrg":dia[4],"entries":[]})
            count+=1
        return ddd


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

    def getImage(self, filename, w, h):
        ##returns an image to display, resized.
        img = Image.open(filename) # load image
        resized_image = img.resize((w,h), Image.Resampling.LANCZOS) # resize, remove structural padding
        new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
        return new_image

    
    def run(self):
        self.root.mainloop()



    
    
