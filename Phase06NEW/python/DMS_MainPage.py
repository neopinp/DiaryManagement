##Team Sweet Dreams Diary Management System
##created on: 11/15/23
##last updated: 1/2/2023

##The following code defines the main screen for the Diary Management System.
##If a user is logged in successfully, this screen will appear.

import tkinter as tk
from RootWindow import RootWindow
import calendar
import datetime
from tkinter import messagebox, PhotoImage
from tkinter.ttk import Combobox, Button, Style
from PIL import Image, ImageTk
import DMS_Login

def banner(root):
    ##creates the banner at the top of the screen and the spacers on the side
    ##returns the space left on the screen

    aW, aH = root.screen_width, root.screen_height ##available width and height of the screen
    topW, topH = root.screen_width, 75 ##width and height of top banner
    spacerW, spacerH = 20, aW-topH ##width and height of side spacers

    aW-=spacerW*2
    aH-=topH
    
    ##rewrite the width and height to variables to reduce hardcoded numbers
    topBanner = tk.Frame(root.root, bg="Pink", width=topW, height=topH)
    leftSpacer = tk.Frame(root.root, bg="Purple",width=spacerW, height=spacerH)
    rightSpacer = tk.Frame(root.root, bg="Purple",width=spacerW, height=spacerH)
    mainFrame = tk.Frame(root.root, bg="Purple", width=aW, height=aH)
    
    frame11 = tk.Frame(topBanner, height=100, width=300)
    frame112 = tk.Frame(frame11, bg='Pink', height=50, width=200)
    frame113 = tk.Frame(frame11, bg='Pink', height=50, width=200)
    frame114 = tk.Frame(frame11, bg='Pink', height=topH, width=topH)

    nameLabel = tk.Label(frame112, text=f'{root.getCurrentUserDetails()[3]}', font=('Helvetica', 14), bg='Pink')
    roleLabel = tk.Label(frame113, text=f'{root.getCurrentUserRoleDetails()[1]}', font=('Helvetica', 11), bg='Pink')

    ##determine which button to present
    if root.getCurrentPage()=="Main":
        img=root.getImage("gear.png", topH-5, topH-5)
        settingsButton = tk.Button(frame114, image=img, command=lambda:openSettings(root))
        settingsButton.image=img
        settingsButton.pack(padx=15, pady=10)
    elif root.getCurrentPage()=="Settings":
        img=root.getImage("redX.png", topH-5, topH-5)
        backButton = tk.Button(frame114, image=img, command=lambda:MainPage(root))
        backButton.image=img
        backButton.pack(padx=15, pady=10)
    

    topLabel = tk.Label(topBanner, text="Diary Management System", font=("Helvetica", 35), bg="Pink", fg="Black")

    topBanner.pack(side='top', fill="both")
    leftSpacer.pack(side='left', fill="both")
    rightSpacer.pack(side='right', fill="both")
    frame11.pack(side='right', fill="both")
    topLabel.pack(side='left', padx=20, pady=5)
    frame114.pack(side='right', fill="both")
    frame112.pack(fill="both")
    frame113.pack(fill="both")
    nameLabel.pack(padx=10, pady=12, fill='both')
    roleLabel.pack(padx=10, fill='both', pady=10)

    
    return mainFrame, aW, aH

def openSettings(root):
    ##opens a new window that allows a user
    ##to edit their account information
            
    root.removeWidgets(root.root)
    root.setCurrentPage("Settings")
    availableSpace, aW, aH = banner(root) ## display the banner and borders of the main page
    
    ##define the contents
    frame1 = tk.Frame(availableSpace, bg='White')
    frame2 = tk.Frame(availableSpace, bg='Purple')
    frame3 = tk.Frame(availableSpace, bg='Purple')

    availableSpace.pack(fill='both')
    frame1.pack(side='left', fill='both')
    frame2.pack(fill='both')
    frame3.pack(side='right', fill='both')
    
    nameLabel=tk.Label(frame1, text="Name:")
    nameInfo=tk.Label(frame1, text=f'{root.getCurrentUserDetails()[3]}') #Displays Name
    
    usernameLabel=tk.Label(frame1, text="Username:")
    usernameInfo=tk.Label(frame1, text=f'{root.getCurrentUserDetails()[4]}') # Displays Username

    passLabel=tk.Label(frame1, text="Password:")
    passInfo=tk.Label(frame1, text="*********")

    orgsLabel=tk.Label(frame1, text="Your Organizations:")

    nameEntry=tk.Entry(frame1)

    editButton=tk.Button(frame1, text='Edit Information', command=lambda: editUserSettings(mainFrame))

    logoutButton=tk.Button(frame3, text='Log Out', font=('Helvetica', 14), command=lambda:logout(root))

    aboutUsButton=tk.Button(frame3, text='About Us', font=('Helvetica', 14), command=lambda:showAboutUs(root, frame1))

    ##Add the contents to the window
    
    #editButton.grid(column=3, row=1)
    nameLabel.grid(column=1, row=1)

    usernameLabel.grid(column=1, row=2)
    #passLabel.grid(column=1, row=5)
    orgsLabel.grid(column=1, row=3)
    
    nameInfo.grid(column=2, row=1)
    usernameInfo.grid(column=2, row=2)

    logoutButton.pack(pady=10)
    aboutUsButton.pack(pady=10)

def editUserSettings(mainFrame):
    pass

def logout(root):
    answer=tk.messagebox.askyesno('Log Out', f'Are you sure you want to log out?')
    if answer:
        root.currenUser_id=None
        root.removeWidgets(root.root)
        DMS_Login.Login(root)
    

