##Team Sweet Dreams Diary Management System
##11/15/23
##The following code defines the main screen for the Diary Management System.
##If a user is logged in successfully, this screen will appear.

import tkinter as tk

def banner(root):
    frame1 = tk.Frame(root.root, bg="Red", width=root.screen_width, height=100)
    frame2 = tk.Frame(root.root, bg="Green",width=100, height=root.screen_height)
    
    frame11 = tk.Frame(frame1, height=100, width=300)
    frame112 = tk.Frame(frame11, bg='Pink', height=50, width=200)
    frame113 = tk.Frame(frame11, bg='Orange', height=50, width=200)
    frame114 = tk.Frame(frame11, bg='Blue', height=100, width=100)
    frame115 = tk.Frame(frame11, bg="Yellow", width=root.screen_width-300, height=100)

    frame1.pack(side='top')
    frame2.pack(side='left')
    frame11.pack(side='right')
    frame115.pack(side='left')
    frame114.pack(side='right')
    frame112.pack()
    frame113.pack()

def addOrgs(root):
    ##creates a frame, label, and buttons
    ##for every organizaton the user has access to
    pass
    

def MainPage(root):
    ##takes the RootWindow object as a parameter
    banner(root)
    #addOrgs(root)
    frame3 = tk.Frame(root.root, bg="Purple", width=root.screen_width-100, height=root.screen_height-100)
    frame1 = tk.Frame(frame3, bg="Purple", width=root.screen_width-100, height = 200)
    frame11 = tk.Frame(frame1, bg="Purple", width=2000, height=200)
    frame12 = tk.Frame(frame1, bg="Purple", width=90, height=200)

    titleLabel = tk.Label(frame11, text=f'Organization {1}', font=('Helvetica', 30), bg="White")

    openButton = tk.Button(frame12, text='Open', font=('Helvetica', 15), width=4, bg="Red")
    editButton = tk.Button(frame12, text='Edit', font=('Helvetica', 15), width=4, bg="Pink")

    frame3.pack(side='top')
    frame1.pack(padx=5, pady=5)
    frame11.pack(side='left')
    frame12.pack(side='left')
    titleLabel.pack(padx=10, pady=10)
    editButton.pack(side='right', padx=10, pady=10)
    openButton.pack(side='right', padx=10, pady=10)
