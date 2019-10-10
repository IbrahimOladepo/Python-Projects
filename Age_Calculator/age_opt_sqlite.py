# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:55:04 2016

@author: IbrahimOladepo
"""

import time
import age_FUNCTION
import sqlite3

# inputs
name = input("Enter your name: ")        

# input year of birth and check validity
currentYear = int(time.strftime("%Y"))
birthYear = int(input("Enter birthYear: "))
age_FUNCTION.validyear(currentYear, birthYear)

# input month of birth and check validity
birthMonth = input("Enter birthMonth: ")
age_FUNCTION.validmonth(birthMonth)

# input day of birth and check validity
birthDay = int(input("Enter birthDay: "))
age_FUNCTION.validday(birthMonth, birthDay)

prevYearDays = age_FUNCTION.yearDays(currentYear - 1)
days = age_FUNCTION.bdayLocation(birthYear, birthMonth, birthDay)
currentDay = int(time.strftime("%j"))

# some calculations
if (days < currentDay):
    daysOld = currentDay - days
    yearsOld = currentYear - birthYear
elif (days > currentDay):
    daysOld = (prevYearDays - days) + currentDay
    yearsOld = currentYear - birthYear - 1    
    yearsOld = currentYear - birthYear
else:
    daysOld = 0
     
print ("\nYou are {} years old and {} days old".format(yearsOld, daysOld))

# Saving data to sqlite3 database  
try:
    con = sqlite3.connect('agedata.sqlite')
    cur = con.cursor()
    data = [(name.title(), time.strftime("%c"), yearsOld, daysOld)]
    
    if (yearsOld < 19 ):
        cur.executemany("INSERT INTO agetable_18below VALUES(?, ?, ?, ?)", data)
    elif (yearsOld < 41):
        cur.executemany("INSERT INTO agetable_18to40 VALUES(?, ?, ?, ?)", data)
    else:
        cur.executemany("INSERT INTO agetable_40plus VALUES(?, ?, ?, ?)", data)
        
    con.commit()
    cur.close()
    con.close()
except:
    print("Error somewhere")
