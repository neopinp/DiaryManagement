##Team Sweet Dreams Diary Management System
##Created on: 11/14/2023
##Last Updated: 11/14/2023

##The following code defines the Login page of the Diary Management System
##If a user is not logged in, this screen will appear.


import tkinter as tk
import DMS_MainPage

def Action(root, master=None):
    if verifyCredentials():
        root.removeWidgets(master)
        DMS_MainPage.MainPage(root)

def verifyCredentials():
    return True

def Login(root):
    ##takes the RootWindow object as a parameter
    root.setCurrentPage("Login")
    outerFrame = tk.Frame(root.root, bg="Green")
    innerFrame = tk.Frame(outerFrame, bg = "Pink", width=root.screen_width/2, height=root.screen_height/2)

    label1 = tk.Label(innerFrame, text='Welcome to Sweet Dreams Diary Management System!')
    label2 = tk.Label(innerFrame, text='Please enter your credentials to log in.')

    entryFrame = tk.Frame(innerFrame)

    usernameLabel = tk.Label(entryFrame, text='Username')
    passwordLabel = tk.Label(entryFrame, text='Password')

    userEntry = tk.Entry(entryFrame)  
    passEntry = tk.Entry(entryFrame)

    loginButton = tk.Button(innerFrame, text="Log In", command=lambda:Action(root, root.root))

    ##add widgets to screen
    outerFrame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    innerFrame.pack(expand=True, padx=root.screen_width/10, pady=root.screen_height/10)
    label1.pack(fill=tk.BOTH)
    label2.pack(fill=tk.BOTH)
    entryFrame.pack()
    usernameLabel.grid(column=1,row=1)
    userEntry.grid(column=2,row=1)
    passwordLabel.grid(column=1,row=2)
    passEntry.grid(column=2,row=2)
    loginButton.pack()
    
    
