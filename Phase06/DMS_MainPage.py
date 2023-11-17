##Team Sweet Dreams Diary Management System
##11/15/23
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
    
    ##rewrite the width and height to variables to reduce hardcoded numbers
    topBanner = tk.Frame(root.root, bg="Red", width=root.screen_width, height=100)
    leftSpacer = tk.Frame(root.root, bg="Green",width=20, height=root.screen_height)
    rightSpacer = tk.Frame(root.root, bg="Green",width=20, height=root.screen_height)
    mainFrame = tk.Frame(root.root, bg="Purple", width=root.screen_width, height=root.screen_height)
    
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

    ##should return the remaining available width and height after the banner is placed
    ##return width, height


def Open(root):
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
            titleLabel = tk.Label(frame11, text=f"Organization {i}", font=('Helvetica', 30), bg="White")
            openButton = tk.Button(frame12, text='Open', font=('Helvetica', 15),
                                   width=4, bg="Red", command=lambda:Open(root))
            editButton = tk.Button(frame12, text='Edit', font=('Helvetica', 15),
                               width=4, bg="Pink", command=lambda:EditOrg()) #will likely pass in the organization id.

            ##add the contents to the window
            
            titleLabel.pack(padx=10, pady=10)
            editButton.pack(side='right', padx=10, pady=10)
            openButton.pack(side='right', padx=10, pady=10)
            continue

        titleLabel = tk.Label(frame11, text=f"Add Organization", font=('Helvetica', 30), bg="White")
        addButton = tk.Button(frame12, text='+', font=('Helvetica', 15),
                           width=4, bg="Pink", command=lambda:EditOrg())
        titleLabel.pack(padx=10, pady=10)
        addButton.pack(side='right', padx=10, pady=10)
    


def createDiary(root, frame):
    ##this will be cleaned up in time.
    ##creates a calendar that tells you what day it is.
    ##functional but incomplete, will update soon.
    
    ##clear the screen
    root.removeWidgets(frame)

    ##create title headers
    diaryTitle="Diary"
    diaryTitle=tk.Label(frame, text=diaryTitle, font=("Helvetica", 20))
    diaryTitle.pack(side='top', pady=20)

    calendarFrame=tk.Frame(frame) ##frame for the actual calendar
    calendarFrame.pack(side='top', padx=20)

    ##create the calendar
    
    ##initialize important veriables
    today = datetime.date.today() ##date today
    weekdays=[]
    months=[]
    years=[]

    ##have to pull out sunday and do it separately because it absolutely refuses all attempts to be first in the iteration
    weekdays.append(calendar.day_name[-1:][0])
    dayLabel = tk.Label(calendarFrame, text=weekdays[0])
    dayLabel.grid(column=1, row=1)
    ##iterate days
    for day in calendar.day_name[:-1]: ##get a list of all weekdays
            weekdays.append(day)
            dayLabel = tk.Label(calendarFrame, text=f'{day}')
            dayLabel.grid(column=weekdays.index(day)+1, row=1)
    for i in calendar.month_name[1:]: ## get a list of all months
        months.append(i)
    for i in range(2023, today.year+10): ##get a list of ten years from this year, starting from 2023
        years.append(i)


    ##get inputted date information
    year=2023 ##set the year (combobox)
    month=11 ##set the month (combobox)
    
    ##get the first weekday of the month and the number of days in the month, respectively
    firstWeekday, daysInMonth = calendar.monthrange(year, month)
    dayNum=1
    blankCount=0

    for week in range(1,7): ##up to 6 weeks (rows) in one month
        for day in range(1,8): ##seven days(columns) in one week
            if dayNum <= daysInMonth:
                if blankCount < firstWeekday: ##add a blank label for every day before the month's first day
                    label=tk.Label(calendarFrame, text=" "*5, bg='green')
                    label.grid(column=day, row=week+1, sticky='nsew')
                    blankCount+=1
                else:
                    if dayNum==today.day and today.month==month and today.year==year: ##if it is today's date
                        dayButton = tk.Button(calendarFrame,text=dayNum, width=8, height=4, bg="Pink") ##indicate in pink
                    else:
                        dayButton = tk.Button(calendarFrame,text=dayNum, width=8, height=4) ##otherwise, no indication
                    dayButton.grid(column=day, row=week+1, sticky='nsew')
                    dayNum+=1


def MainPage(root):
    ##takes the RootWindow object as a parameter

    ##width, height =
    banner(root) ## display the banner and borders of the main page
    
    ##this frame is the container for the 
    optionsFrameWidth, optionsFrameHeight = ((root.screen_width-40)*0.3, root.screen_height-50)
    calendarFrameWidth, calendarFrameHeight = ((root.screen_width-40)*0.7, root.screen_height-50)
    entryFrameWidth, entryFrameHeight=((root.screen_width-40)*0.3, root.screen_height-50)

    optionsFrame = tk.Frame(root.root, bg="Purple", width=optionsFrameWidth, height=optionsFrameHeight)
    calendarFrame = tk.Frame(root.root, bg="Purple", width=calendarFrameWidth, height=calendarFrameHeight)
    entryFrame=tk.Frame(root.root, bg="Purple", width=entryFrameWidth, height=entryFrameHeight)

    optionsFrame.pack(side='left', fill='both')
    calendarFrame.pack(side='left', fill='both')
    entryFrame.pack(side='right', fill='both')

    numOrgs=5
    iterateOrgs(root, optionsFrame, numOrgs)
    


    createDiary(root, calendarFrame)

        
