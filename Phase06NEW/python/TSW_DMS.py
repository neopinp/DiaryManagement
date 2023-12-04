##Team Sweet Dreams Diary Management System
##created on: 11/14/23
##last updated: 11/17/2023

##The following code will open the DMS app when run, starting at the login page.

import DMS_Login
from RootWindow import RootWindow


if __name__ == "__main__":
    root = RootWindow()
    DMS_Login.Login(root)
    root.run()
