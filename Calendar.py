# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Create a calendar that user be able to choose to: view calendar, delete an event, change an event, delete an event. Program should  behave in the following way: prompt the user to view, update, or delete an event in calendar.")
from time import sleep, strftime
FIRST_NAME = "Petru"
calendar = {}
def welcome():
  print("Welcome " + FIRST_NAME + " .")
  print("Calendar is open")
  sleep(1)
  print(" Today is " + strftime("%A %B %d, %Y"))
  print(strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do")
def start_calendar():
  welcome()
  start = True 
  while start:
    user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print("Calendar is empty")
      else:
        print(calendar)
    elif user_choice == "U":
      date = input("What date: ")
      update = input("Enter the update: ")
      calendar[date] = update 
      print("Update performed successfuly")
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print("The date entered is invalid")
        try_again = input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else: 
          start = False 
      else:
        calendar[date] = event 
        print("Event was successfully added")
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("The calendar is empty")
      else:
        event = input("What event?: ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print("The event was deleted successfully")
          else:
            print("Incorrect event specified")
    elif user_choice == "X":
        start = False 
    else:
        print("Invalid command was entered")
        
start_calendar()
