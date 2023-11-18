##Team Sweet Dreams Diary Management System
##created on: 11/15/23
##last updated: 11/18/2023

##The following code defines the main screen for the Diary Management System.
##If a user is logged in successfully, this screen will appear.

import tkinter as tk
from RootWindow import RootWindow
import calendar
import datetime
from tkinter import messagebox
from tkinter.ttk import Combobox

def banner(root):
    ##creates the banner at the top of the screen and the spacers on the side
    ##returns the space left on the screen

    aW, aH = root.screen_width, root.screen_height ##available width and height of the screen
    topW, topH = root.screen_width, 100 ##width and height of top banner
    spacerW, spacerH = 20, aW-topH ##width and height of side spacers

    aW-=spacerW*2
    aH-=topH
    
    ##rewrite the width and height to variables to reduce hardcoded numbers
    topBanner = tk.Frame(root.root, bg="Red", width=topW, height=topH)
    leftSpacer = tk.Frame(root.root, bg="Green",width=spacerW, height=spacerH)
    rightSpacer = tk.Frame(root.root, bg="Green",width=spacerW, height=spacerH)
    mainFrame = tk.Frame(root.root, bg="Purple", width=aW, height=aH)
    
    frame11 = tk.Frame(topBanner, height=100, width=300)
    frame112 = tk.Frame(frame11, bg='Pink', height=50, width=200)
    frame113 = tk.Frame(frame11, bg='Orange', height=50, width=200)
    frame114 = tk.Frame(frame11, bg='Blue', height=100, width=100)

    topLabel = tk.Label(topBanner, text="Diary Management System", font=("Helvetica", 45), bg="Red", fg="White")

    topBanner.pack(side='top', fill="both")
    leftSpacer.pack(side='left', fill="both")
    rightSpacer.pack(side='right', fill="both")
    frame11.pack(side='right', fill="both")
    topLabel.pack(side='left', padx=20, pady=5)
    frame114.pack(side='right', fill="both")
    frame112.pack(fill="both")
    frame113.pack(fill="both")
    
    return mainFrame, aW, aH


def Open():
    pass




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
                                   width=4, bg="Red", command=lambda:Open())
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
    


def createDiary(root, wholeFrame):
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
                if blankCount < firstWeekday: ##add a blank label for every day before the month's first day
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
        entryButton = tk.Button(frame, text=txt, width=60, height=3, command=lambda:showEntryDetails(frame, entryId=None))
        entryButton.pack(fill='both', padx=5, pady=5)
     


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

    numOrgs=5 ##get the number of organizations a user has access to
    iterateOrgs(root, optionsFrame, numOrgs)

    createDiary(root, calendarFrame)


    searchFrame=tk.Frame(entryFrame, width=entryFrameWidth, height=100)
    searchFrame.pack(fill='both')
    numEntries=4
    iterateEntries(entryFrame, entryFrameWidth, entryFrameHeight, numEntries)

    ##it is possible to grab index of specific widget (button) and reference it.
    lis=entryFrame.winfo_children()
    for i in lis:
        if isinstance(i, tk.Button):
            if entryFrame.winfo_children().index(i)==3:
                entryFrame.winfo_children()[3].config(fg='Red')
            print(i['text'])###if we know title, we can find id!!
            
        
