##Team Sweet Dreams Diary Management System
##Created on: 11/14/2023
##Last Updated: 11/19/2023

##The following code defines the Login page of the Diary Management System
##If a user is not logged in, this screen will appear.


import tkinter as tk
import DMS_MainPage

def Action(root, username, password, master=None):
    ##first verifies the username and password of the user.
    ##if verified, displays a confirmation message and sends the user to the main page.
    ##otherwise, shows a warning and allows the user to retry.
    
    #user_id=verifyCredentials(root, username, password)
    user_id = 1
    if user_id:
        root.cursor.execute(f"""SELECT fullname FROM Users WHERE user_id={user_id};""")
        fullname = root.cursor.fetchone()[0]
        tk.messagebox.showinfo('Access Granted', f'Welcome, {fullname}!')
        root.setCurrentUser(user_id)
        root.removeWidgets(master)
        DMS_MainPage.MainPage(root)
    else:
        tk.messagebox.showwarning('Access Denied', f'The username or password is incorrect.')

def verifyCredentials(root, username, password):
    ##this might not be how this will be done in the final product,
    ##but mysql workbench is acting up Big Time and I cant troubleshoot it

    root.cursor.execute("""SELECT username, password, user_id FROM Users;""")
    data = root.cursor.fetchall()
    for item in data:
        if item[0]==username and item[1]==password:
            return item[2] ##return user_id
    return None

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

    loginButton = tk.Button(innerFrame, text="Log In",
                            command=lambda:Action(root, userEntry.get(), passEntry.get(), master=root.root))

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
    
    