def showAboutUs(root, frame):
    root.removeWidgets(root.root)
    
    lab=tk.Label(root.root, font=('Helvetica', 16), bg="Purple", fg='Light Blue',
                 text="""Team Sweet Dreams
    ----------------------------------------------------
    We are a group of students at Marist College creating this project
    for Dr. Reza Sadeghi's Fall 2023 Database Management class.

    Meet the Team:
    Evan Spillane..........Evan.Spillane1@marist.edu
    Abel Scholl............Anna.Scholl1@marist.edu
    Connor Fleischman......Connor.Fleischman1@marist.edu
    Lilli Cartiera.........Lilliana.Cartiera1@marist.edu 
    Neo Pi.................Neo.Pi1@marist.edu

    Special Thanks to Dr. Reza Sadeghi""")
    
    img=root.getImage("Marist_College_Seal.png", int(640/2), int(640/2))
    sealLabel = tk.Label(root.root, image=img, bg='White')
    sealLabel.image=img
    backButton=tk.Button(root.root, text='<- Back', command=lambda:openSettings(root))
    backButton.pack()
    lab.pack(padx=10, pady=10)
    sealLabel.pack(padx=10, pady=10)

def Save(root, master=None):
    ##this function will update the database with the new information.

    ##close the popup window (placeholder action for now)
    root.removeWidgets(master)


def EditOrg(org_name=None):
    ##opens a new window that allows a user
    ##to edit an organization's information
    ##if org_name=None, it prompts to create a new organization.

    ##create the popup
    editWindow = RootWindow(title="Edit Organization")
    editWindow.root.geometry("500x500")
    
    ##define the contents
    frame1 = tk.Frame(editWindow.root, bg="Blue")
    nameLabel=tk.Label(frame1, text="Organization name:")
    nameEntry=tk.Entry(frame1)
    
    saveButton=tk.Button(frame1, text='Save Changes', command=lambda:Save(editWindow))

    if org_name:
        if nameEntry.get():
            nameEntry.delete(0, tk.END)
        nameEntry.insert(0, org_name)

    ##Add the contents to the window
    frame1.pack()
    nameLabel.grid(column=1, row=1)
    nameEntry.grid(column=2, row=1)
    saveButton.grid(column=3, row=2)
    
    editWindow.run() ##open the window



def populateOptionsFrame(root, framesList):
    ##populates the options frame with a way to choose an organization and show its associated diaries

    opf = framesList[0]
    ##Add Frames
    headingFrame = tk.Frame(opf, bg="Purple")
    headingFrame.pack(fill='both')
    comboFrame=tk.Frame(opf, bg="Purple")
    comboFrame.pack(fill='both')
    headingFrame2 = tk.Frame(opf, bg="Purple")
    headingFrame2.pack(fill='both')
    diaryListFrame = tk.Frame(opf, bg="White")
    diaryListFrame.pack(fill='both')

    if diaryListFrame not in framesList:
        framesList.append(diaryListFrame)

    ##Add heading labels
    heading=tk.Label(headingFrame, text="Organization", font=('Helvetica', 20), bg="Purple", fg="Light Blue")
    #heading.pack(padx=10, pady=10)
    heading2=tk.Label(headingFrame2, text="Diaries", font=('Helvetica', 18), bg="White", fg="Purple")
    heading2.pack(padx=10, pady=10, fill=tk.X)

    userOrgData = root.getUserOrgData()

    orgs=[]
    for item in userOrgData:
        orgs.append(item[1]) ##append organization name

    orgsCombo = Combobox(comboFrame, font=('Helvetica', 18), state="readonly")
    orgsCombo['values']=orgs
    orgsCombo.current(0)
    orgsCombo.pack(padx=10, pady=10)

        
    ##get all diaries a user has access to and the organization it is associated with(title and id)   
    userDiaryData=root.getUserDiaryData()

    showDiariesButton = tk.Button(comboFrame, text='Show Diaries', font=('Helvetica', 12),
                                  bg="Pink", command=lambda:showOrgDiaries(root, framesList, orgsCombo.get()))
    editButton = tk.Button(comboFrame, text='Edit', font=('Helvetica', 12),
                                   bg="Pink", command=lambda:EditOrg(orgsCombo.get()))
    #editButton.configure(command=lambda editButton=editButton:EditOrg())
    
    showDiariesButton.pack(padx=5, pady=5)
    #editButton.pack(padx=5)

    showOrgDiaries(root, framesList, orgsCombo.get())


def EditOrg(id=None):
    ##opens a new window that allows a user
    ##to edit an organization's information
    ##if id=None, it prompts to create a new organization.

    ##create the popup
    editWindow = RootWindow(title="Edit Organization")
    editWindow.root.geometry("500x500")
    
    ##define the contents
    frame1 = tk.Frame(editWindow.root, bg="Blue")
    nameLabel=tk.Label(frame1, text="Organization name:")
    nameEntry=tk.Entry(frame1)
    
    ##only passing the window to Save,
    ##so master of .removeWidgets(master) is None, which will close the whole window.
    saveButton=tk.Button(frame1, text='Save Changes', command=lambda:Save(editWindow))

    ##Add the contents to the window
    frame1.pack()
    nameLabel.grid(column=1, row=1)
    nameEntry.grid(column=2, row=1)
    saveButton.grid(column=3, row=2)
    
    editWindow.run() ##open the window



