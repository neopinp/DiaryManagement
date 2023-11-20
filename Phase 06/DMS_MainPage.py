##Team Sweet Dreams Diary Management System
##created on: 11/15/23
##last updated: 11/19/2023

##The following code defines the main screen for the Diary Management System.
##If a user is logged in successfully, this screen will appear.

import tkinter as tk
from RootWindow import RootWindow
import calendar
import datetime
from tkinter import messagebox, PhotoImage
from tkinter.ttk import Combobox, Button, Style
from PIL import Image, ImageTk

def banner(root):
    ##creates the banner at the top of the screen and the spacers on the side
    ##returns the space left on the screen

    aW, aH = root.screen_width, root.screen_height ##available width and height of the screen
    topW, topH = root.screen_width, 75 ##width and height of top banner
    spacerW, spacerH = 20, aW-topH ##width and height of side spacers

    aW-=spacerW*2
    aH-=topH
    
    ##rewrite the width and height to variables to reduce hardcoded numbers
    topBanner = tk.Frame(root.root, bg="Red", width=topW, height=topH)
    leftSpacer = tk.Frame(root.root, bg="Green",width=spacerW, height=spacerH)
    rightSpacer = tk.Frame(root.root, bg="Green",width=spacerW, height=spacerH)
    mainFrame = tk.Frame(root.root, bg="Purple", width=aW, height=aH)
    
    frame11 = tk.Frame(topBanner, height=100, width=300)
    frame112 = tk.Frame(frame11, bg='Red', height=50, width=200)
    frame113 = tk.Frame(frame11, bg='Red', height=50, width=200)
    frame114 = tk.Frame(frame11, bg='Red', height=topH, width=topH)

    nameLabel = tk.Label(frame112, text=f'{root.getCurrentUserDetails()[3]}', font=('Helvetica', 14), bg='Red')
    roleLabel = tk.Label(frame113, text=f'Role', font=('Helvetica', 11), bg='Red')

    img=getImage("gear.png", topH-5, topH-5)
    settingsButton = tk.Button(frame114, image=img, command=lambda:openSettings(root))
    settingsButton.image=img

    topLabel = tk.Label(topBanner, text="Diary Management System", font=("Helvetica", 35), bg="Red", fg="White")

    topBanner.pack(side='top', fill="both")
    leftSpacer.pack(side='left', fill="both")
    rightSpacer.pack(side='right', fill="both")
    frame11.pack(side='right', fill="both")
    topLabel.pack(side='left', padx=20, pady=5)
    frame114.pack(side='right', fill="both")
    frame112.pack(fill="both")
    frame113.pack(fill="both")
    nameLabel.pack(padx=10, pady=10, fill='both')
    roleLabel.pack(padx=10, fill='both')
    settingsButton.pack(padx=10, pady=10)

    
    return mainFrame, aW, aH

def openSettings(root):
    ##opens the Settings window
    ##that allows a user to view their user information
    ##or add, update, depete that information if the user is an Admin.

    ##create the popup
    settingsWindow = RootWindow(title="Edit Organization")
    settingsWindow.root.geometry("500x500")
    
    ##define the contents
    frame1 = tk.Frame(settingsWindow.root, bg="Blue")
    nameLabel=tk.Label(frame1, text="Organization name:")
    nameEntry=tk.Entry(frame1)
    
    ##only passing the window to Save,
    ##so master of .removeWidgets(master) is None, which will close the whole window.
    saveButton=tk.Button(frame1, text='Save Changes', command=lambda:Save(settingsWindow))
    backButton=tk.Button(frame1, text='<- Back', command=lambda:closeWindow(settingsWindow))
    

    ##Add the contents to the window
    frame1.pack()
    nameLabel.grid(column=1, row=2)
    nameEntry.grid(column=2, row=2)
    saveButton.grid(column=3, row=3)
    backButton.grid(column=1, row=1)
    cancelButton.grid(column=2, row=2, padx=5, pady=10, sticky='nsew')

    settingsWindow.run()


