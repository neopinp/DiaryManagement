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
from tkinter.ttk import Combobox, Button
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

def refreshPage():
    pass

def closeWindow(root, master=None):
    root.removeWidgets(master)


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

    settingsWindow.run()




def Save(root, master=None):
    ##this function will update the database with the new information.

    ##close the popup window (placeholder action for now)
    root.removeWidgets(master)




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

def populateOptionsFrame(root, frame, calendarFrame, entryFrame):
    ##populates the options frame with a way to choose an organization and show its associated diaries
    
    ##Add Frames
    headingFrame = tk.Frame(frame, bg="Purple")
    headingFrame.pack(fill='both')
    comboFrame=tk.Frame(frame, bg="Purple")
    comboFrame.pack(fill='both')
    headingFrame2 = tk.Frame(frame, bg="Purple")
    headingFrame2.pack(fill='both')
    diaryListFrame = tk.Frame(frame, bg="Purple")
    diaryListFrame.pack(fill='both')

    ##Add heading labels
    heading=tk.Label(headingFrame, text="Organization", font=('Helvetica', 20), bg="Purple", fg="Light Blue")
    heading.pack(padx=10, pady=10)
    heading2=tk.Label(headingFrame2, text="Diaries", font=('Helvetica', 18), bg="Purple", fg="Light Blue")
    heading2.pack(padx=10, pady=10)

    ##placeholder data
    ##to get real data: find the userId, put it through OrganizationMembers to get a list of all organizations the user is associated with.
    ##then, iterate through to return only those organizations.
    orgs=["Personal", "Human Resources", "Information Technology"]
    diaries = ["Diary 1", "Diary 2", "Diary 3"]
    data = {'organizations':[{"name":"Personal", "orgId":1, "diaries":["org1Diary1","org1diary2", "org1diary3"]},
         {"name":"Human Resources", "orgId":2, "diaries":["org2Diary1","org2diary2"]},
         {"name":"Information Technology", "orgId":3, "diaries":["org3Diary1","org3diary2"]}]}

    orgsCombo = Combobox(comboFrame, font=('Helvetica', 12), state="readonly")
    orgsCombo['values']=orgs
    orgsCombo.current(0)
    orgsCombo.pack(side='left', padx=10)

    showDiariesButton = tk.Button(comboFrame, text='Show Diaries', font=('Helvetica', 11),
                                  bg="Red", command=lambda:showOrgDiaries(root, diaryListFrame, data, orgsCombo.get(), calendarFrame, entryFrame))
    editButton = tk.Button(comboFrame, text='Edit', font=('Helvetica', 11),
                                   bg="Pink", command=lambda:EditOrg()) #will likely pass in the organization id.
    
    showDiariesButton.pack(side='left', padx=5)
    editButton.pack(side='left', padx=5)

    showOrgDiaries(root, diaryListFrame, data, orgsCombo.get(), calendarFrame, entryFrame)           

def showOrgDiaries(root, diaryListFrame, data, currentOrg, calendarFrame, entryFrame):
    root.removeWidgets(diaryListFrame)
    ##Show a button for wach diary associated with an organization
    for org in data['organizations']:
        if org['name']==currentOrg:
            for diary in org['diaries']:
                diaryButton = tk.Button(diaryListFrame, text=diary, font=('Helvetica', 11),
                                        bg="Pink", width=8, command=lambda:createDiary(root, calendarFrame, entryFrame))
                diaryButton.pack(padx=5, pady=10) 

def iterateOrgs(root, optionsFrame, numOrgs):
    for i in range(1,numOrgs+1): ## for Org in Organizations (where organizations is a list of organizations that belong to the logged in user)
        ##creates a frame, label, and buttons
        ##for one organization

        ##define the contents
        frame1 = tk.Frame(optionsFrame, bg="Purple", width=root.screen_width-100, height = 200)
        frame11 = tk.Frame(frame1, bg="Purple", width=2000, height=200)
        frame12 = tk.Frame(frame1, bg="Purple", width=90, height=200)
        frame1.pack(side='top', padx=5, pady=5)
        frame11.pack(side='left')
        frame12.pack(side='left')
        if i<numOrgs:
            titleLabel = tk.Label(frame11, text=f"Organization {i}", font=('Helvetica', 18), bg="White")
            openButton = tk.Button(frame12, text='Open', font=('Helvetica', 12),
                                   width=4, bg="Red", command=None)
            editButton = tk.Button(frame12, text='Edit', font=('Helvetica', 12),
                               width=4, bg="Pink", command=lambda:EditOrg()) #will likely pass in the organization id.

            ##add the contents to the window
            
            titleLabel.pack(padx=10, pady=10)
            editButton.pack(side='right', padx=10, pady=10)
            openButton.pack(side='right', padx=10, pady=10)
            continue

        titleLabel = tk.Label(frame11, text=f"Add Organization", font=('Helvetica', 18), bg="White")
        addButton = tk.Button(frame12, text='+', font=('Helvetica', 12),
                           width=4, bg="Pink", command=lambda:EditOrg())
        titleLabel.pack(padx=10, pady=10)
        addButton.pack(side='right', padx=10, pady=10)
    