def showOrgDiaries(root, framesList, currentOrg, returnTitle=None):
    dlf = framesList[5]
    root.removeWidgets(dlf)
    
    ##Show a button for each diary associated with an organization
    data=root.getUserDiaryData()
    for item in data:
        if item[1]==currentOrg: ##if the organization name is the same as the one in the combobox
            diaryButton = tk.Button(dlf, text=item[0], font=('Helvetica', 14),
                    bg="Pink", width=20)
            diaryButton.config(command=lambda diaryTitle=item[0], diaryButton = diaryButton: createDiary(root, framesList, currentOrg, diaryTitle=diaryTitle))
            diaryButton.pack(padx=5, pady=10)
            
    ##if permission allows:
    addDiaryButton = tk.Button(dlf, text="Add Diary +", font=('Helvetica', 14),
        bg="Pink", width=20, command=lambda:editDiary(root, currentOrg, framesList)) ##pass with no third parameter prompts to add new
    addDiaryButton.pack(padx=5, pady=10)

    createDiary(root, framesList, currentOrg, diaryTitle=returnTitle) 


def saveDiary(root, window, frame, title, subject, currentOrg, membersTextBox, framesList, userMap, currentMembers, action, oldTitle=None):
    ##creates a new diary or deletes or edits an existing diary.

    ##need to add other verification! verify entry lengths, cannot delete yourself from diary
    ##should change implementation so that diary_id can be retreived easily from root.
    
    if not title:
        errorLabel = tk.Label(frame, text="Please enter a title.", bg="Pink", fg="Red")
        errorLabel.pack(side='bottom', padx=10, pady=15)
        return
    now = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')

    if action == 'delete': ##delete the existing diary
        answer=tk.messagebox.askyesno('Delete Diary', f"""Are you sure you want to delete {title}?""")
        if answer:
            try:
                root.cursor.execute(f"""SELECT diary_id FROM Diaries WHERE title="{oldTitle}";""")
                diary_id = root.cursor.fetchall()[0][0]
                root.cursor.execute(f"""DELETE FROM Diaries WHERE diary_id="{int(diary_id)}";""")
                root.connection.commit()
            except Exception as e:
                print("save delete diary:\n", e)     


    elif action != 'delete':
        if action == 'new': ##create a new diary
            try:
                root.cursor.execute(f"""SELECT org_id FROM Organizations WHERE org_name = "{currentOrg}";""")
                org_id = root.cursor.fetchall()[0][0]

                root.cursor.execute(f"""INSERT INTO Diaries (title, date_created, last_updated, owner_id, subject, diaryOrg_id)
                VALUES("{title}", "{now}", "{now}", {root.currentUser_id}, "{subject}", {org_id});""")
                root.connection.commit()
                root.cursor.execute(f"""INSERT INTO UserDiaries (user_id, diary_id) VALUES ({root.currentUser_id}, (SELECT MAX(LAST_INSERT_ID()) FROM Diaries));""")
                root.connection.commit()
            except Exception as e:
                print("ERROR: save new Diary: ", e)

        elif action == 'edit': ##edit the existing diary
            try:
                root.cursor.execute(f"""SELECT diary_id FROM Diaries WHERE title="{oldTitle}";""")
                diary_id = root.cursor.fetchall()[0][0]
                root.cursor.execute(f"""UPDATE Diaries
    SET title="{title}", last_updated="{now}", subject="{subject}" WHERE diary_id="{int(diary_id)}";""")
                root.connection.commit()
            except Exception as e:
                print("ERROR: Save edit diary: ", e)


        
        membersList = membersTextBox.get(0.0, "end - 1 lines").rstrip().split("\n") ##get the contents of the textBox AFTER changes have been made
        if membersList:
            for i in currentMembers:## currentMembers: ORIGINAL value of the textBox BEFORE changes were made.
                if i not in membersList: ##if an original member is no longer in the text box, delete it.
                    print(f"delete user {i}")
                    for u in userMap:
                        if i==u['name'] and u['title']==title:
                            try:
                                root.cursor.execute(f"""DELETE FROM UserDiaries WHERE user_id={u['user_id']} and diary_id={u['diary_id']};""")
                                root.connection.commit()
                                print("deleted!")
                            except Exception as e:
                                print(f"ERROR: Delete user: {e}")

            for member in membersList:
                if member not in currentMembers:
                    print(f"add user {member}")
                    for u in userMap:
                        if member==u['name']:
                            try:
                                if action=='new':
                                    root.cursor.execute(f"""INSERT INTO UserDiaries (user_id, diary_id) VALUES ({u['user_id']}, (SELECT MAX(LAST_INSERT_ID()) FROM Diaries));""")
                                    root.connection.commit()
                                    print("added! (new)")
                                elif action == 'edit':
                                    root.cursor.execute(f"""INSERT INTO UserDiaries (user_id, diary_id) VALUES ({u['user_id']}, {root.getDiaryIdByTitle(title)});""")
                                    root.connection.commit()
                                    print("added! (edit)")
                                else:
                                    print("Action: ", action)
                            except Exception as e:
                                if "1062 (23000): Duplicate entry" in str(e):
                                    continue
                                else: print(f"ERROR: Add user: {e}")
   

    window.removeWidgets(master=None) ##close the window
    showOrgDiaries(root, framesList, currentOrg, title)



def manageDiaryMembers(root, window, frameList, user, userMap, action=None):
    ##adds or removes a selected user within the organization
    ##to the list of users to be added to the diary.
    
    lis=frameList[0].winfo_children()
    for widget in lis:
        if isinstance(widget, tk.Text):
            widget['state']='normal'
            found=False
            for i in userMap:
                if user==i['name']:
                    found=True
                    if action=="add":
                        if user not in widget.get(1.0, "end-1c"):
                            widget.insert(tk.END, f"{user}\n")
                            root.removeWidgets(frameList[1])
                    elif action=="remove":
                        if user in widget.get(1.0, "end-1c"):
                            textList=widget.get(1.0, "end - 1 lines").rstrip().split("\n")
                            if user in textList:
                                textList.remove(user)
                                widget.delete(1.0, tk.END)
                            for member in textList:
                                manageDiaryMembers(root, window, frameList, member, userMap, action="add")
            widget['state']='disabled'
            if not found:
                root.removeWidgets(frameList[1])
                errorLabel = tk.Label(frameList[1], text=f"user {user} does not exist.", bg="Pink", fg="Red")
                errorLabel.pack(side='bottom', padx=10, pady=15)
                return
                