def getImage(filename, w, h):
    ##returns an image to display, resized.
    img = Image.open(filename) # load image
    resized_image = img.resize((w,h), Image.Resampling.LANCZOS) # resize, remove structural padding
    new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
    return new_image


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
    diaryListFrame = tk.Frame(opf, bg="Purple")
    diaryListFrame.pack(fill='both')

    if diaryListFrame not in framesList:
        framesList.append(diaryListFrame)

    ##Add heading labels
    heading=tk.Label(headingFrame, text="Organization", font=('Helvetica', 20), bg="Purple", fg="Light Blue")
    heading.pack(padx=10, pady=10)
    heading2=tk.Label(headingFrame2, text="Diaries", font=('Helvetica', 18), bg="Purple", fg="Light Blue")
    heading2.pack(padx=10, pady=10)

    userOrgData = root.getUserOrgData()

    orgs=[]
    for item in userOrgData:
        orgs.append(item[-1]) ##append organization name

    orgsCombo = Combobox(comboFrame, font=('Helvetica', 12), state="readonly")
    orgsCombo['values']=orgs
    orgsCombo.current(0)
    orgsCombo.pack(side='left', padx=10)

        
    ##get all diaries a user has access to and the organization it is associated with(title and id)   
    userDiaryData=root.getUserDiaryData()

    showDiariesButton = tk.Button(comboFrame, text='Show Diaries', font=('Helvetica', 11),
                                  bg="Red", command=lambda:showOrgDiaries(root, framesList, orgsCombo.get()))
    editButton = tk.Button(comboFrame, text='Edit', font=('Helvetica', 11),
                                   bg="Pink", command=lambda:EditOrg(orgsCombo.get()))
    #editButton.configure(command=lambda editButton=editButton:EditOrg())
    
    showDiariesButton.pack(side='left', padx=5)
    editButton.pack(side='left', padx=5)

    showOrgDiaries(root, framesList, orgsCombo.get())






def showOrgDiaries(root, framesList, currentOrg, returnTitle=None):
    dlf = framesList[5]
    root.removeWidgets(dlf)
    
    ##Show a button for each diary associated with an organization
    data=root.getUserDiaryData()
    for item in data:
        if item[1]==currentOrg: ##if the organization name is the same as the one in the combobox
            diaryButton = tk.Button(dlf, text=item[0], font=('Helvetica', 11),
                    bg="Pink", width=20)
            diaryButton.config(command=lambda diaryTitle=item[0], diaryButton = diaryButton: createDiary(root, framesList, currentOrg, diaryTitle=diaryTitle))
            diaryButton.pack(padx=5, pady=10)
            
    ##if permission allows:
    addDiaryButton = tk.Button(dlf, text="Add Diary", font=('Helvetica', 11),
        bg="Pink", width=20, command=lambda:editDiary(root, currentOrg, framesList)) ##pass with no third parameter prompts to add new
    addDiaryButton.pack(padx=5, pady=10)

    createDiary(root, framesList, currentOrg, diaryTitle=returnTitle)

    


def saveDiary(root, window, frame, title, subject, currentOrg, framesList, action, oldTitle=None):
    if not title:
        errorLabel = tk.Label(frame, text="Please enter a title.")
        errorLabel.grid(column=2, row=4, padx=10, pady=15)
        return
    now = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')

    if action == 'new':
        try:
            root.cursor.execute(f"SELECT org_id FROM Organizations WHERE org_name = '{currentOrg}'")
            org_id = root.cursor.fetchall()[0]

            root.cursor.execute(f"""INSERT INTO Diaries (title, date_created, last_updated, owner_id, subject, diaryOrg_id)
            VALUES("{title}", "{now}", "{now}", {root.currentUser_id}, "{subject}", {org_id});""")
            root.connection.commit()
            
            root.cursor.execute(f"""INSERT INTO UserDiaries (user_id, diary_id) VALUE ({root.currentUser_id}, (SELECT MAX(LAST_INSERT_ID()) FROM Diaries));""")
            root.connection.commit()
        except Exception as e:
            print(e)

    elif action == 'edit':
        try:
            root.cursor.execute(f"SELECT diary_id FROM Diaries WHERE title='{oldTitle}'")
            diary_id = root.cursor.fetchall()[0]
            root.cursor.execute(f"""UPDATE Diaries
SET title="{title}", last_updated="{now}", subject="{subject}" WHERE diary_id='{int(diary_id)}';""")
            root.connection.commit()
        except Exception as e:
            print(e)

    window.removeWidgets(master=None) ##close the window
    showOrgDiaries(root, framesList, currentOrg, title)


