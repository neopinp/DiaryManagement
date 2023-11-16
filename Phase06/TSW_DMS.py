##Team Sweet Dreams Diary Management System
##11/14/2023

##The following code will open the DMS app when run, starting at the login page.

import tkinter as tk
import DMS_Login
from RootWindow import RootWindow


if __name__ == "__main__":
    root = RootWindow()
    DMS_Login.Login(root)
    root.root.mainloop()