def editDiary(root, currentOrg, framesList, diary=None):
    ##opens a new window that allows a user
    ##to edit a diary's information
    ##if diary=None, it prompts to create a new diary.

    ##create the popup
    t='Edit' if diary else 'Add'
    window = RootWindow(title=f'{t} Diary')
    window.root.geometry(f"{int(root.screen_width*0.8)}x{int(root.screen_height*0.8)}")
    window.root['bg']='Pink'
    
    ##define the contents
    frame1 = tk.Frame(window.root, bg="Pink")
    frame2 = tk.Frame(window.root, bg="Pink")
    frame3 = tk.Frame(window.root, bg="Pink")
    frame4 = tk.Frame(window.root, bg="Pink")
    errorFrame = tk.Frame(window.root, bg="Pink")
    titleLabel=tk.Label(frame1, text="Diary title:", font=('Helvetica',14), bg="Pink")
    titleEntry=tk.Entry(frame1, font=('Helvetica',12))
    subjectLabel=tk.Label(frame2, text="Subject:", font=('Helvetica',14), bg="Pink")
    subjectEntry=tk.Entry(frame2, width=100, font=('Helvetica',12))

    membersLabel=tk.Label(frame4, text="Add or Remove Members:", font=('Helvetica',14), bg="Pink")
    membersCombo=Combobox(frame4, font=('Helvetica', 12))
    membersTextBox=tk.Text(frame4, font=('Helvetica', 12), width=30, height=10)

    userMap=root.getOrgUserInfo(currentOrg) ##get all members in this organization
    availableMembers=[]
    currentMembers=[]
    currentUserName=''
    
    ##populate availableMembers, a list of only names from userMap.
    try:
        for i in userMap:
            if i['user_id']==root.currentUser_id:
                currentUserName=i['name']
            if i['name'] not in availableMembers:
                availableMembers.append(i['name'])
        membersCombo['values']=availableMembers
        membersCombo.set("Choose a Member")
        print(userMap,"\n")
    except Exception as e:
        print(f'edit Diary get org members\n{e}')
        
    addMemberButton=tk.Button(frame4, text="Add Member +", font=('Helvetica',14),
                              command=lambda:manageDiaryMembers(root, window, [frame4, errorFrame], membersCombo.get(), userMap, action="add"))
    removeMemberButton=tk.Button(frame4, text="Remove Member -", font=('Helvetica',14),
                              command=lambda:manageDiaryMembers(root, window, [frame4, errorFrame], membersCombo.get(), userMap, action="remove"))
    
    
    cancelButton=tk.Button(frame3, text='Cancel', command=lambda:window.root.destroy(), font=('Helvetica',12), bg="Light Blue")
    deleteButton=tk.Button(frame3, text='Delete This Diary', font=('Helvetica',12), bg="Red", fg="White")
    
    ##only passing the window to Save,
    ##so master of .removeWidgets(master) is None, which will close the whole window.
    saveButton=tk.Button(frame3, text='Save',  font=('Helvetica',12), bg="Green", fg="White")

    ##Add the contents to the window
    frame1.pack(fill='both')
    frame2.pack(fill='both')
    frame4.pack(fill='both')
    frame3.pack(fill='both', side='bottom')
    errorFrame.pack(fill='both', side='bottom')
    titleLabel.pack(side='left', padx=10, pady=10)
    titleEntry.pack(side='left', padx=10, pady=10)
    subjectLabel.pack(side='left', padx=5, pady=10)
    subjectEntry.pack(side='left', padx=5, pady=10)
    membersLabel.pack(side='left', padx=5, pady=10)
    membersCombo.pack(side='left', padx=5, pady=10)
    addMemberButton.pack(side='left', padx=5, pady=10)
    membersTextBox.pack(side='left', expand=True, padx=5, pady=10)
    removeMemberButton.pack(side='right', padx=10, pady=10)
    saveButton.pack(side='right', padx=10, pady=10)
    cancelButton.pack(side='right', padx=10, pady=10)
    
    if diary:
        try:
            ##select all members with access to this diary
            root.cursor.execute(f"""SELECT DISTINCT diary_id, title, user_id, fullname, org_name FROM diaryinfopgvw WHERE org_name="{currentOrg}" AND title="{diary}";""")
            result=root.cursor.fetchall()
            for u in result:
                currentMembers.append(u[3])
                membersTextBox.insert(tk.END, f"{u[3]}\n")
            membersTextBox['state']='disabled'
            deleteButton.pack(side='right', padx=20, pady=10)
            root.cursor.execute(f"""SELECT diary_id, subject FROM diaryinfopgvw WHERE title="{diary}" AND org_name="{currentOrg}";""")
            data = root.cursor.fetchall()[0]
            diary_id, subject = data[0], data[1]
            
            if titleEntry.get():
                titleEntry.delete(0, tk.END)
            titleEntry.insert(0, diary)
            if subjectEntry.get():
                subjectEntry.delete(0, tk.END)
            subjectEntry.insert(0, subject)

            saveButton.config(command=lambda cO=currentOrg,
                saveButton=saveButton:saveDiary(root, window, errorFrame, titleEntry.get(),
                                            subjectEntry.get(), cO, membersTextBox, framesList, userMap, currentMembers, action='edit', oldTitle=diary))

            deleteButton.config(command=lambda cO=currentOrg,
                    deleteButton=deleteButton:saveDiary(root, window, errorFrame, titleEntry.get(),
                                            subjectEntry.get(), cO, membersTextBox, framesList, userMap, currentMembers, action='delete', oldTitle=diary))
    
        except Exception as e:
            print("first Edit: ", e)
            
    else:
        currentMembers.append(currentUserName)
        membersTextBox.insert(tk.END, f"{currentUserName}\n")
        membersTextBox['state']='disabled'
        saveButton.config(command=lambda cO=currentOrg,
            saveButton=saveButton:saveDiary(root, window, errorFrame, titleEntry.get(), subjectEntry.get(),
                                            cO, membersTextBox, framesList, userMap, currentMembers, action='new'))

    window.run() ##open the window