def editDiary(root, currentOrg, framesList, diary=None):
    ##opens a new window that allows a user
    ##to edit a diary's information
    ##if diary=None, it prompts to create a new diary.

    ##create the popup
    window = RootWindow(title="Edit Diary")
    window.root.geometry("800x200")
    
    ##define the contents
    frame1 = tk.Frame(window.root, bg="Blue")
    titleLabel=tk.Label(frame1, text="Diary title:")
    titleEntry=tk.Entry(frame1)
    subjectLabel=tk.Label(frame1, text="Subject:")
    subjectEntry=tk.Entry(frame1, width=100)
    cancelButton=tk.Button(frame1, text='Cancel', command=lambda:window.root.destroy())
    
    ##only passing the window to Save,
    ##so master of .removeWidgets(master) is None, which will close the whole window.
    saveButton=tk.Button(frame1, text='Save')
    saveButton.config(command=lambda cO=currentOrg,
                    saveButton=saveButton:saveDiary(root, window, frame1, titleEntry.get(), subjectEntry.get(), cO, framesList))

    
    
    if diary:
        root.cursor.execute(f"SELECT diary_id, subject FROM Diaries WHERE title='{diary}'")
        data = root.cursor.fetchall()[0]
        diary_id, subject = data[0], data[1]
        
        if titleEntry.get():
            titleEntry.delete(0, tk.END)
        titleEntry.insert(0, diary)
        if subjectEntry.get():
            subjectEntry.delete(0, tk.END)
        subjectEntry.insert(0, subject)

        saveButton.config(command=lambda cO=currentOrg,
            saveButton=saveButton:saveDiary(root, window, frame1, titleEntry.get(),
                                            subjectEntry.get(), cO, framesList, action='edit', oldTitle=diary))
        
    else:
        saveButton.config(command=lambda cO=currentOrg,
            saveButton=saveButton:saveDiary(root, window, frame1, titleEntry.get(), subjectEntry.get(),
                                            cO, framesList, action='new'))

    ##Add the contents to the window
    frame1.pack(fill='both')
    titleLabel.grid(column=1, row=1, padx=10, pady=10, sticky='nsew')
    titleEntry.grid(column=2, row=1, padx=10, pady=10, sticky='nsew')
    subjectLabel.grid(column=1, row=2, padx=10, pady=10, sticky='nsew')
    subjectEntry.grid(column=2, row=2, padx=10, pady=10, sticky='nsew')
    cancelButton.grid(column=3, row=3, padx=5, pady=10, sticky='nsew')
    saveButton.grid(column=4, row=3, padx=5, pady=10, sticky='nsew')


    titleEntry.focus()
    
    window.run() ##open the window


def createDiary(root, framesList, currentOrg, diaryTitle=None):

    cdf = framesList[1]
    
    ##this function populates the middle calendar frame.
    ##with the diary name and a functional calendar.

    ##Retrieve a specified user's diaries
    root.cursor.execute(f"SELECT title, org_name FROM diaryinfopgvw WHERE user_id = '{root.currentUser_id}'")
    diaries = root.cursor.fetchall()
        
    ##clear the screen
    root.removeWidgets(cdf)

    ##create title headers
    if diaryTitle == None: ##if no title is given, choose the first in the list to display.
        for item in diaries:
            if item[1]==currentOrg:
                diaryTitle = item[0]
                break

    diaryLabel=tk.Label(cdf, text=diaryTitle, font=("Helvetica", 20))
    diaryLabel.pack(side='top', pady=20)

    monthYearFrame = tk.Frame(cdf)
    monthYearFrame.pack(side='top')

    ##create the calendar
    calendarFrame=tk.Frame(cdf) ##frame for the actual calendar
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
    monthsCombo = Combobox(monthYearFrame, width=10, state="readonly")
    monthsCombo['values']=months
    monthsCombo.current((datetime.date.today().month)-1) ##index starts at 0
    monthsCombo.pack(side='left')
    
    yearsCombo = Combobox(monthYearFrame,width=8, state="readonly")
    yearsCombo['values']=years
    yearsCombo.current((datetime.date.today().year)-2023)##first index is this year (2023)
    yearsCombo.pack(side='left', pady=10)

    showCalendarButton = tk.Button(monthYearFrame, text="Show Calendar",
                                   command=lambda:showCalendar(root, calendarFrame, framesList,
                                    months.index(monthsCombo.get())+1,int(yearsCombo.get()), today, diaryTitle))
    showCalendarButton.pack(side='left', padx=5)

    editDiaryButton = tk.Button(monthYearFrame, text="Edit Diary",
                                command=lambda:editDiary(root, currentOrg, framesList, diary=diaryTitle))
    editDiaryButton.pack(side='left')

    showCalendar(root, calendarFrame, framesList, months.index(monthsCombo.get())+1, int(yearsCombo.get()), today, diaryTitle)

    iterateEntries(root, framesList[4], diaryTitle)


