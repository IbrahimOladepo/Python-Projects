# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:20:59 2016

@author: IbrahimOladepo
"""
from sys import exit

# define month dictionary
months = {
                "JANUARY": 31, "FEBRUARY": 29, "MARCH": 31, "APRIL": 30, "MAY": 31,
                "JUNE": 30, "JULY": 31, "AUGUST": 31, "SEPTEMBER": 30, "OCTOBER": 31,
                "NOVEMBER": 30, "DECEMBER": 31
            }
            
# define months list
monthsList = [
                "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
                "AUGUST", "SEPTEMBER", "OCTOBER","NOVEMBER", "DECEMBER"
                ]

# define month and edit February
def defmonth(birthYear, months):        
    # edit february    
    if ((birthYear % 4) == 0):
        months["FEBRUARY"] = 29
    else:
        months["FEBRUARY"] = 28

# check if year is valid
def validyear(currentYear, birthYear):
    if (birthYear > currentYear):
        print("\nYou probably aren't human (yet).\n")
        exit()

# check if day is valid
def validday(birthMonth, birthDay):
    if not (months[birthMonth.upper()] >= birthDay):
        print("\nInvalid birthday was inputted\n")
        exit()

# check if month is valid       
def validmonth(birthMonth):
    if not (birthMonth.upper() in months):
        print("\nInvalid birthmonth was inputted\n") 
        exit()
        
def yearDays(year):
    if ((year % 4) == 0):
        return 366
    else:
        return 365

def bdayLocation(birthYear, birthMonth, birthDay):
    days = 0    
    
    # calculations
    ubm = str(birthMonth)
    index = monthsList.index(ubm.upper())
            
    for i in range(0, index):
        days = days + months[monthsList[i]]
        
    days = days + birthDay
    return days