def createDiary(root, framesList, currentOrg, diaryTitle=None):
    ##this function populates the middle calendar frame.
    ##with the diary name and a functional calendar.

    cdf = framesList[1]

    ##Retrieve a specified user's diaries
    root.cursor.execute(f"""SELECT title, org_name FROM diaryinfopgvw WHERE user_id = "{root.currentUser_id}";""")
    diaries = root.cursor.fetchall()
        
    ##clear the screen
    root.removeWidgets(cdf)

    ##create title headers
    if diaryTitle == None: ##if no title is given, choose the first in the list to display.
        for item in diaries:
            if item[1]==currentOrg:
                diaryTitle = item[0]
                break

    diaryLabel=tk.Label(cdf, text=diaryTitle, font=("Helvetica", 28), bg="Purple", fg="Light Blue")
    diaryLabel.pack(side='top', pady=20)

    monthYearFrame = tk.Frame(cdf, bg="Purple")
    monthYearFrame.pack(side='top')

    ##create the calendar
    calendarFrame=tk.Frame(cdf, bg="White") ##frame for the actual calendar
    calendarFrame.pack(side='top', padx=20)
    
    ##initialize important veriables
    today=datetime.date.today()
    months=[]
    years=[]

    for i in calendar.month_name[1:]: ## get a list of all months
        months.append(i)
    for i in range(2023, today.year+10): ##get a list of ten years from this year, starting from 2023
        years.append(i)


    ##create comboboxes
    monthsCombo = Combobox(monthYearFrame, width=10, state="readonly", font=("Helvetica", 12))
    monthsCombo['values']=months
    monthsCombo.current((datetime.date.today().month)-1) ##index starts at 0
    monthsCombo.pack(side='left', padx=5)
    
    yearsCombo = Combobox(monthYearFrame,width=8, state="readonly", font=("Helvetica", 12))
    yearsCombo['values']=years
    yearsCombo.current((datetime.date.today().year)-2023)##first index is this year (2023)
    yearsCombo.pack(side='left', pady=10)

    showCalendarButton = tk.Button(monthYearFrame, text="Show Calendar", bg="White",
                                   command=lambda:showCalendar(root, calendarFrame, framesList,
                                    months.index(monthsCombo.get())+1,int(yearsCombo.get()), today, diaryTitle))
    showCalendarButton.pack(side='left', padx=5)

    editDiaryButton = tk.Button(monthYearFrame, text="Edit Diary", bg="White",
                                command=lambda:editDiary(root, currentOrg, framesList, diary=diaryTitle))
    editDiaryButton.pack(side='left', padx=5)
    
    addEntryButton = tk.Button(monthYearFrame, text="Add Entry", bg="White",
                                command=lambda:addEntry(root, currentOrg, framesList, diaryTitle))
    addEntryButton.pack(side='left', padx=5)

    showCalendar(root, calendarFrame, framesList, months.index(monthsCombo.get())+1, int(yearsCombo.get()), today, diaryTitle)

    iterateEntries(root, framesList[4], diaryTitle)

    populateSearchFrame(root, framesList, diaryTitle, currentOrg)


def showCalendar(root, calendarFrame, framesList, month, year, today, diaryTitle):
    cdf=framesList[1]
    ##clear calendar
    root.removeWidgets(calendarFrame)

    command=iterateEntries(root, framesList[4], diaryTitle)
    weekdays=[]
    ##have to pull out sunday and do it separately because it absolutely refuses all attempts to be first in the iteration
    weekdays.append(calendar.day_name[-1:][0])
    dayLabel = tk.Label(calendarFrame, text=weekdays[0], bg="White")
    dayLabel.grid(column=1, row=1)
    ##iterate days
    for day in calendar.day_name[:-1]: ##get a list of all weekdays
            weekdays.append(day)
            dayLabel = tk.Label(calendarFrame, text=f'{day}', bg="White")
            dayLabel.grid(column=weekdays.index(day)+1, row=1)
    
    ##get the first weekday of the month and the number of days in the month, respectively
    firstWeekday, daysInMonth = calendar.monthrange(year, month)
    dayNum=1
    blankCount=0

    for week in range(1,7): ##up to 6 weeks (rows) in one month
        for day in range(1,8): ##seven days(columns) in one week
            if dayNum <= daysInMonth:
                if blankCount < firstWeekday+1: ##add a blank label for every day before the month's first day
                    blankButton = tk.Button(calendarFrame, width=9, height=5, bg="White",)
                    blankButton.grid(column=day, row=week+1, sticky='nsew')
                    blankCount+=1
                else:
                    if dayNum==today.day and today.month==month and today.year==year: ##if it is today's date
                        dayButton = tk.Button(calendarFrame,text=dayNum, width=9, height=5, bg="Pink") ##indicate in pink
                    else:
                        dayButton = tk.Button(calendarFrame, text=dayNum, width=9, height=5, bg="White",) ##otherwise, no indication
                    dayButton.grid(column=day, row=week+1, sticky='nsew')
                    dayNum+=1

                    