def showCalendar(root, calendarFrame, framesList, month, year, today, diaryTitle):
    cdf=framesList[1]
    
    
    ##clear calendar
    root.removeWidgets(calendarFrame)

    command=iterateEntries(root, framesList[4], diaryTitle)
    weekdays=[]
    ##have to pull out sunday and do it separately because it absolutely refuses all attempts to be first in the iteration
    weekdays.append(calendar.day_name[-1:][0])
    dayLabel = tk.Label(calendarFrame, text=weekdays[0])
    dayLabel.grid(column=1, row=1)
    ##iterate days
    for day in calendar.day_name[:-1]: ##get a list of all weekdays
            weekdays.append(day)
            dayLabel = tk.Label(calendarFrame, text=f'{day}')
            dayLabel.grid(column=weekdays.index(day)+1, row=1)
    
    ##get the first weekday of the month and the number of days in the month, respectively
    firstWeekday, daysInMonth = calendar.monthrange(year, month)
    dayNum=1
    blankCount=0

    for week in range(1,7): ##up to 6 weeks (rows) in one month
        for day in range(1,8): ##seven days(columns) in one week
            if dayNum <= daysInMonth:
                if blankCount < firstWeekday+1: ##add a blank label for every day before the month's first day
                    label=tk.Label(calendarFrame, text=" "*5, bg='Light Green')
                    label.grid(column=day, row=week+1, sticky='nsew')
                    blankCount+=1
                else:
                    if dayNum==today.day and today.month==month and today.year==year: ##if it is today's date
                        dayButton = tk.Button(calendarFrame,text=dayNum, width=9, height=5, bg="Pink") ##indicate in pink
                    else:
                        dayButton = tk.Button(calendarFrame, text=dayNum, width=9, height=5) ##otherwise, no indication
                    dayButton.grid(column=day, row=week+1, sticky='nsew')
                    dayNum+=1


def iterateEntries(root, entryFrame, diaryTitle):

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

    root.cursor.execute(f"""SELECT entry_title, start_time, priority, entryOwner_id
FROM EntryInfoPgVW WHERE diary_title = '{diaryTitle}'""")
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
        entryButton.pack(fill='both', padx=5, pady=5)
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



def MainPage(root):
    root.root.config(bg='Purple') ##set the main window's background to purple
    ##takes the RootWindow object as a parameter
    ##controls the layout for the whole main window

    availableSpace, aW, aH = banner(root) ## display the banner and borders of the main page

    optionsFrameWidth, optionsFrameHeight = (int(aW*0.2), aH)
    calendarFrameWidth, calendarFrameHeight = (int(aW*0.6), aH)
    entryFrameWidth, entryFrameHeight=(int(aW*0.2), aH)

    ##main page frames
    optionsFrame = tk.Frame(availableSpace, bg="Purple", width=optionsFrameWidth, height=optionsFrameHeight)
    calendarFrame = tk.Frame(availableSpace, bg="Purple", width=calendarFrameWidth, height=calendarFrameHeight)
    searchEntryFrame = tk.Frame(availableSpace, bg="Purple", width=entryFrameWidth, height=entryFrameHeight)
    searchFrame=tk.Frame(searchEntryFrame, width=entryFrameWidth, height=100)
    entryFrame=tk.Frame(searchEntryFrame, bg="Purple", width=entryFrameWidth, height=entryFrameHeight)
    
    availableSpace.pack(fill='both')
    
    optionsFrame.grid(column=1, row=1, sticky='nsew')
    calendarFrame.grid(column=2, row=1, sticky='nsew')
    searchEntryFrame.grid(column=3, row=1, sticky='nsew')
    searchFrame.grid(column=1, row=1, sticky='nsew')
    entryFrame.grid(column=1, row=2, sticky='nsew')

    framesList = [optionsFrame, calendarFrame, searchEntryFrame, searchFrame, entryFrame]

    populateOptionsFrame(root, framesList)