def createDiary(root, wholeFrame, entryFrame):
    ##this will be cleaned up in time.
    ##creates a calendar that tells you what day it is.
    ##functional but incomplete, will update soon.
    
    ##clear the screen
    root.removeWidgets(wholeFrame)

    ##create title headers
    diaryTitle="Diary"
    diaryTitle=tk.Label(wholeFrame, text=diaryTitle, font=("Helvetica", 20))
    diaryTitle.pack(side='top', pady=20)

    monthYearFrame = tk.Frame(wholeFrame)
    monthYearFrame.pack(side='top')

    ##create the calendar
    calendarFrame=tk.Frame(wholeFrame) ##frame for the actual calendar
    calendarFrame.pack(side='top', padx=20)
    
    ##initialize important veriables
    today=datetime.date.today()
    months=[]
    years=[]

    for i in calendar.month_name[1:]: ## get a list of all months
        months.append(i)
    for i in range(2023, today.year+10): ##get a list of ten years from this year, starting from 2023
        years.append(i)

    monthsCombo = Combobox(monthYearFrame, width=10, state="readonly")
    monthsCombo['values']=months
    monthsCombo.current((datetime.date.today().month)-1) ##index starts at 0
    monthsCombo.pack(side='left')

    yearsCombo = Combobox(monthYearFrame,width=8, state="readonly")
    yearsCombo['values']=years
    yearsCombo.current((datetime.date.today().year)-2023)##first index is this year (2023)
    yearsCombo.pack(side='left', pady=10)

    showCalendarButton = tk.Button(monthYearFrame, text="Show Calendar", command=lambda:showCalendar(root, calendarFrame, months.index(monthsCombo.get())+1, int(yearsCombo.get()), today))
    showCalendarButton.pack(side='left', padx=5)

    showCalendar(root, calendarFrame, months.index(monthsCombo.get())+1, int(yearsCombo.get()), today)

def showCalendar(root, calendarFrame, month, year, today):
    ##clear calendar
    root.removeWidgets(calendarFrame)

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
                        dayButton = tk.Button(calendarFrame,text=dayNum, width=9, height=5) ##otherwise, no indication
                    dayButton.grid(column=day, row=week+1, sticky='nsew')
                    dayNum+=1

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

def iterateEntries(frame, frameWidth, frameHeight, numEntries):
    for i in range(1,numEntries+1):
        startTime=datetime.datetime.strftime(datetime.datetime.now(), "%y/%m/%d %I:%M %p")
        txt=f"Entry {i}\n{startTime}"
        img= getPriorityImage(priority=1)
        entryButton = Button(frame, text=txt, width=60, image=img, compound=tk.LEFT, command=lambda:showEntryDetails(frame, entryId=None))
        entryButton.pack(fill='both', padx=5, pady=5)
        entryButton.image=img
        
def getPriorityImage(priority=None):
    ##returns an image to display next to an entry based on the entry's priority
    if priority:
        img = Image.open("exclamation.png") # load image
        resized_image = img.resize((25,25), Image.Resampling.LANCZOS) # resize, remove structural padding
        new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
        return new_image

def getImage(filename, w, h):
    ##returns an image to display, resized.
    img = Image.open(filename) # load image
    resized_image = img.resize((w,h), Image.Resampling.LANCZOS) # resize, remove structural padding
    new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
    return new_image


def MainPage(root):
    root.root.config(bg='Purple') ##set the main window's background to purple
    ##takes the RootWindow object as a parameter
    ##controls the layout for the whole main window

    availableSpace, aW, aH = banner(root) ## display the banner and borders of the main page

    ##this frame is the container for the 
    optionsFrameWidth, optionsFrameHeight = (int(aW*0.2), aH)
    calendarFrameWidth, calendarFrameHeight = (int(aW*0.6), aH)
    entryFrameWidth, entryFrameHeight=(int(aW*0.2), aH)

    optionsFrame = tk.Frame(availableSpace, bg="Purple", width=optionsFrameWidth, height=optionsFrameHeight)
    calendarFrame = tk.Frame(availableSpace, bg="Purple", width=calendarFrameWidth, height=calendarFrameHeight)
    entryFrame=tk.Frame(availableSpace, bg="Purple", width=entryFrameWidth, height=entryFrameHeight)

    availableSpace.pack(fill='both')
    
    optionsFrame.grid(column=1, row=1, sticky='nsew')
    calendarFrame.grid(column=2, row=1, sticky='nsew')
    entryFrame.grid(column=3, row=1, sticky='nsew')

    ##possibly not needed? we'll see...
    #numOrgs=5 ##get the number of organizations a user has access to
    #iterateOrgs(root, optionsFrame, numOrgs)

    populateOptionsFrame(root, optionsFrame, calendarFrame, entryFrame)

    createDiary(root, calendarFrame, entryFrame)

    ##Image Test
    img = getPriorityImage()
    
    searchFrame=tk.Frame(entryFrame, width=entryFrameWidth, height=100)
    searchFrame.pack(fill='both')

    label = tk.Label(searchFrame, image = img) #display the image
    label.image = img ##create a reference to the object so tkinter does not make it show up transparent
    label.pack()
    
    numEntries=4
    iterateEntries(entryFrame, entryFrameWidth, entryFrameHeight, numEntries)

    ##it is possible to grab index of specific widget (button) and reference it.
    lis=entryFrame.winfo_children()
    for i in lis:
        if isinstance(i, tk.Button):
            if entryFrame.winfo_children().index(i)==3:
                entryFrame.winfo_children()[3].config(fg='Red')
            print(i['text'])###if we know title, we can find id!!

            
        