def addEntry(root, currentOrg, framesList, diaryTitle):
    ##opens a new window that allows a user
    ##to add a new Entry to a diary
    ##if diary=None, it prompts to create a new diary.

    ##create the popup
    window = RootWindow(title="Add Entry")
    window.root.geometry(f"{int(root.screen_width*0.8)}x{int(root.screen_height*0.8)}")
    window.root['bg']='Pink'
    
    ##define the contents
    frame1 = tk.Frame(window.root, bg="Pink")
    frame2 = tk.Frame(window.root, bg="Pink")
    frame3 = tk.Frame(window.root, bg="Pink")
    locationFrame=tk.Frame(window.root, bg="Pink")
    locFrame1=tk.Frame(locationFrame, bg="Pink")
    locFrame2=tk.Frame(locationFrame, bg="Pink")
    
    frame4 = tk.Frame(window.root, bg="Pink")
    frame5 = tk.Frame(window.root, bg="Pink") ##used to show input issues
    
    titleLabel=tk.Label(frame1, text="Entry title:", font=('Helvetica',14), bg="Pink")
    titleEntry=tk.Entry(frame1, font=('Helvetica',12))
    
    descriptionLabel=tk.Label(frame2, text="Description:", font=('Helvetica',14), bg="Pink")
    descriptionEntry=tk.Entry(frame2, width=100, font=('Helvetica',12))

    startTimeLabel=tk.Label(frame3, text="Start Time:", font=('Helvetica',14), bg="Pink")
    startTimeEntry=tk.Entry(frame3, font=('Helvetica',12))
    
    
    endTimeLabel=tk.Label(frame3, text="End Time:", font=('Helvetica',14), bg="Pink")
    endTimeEntry=tk.Entry(frame3, font=('Helvetica',12))

    priorityLabel=tk.Label(frame3, text="Priority:", font=('Helvetica',14), bg="Pink")
    priorityCombo=Combobox(frame3, font=('Helvetica',12), state='readonly')
    priorityCombo['values']= ("None", "Low", "Medium", "High")
    priorityCombo.current(0)

    entryTypeLabel=tk.Label(frame3, text="Type:", font=('Helvetica',14), bg="Pink")
    entryTypeCombo=Combobox(frame3, font=('Helvetica',12), state='readonly')
    entryTypeCombo['values']= ('Note', 'Meeting')#get list of all entry types
    entryTypeCombo.current(0)
    

    locationLabel=tk.Label(locFrame1, text="Location:", font=('Helvetica',14), bg="Pink")
    add1Label=tk.Label(locFrame1, text="Address Line 1:", font=('Helvetica',14), bg="Pink")
    add1Entry=tk.Entry(locFrame1, font=('Helvetica',12), width=100)
    add2Label=tk.Label(locFrame1, text="Address Line 2:", font=('Helvetica',14), bg="Pink")
    add2Entry=tk.Entry(locFrame1, font=('Helvetica',12), width=100)
    cityLabel=tk.Label(locFrame2, text="City:", font=('Helvetica',14), bg="Pink")
    cityEntry=tk.Entry(locFrame2, font=('Helvetica',12), width=20)
    stateLabel=tk.Label(locFrame2, text="State:", font=('Helvetica',14), bg="Pink")
    stateCombo=Combobox(locFrame2, font=('Helvetica',12))
    ##stateCombo['values']= ()
    zipLabel=tk.Label(locFrame2, text="Zipcode:", font=('Helvetica',14), bg="Pink")
    zipEntry=tk.Entry(locFrame2, font=('Helvetica',12), width=5)

    
    cancelButton=tk.Button(frame4, text='Cancel', command=lambda:window.root.destroy(), font=('Helvetica',12), bg="Light Blue")

    locInfo=[add1Entry, add2Entry, cityEntry, stateCombo, zipEntry]
    info=[diaryTitle, titleEntry, startTimeEntry, endTimeEntry, descriptionEntry, priorityCombo, entryTypeCombo, locInfo]
    
    saveButton=tk.Button(frame4, text='Save',  font=('Helvetica',12), bg="Green", fg="White")
    saveButton.config(command=lambda cO=currentOrg,
                    saveButton=saveButton:saveEntry(root, window, frame5, info, framesList))

    ##Add the contents to the window
    frame1.pack(fill='both')
    frame2.pack(fill='both')
    frame3.pack(fill='both')
    locationFrame.pack(fill='both')
    locFrame1.pack(fill='both')
    locFrame2.pack(fill='both')
    frame4.pack(side='bottom', fill='both')
    frame5.pack(side='bottom', fill='both', pady=10)
    titleLabel.grid(column=1, row=1, padx=10, pady=10)
    titleEntry.grid(column=2, row=1, padx=10, pady=10)
    descriptionLabel.grid(column=1, row=2, padx=10, pady=10)
    descriptionEntry.grid(column=2, row=2, padx=10, pady=10)
    startTimeLabel.grid(column=1, row=3, padx=10, pady=10)
    startTimeEntry.grid(column=2, row=3, padx=10, pady=10)
    endTimeLabel.grid(column=3, row=3, padx=10, pady=10)
    endTimeEntry.grid(column=4, row=3, padx=10, pady=10)
    priorityLabel.grid(column=1, row=5, padx=10, pady=10)
    priorityCombo.grid(column=2, row=5, padx=10, pady=10)
    entryTypeLabel.grid(column=3, row=5, padx=10, pady=10)
    entryTypeCombo.grid(column=4, row=5, padx=10, pady=10)
    
    locationLabel.grid(column=1, row=1, padx=10, pady=10)
    add1Label.grid(column=1, row=2, padx=10, pady=10)
    add1Entry.grid(column=2, row=2, padx=10, pady=10)
    add2Label.grid(column=1, row=3, padx=10, pady=10)
    add2Entry.grid(column=2, row=3, padx=10, pady=10)
    cityLabel.grid(column=1, row=1, padx=10, pady=10)
    cityEntry.grid(column=2, row=1, padx=10, pady=10)
    stateLabel.grid(column=3, row=1, padx=10, pady=10)
    stateCombo.grid(column=4, row=1, padx=10, pady=10)
    zipLabel.grid(column=5, row=1, padx=10, pady=10)
    zipEntry.grid(column=6, row=1, padx=10, pady=10)
    
    saveButton.pack(side='right', padx=10, pady=10, fill='both')
    cancelButton.pack(side='right', padx=10, pady=10, fill='both')


    window.run() ##open the window

def saveEntry(root, window, frame, info, framesList):
    ##this function checks the input for errors, then saves the information to the database
    ##or gives a warning message if errors are present.

    for value in info[1:4]:
        if not value.get() and info.index(value)<=3: ##if title, start time, or end time is not defined
            root.removeWidgets(frame)
            errorLabel = tk.Label(frame, text="Each entry must have a title, start time, and end time.", fg="Red")
            errorLabel.pack(pady=10)
            return
        
    try:
        root.cursor.execute(f"""SELECT diary_id, diaryOrg_id FROM diaryinfopgvw WHERE title="{info[0]}";""")
    except Exception as e:
        print(f"Save Entry Get DiaryId, OrgId:\n{e}\n{info[0]}")
        return
    
    match(info[5].get()):
        case 'None': priority=0
        case 'Low': priority=1
        case 'Medium': priority=2
        case 'High': priority=3
        case _: priority=0
    diary_id, org_id = root.cursor.fetchall()[0]

    try:
        root.cursor.execute(f"""SELECT entryType_id FROM entryTypes WHERE name="{info[6].get()}";""")
    except Exception as e:
        print(f"Save Entry Get entryTypeId:\n{e}")
        return
    entryType_id = root.cursor.fetchall()[0][0]
    
    loc_id='NULL'

    try:
        root.cursor.execute(f"""INSERT INTO teamsweetdreams_dms.entries
(entry_title, start_time, end_time, description, priority, entryType_id, entryOwner_id, entryOrg_id, entryDiary_id, location_id)
VALUES ("{info[1].get()}", "{info[2].get()}", "{info[3].get()}", "{info[4].get()}", {priority}, {entryType_id}, {root.currentUser_id}, {org_id}, {diary_id}, {loc_id})""")
        root.connection.commit()

    except Exception as e:
        print(f"save Entry insert into Entries: {e}")

    iterateEntries(root, framesList[4], info[0])

    window.removeWidgets()
                


def iterateEntries(root, entryFrame, diaryTitle, query=None):

    def x(entryFrame, title, color):
        lis=entryFrame.winfo_children()
        for i in lis:
            if isinstance(i, Button):
                if i['text']==title:
                    style = Style().configure(f"{role[1]}.TButton",
                                              foreground=f"#{color}")##color is the role color
                    i['style'] = f"{role[1]}.TButton"
    #reset the frame                
    root.removeWidgets(entryFrame)

    if not query:
        query = f"""SELECT entry_title, start_time, priority, entryOwner_id
FROM EntryInfoPgVW WHERE diary_title = "{diaryTitle}" ORDER BY priority DESC;"""

    root.cursor.execute(query)
    entries = root.cursor.fetchall()

    role = root.getCurrentUserRoleDetails()
    root.cursor.execute(f"""SELECT hexcode FROM Colors WHERE color_id={role[-1]}""")
    color = root.cursor.fetchall()[0][0]
    
    for item in entries:
        startTime=''
        if item[1]:
            startTime=datetime.datetime.strftime(item[1], "%m/%d/%y %I:%M %p")
        txt=f"{item[0]}\n{startTime}"
        img=getPriorityImage(priority=item[2])
        entryButton = Button(entryFrame, text=txt, width=60, image=img, compound=tk.LEFT,
                             command=lambda:showEntryDetails(entryFrame, entryId=None))
        entryButton.pack(fill='both', padx=10, pady=10)
        entryButton.image=img
        if item[3] == root.currentUser_id:
            x(entryFrame, txt, color)


        
def getPriorityImage(priority=None):
    ##returns an image to display next to an entry based on the entry's priority
    if priority:
        img = Image.open("exclamation.png") # load image
        resized_image = img.resize((25,25), Image.Resampling.LANCZOS) # resize, remove structural padding
        new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
        return new_image   




def showEntryDetails(entryFrame, entryId=None):
    ##creates a popup that shows the details for a specified entry

    ##create the popup
    window = RootWindow(title=f"Entry {entryId}")
    window.root.geometry("500x500")
    
    ##define the contents
    frame1 = tk.Frame(window.root)
    nameLabel=tk.Label(frame1, text="This is what will display all of the details of the entry.")

    
    ##only passing the window to Save,
    ##so master of .removeWidgets(master) is None, which will close the whole window.
    editButton=tk.Button(frame1, text='Edit Entry', command=lambda:editEntry(window, frame1))
    closeButton=tk.Button(frame1, text='Close', command=lambda:window.removeWidgets(master=None))##this command will be changed later

    ##Add the contents to the window
    frame1.pack()
    nameLabel.grid(column=1, row=1)
    editButton.grid(column=3, row=2, padx=5)
    closeButton.grid(column=4, row=2, padx=5)
    
    window.run() ##open the window




def editEntry(window, frame):
    window.removeWidgets(master=frame) ##remove all contents from the frame
    nameLabel=tk.Label(frame, text="Title:")
    nameEntry=tk.Entry(frame)

    ##only passing the window to Save,
    ##so master of .removeWidgets(master) is None, which will close the whole window.
    saveButton=tk.Button(frame, text='Save Changes', command=lambda:Save(window))

    ##Add the contents to the window
    frame.pack()
    nameLabel.grid(column=1, row=1)
    nameEntry.grid(column=2, row=1)
    saveButton.grid(column=3, row=2)
    
    window.run() ##open the window


def searchEntries(root, entryFrame, diaryTitle, criteria, details):
    query= ''
    match criteria:
        case "Place":
            query=f"""SELECT location_id, address_ln_1, address_ln2, city, state, zip FROM EntryInfoPgVW WHERE (address_ln_1 LIKE "%{details}%" OR address_ln2 LIKE "%{details}%" OR city LIKE "%{details}%" OR state LIKE "%{details}%" OR zip LIKE "%{details}%")AND title = "{diaryTitle}";"""
        case "Date":
            query=f"""SELECT entry_title, start_time FROM EntryInfoPgVW WHERE start_time LIKE "{details}%";"""

        case "Time":
            query=f"""SELECT entry_title, start_time FROM EntryInfoPgVW WHERE start_time LIKE "%{details}";"""

        case "Duration":
            query=f"""SELECT entry_title, start_time FROM EntryInfoPgVW WHERE duration LIKE "{details}";"""
    iterateEntries(root, entryFrame, diaryTitle, query=query)
    

def searchHelper(root, searchFrame, entryFrame, diaryTitle, criteria):
    root.removeWidgets(searchFrame)

    t="" 
    match criteria:
        case "Date":
            t="Enter a Date (format: yyyy-mm-dd):"
        case "Time":
            t="Enter a Time (HH:MM:SS):"
        case "Duration":
            t="Enter Duration (hours): "
        case "Place":
            t="Enter a Place: "
        case "No Criteria":
            t ='''Choose Criteria above and
press 'Go' to confirm selection.
Then, type details in the entry
box on the right.'''
         
    searchLabel2=tk.Label(searchFrame, text=t, font=("Helvetica", 11), bg='White', fg="Purple")
    searchLabel2.pack(side='left', pady=10, padx=10)

    
    searchEntry = tk.Entry(searchFrame)
    searchButton=tk.Button(searchFrame, text="Search", font=("Helvetica", 11), bg='Pink', 
                           command=lambda:searchEntries(root, entryFrame, diaryTitle, criteria, searchEntry.get()))
    
    searchButton.pack(side='right', padx=5)
    searchEntry.pack(side='right', padx=5)


def populateSearchFrame(root, framesList, diaryTitle, currentOrg):
    srf=framesList[3]
    root.removeWidgets(srf)
    searchFrame1 = tk.Frame(srf, bg='White')
    searchLabel1=tk.Label(searchFrame1, text="Search by:", font=("Helvetica", 15), bg='White')
    searchLabel1.pack(side='left', padx=10, pady=10)

    searchByCombo = Combobox(searchFrame1, width=12, state="readonly", font=('Helvetica', 13))
    searchByCombo['values']= ("No Criteria", "Date", "Time", "Duration", "Place")
    searchByCombo.set("No Criteria Set")
    searchByCombo.current(0)

    searchFrame2 = tk.Frame(srf, bg="Purple", highlightbackground="Pink", highlightthickness=2)
    searchHelper(root, searchFrame2, framesList[4], diaryTitle, searchByCombo.get())
    goButtonSearch = Button(searchFrame1, text="Go",
                            command=lambda:searchHelper(root, searchFrame2, framesList[4], diaryTitle, searchByCombo.get()))

    searchByCombo.pack(side='left', pady=10)
    goButtonSearch.pack(side='left', padx=10)


    searchFrame1.pack(side='top', fill='both', pady=10)
    searchFrame2.pack(side='top', fill='both')

    


def MainPage(root):
    root.removeWidgets(root.root)
    root.root.config(bg='Purple') ##set the main window's background to purple
    ##takes the RootWindow object as a parameter
    ##controls the layout for the whole main window

    root.setCurrentPage("Main")

    availableSpace, aW, aH = banner(root) ## display the banner and borders of the main page

    optionsFrameWidth, optionsFrameHeight = (int(aW*0.2), aH)
    calendarFrameWidth, calendarFrameHeight = (int(aW*0.6), aH)
    entryFrameWidth, entryFrameHeight=(int(aW*0.2), aH)

    ##main page frames
    optionsFrame = tk.Frame(availableSpace, bg="Purple", width=optionsFrameWidth, height=optionsFrameHeight)
    calendarFrame = tk.Frame(availableSpace, bg="Purple", width=calendarFrameWidth, height=calendarFrameHeight)
    searchEntryFrame = tk.Frame(availableSpace, bg="Purple", width=entryFrameWidth, height=entryFrameHeight)
    searchFrame=tk.Frame(searchEntryFrame, bg="Purple", width=entryFrameWidth, height=100)
    entryFrame=tk.Frame(searchEntryFrame, bg="Purple", width=entryFrameWidth, height=entryFrameHeight)
    
    availableSpace.pack(fill='both')
    
    optionsFrame.grid(column=1, row=1, sticky='nsew')
    calendarFrame.grid(column=2, row=1, sticky='nsew', padx=10)
    searchEntryFrame.grid(column=3, row=1, sticky='nsew')
    searchFrame.grid(column=1, row=1, sticky='nsew')
    entryFrame.grid(column=1, row=2, sticky='nsew')

    framesList = [optionsFrame, calendarFrame, searchEntryFrame, searchFrame, entryFrame]

    populateOptionsFrame(root, framesList)

