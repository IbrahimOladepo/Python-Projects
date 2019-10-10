# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:55:04 2016

@author: IbrahimOladepo
"""

import time
import age_FUNCTION
import pandas as pd

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

# calculations
if (days < currentDay):
    daysOld = currentDay - days
    yearsOld = currentYear - birthYear
elif (days > currentDay):
    daysOld = (prevYearDays - days) + currentDay
    yearsOld = currentYear - birthYear - 1
else:
    daysOld = 0
    yearsOld = currentYear - birthYear

print ("\nYou are {} years old and {} days old".format(yearsOld, daysOld))

"""
# save data to file
keep = open('ageData.txt', 'a')
print(name, file = keep)
print("Runtime: " + time.strftime("%c"), file = keep)
print("age: {} years old and {} days old\n\n".format(yearsOld, daysOld), file = keep)
keep.close()
"""

# Saving data in .csv file with pandas
newdf = pd.DataFrame([(name, yearsOld, daysOld, time.strftime("%c"))], 
                      columns = ['NAME', 'YEARS_OLD', 'DAYS_OLD', 'TIME'])
try:
    if (yearsOld < 19 ):
        olddf = pd.read_csv('agedata_18below.csv')
        data = pd.concat([olddf, newdf], ignore_index=True)
        data.to_csv('agedata_18below.csv', index = False)
    elif (yearsOld < 41):
        olddf = pd.read_csv('agedata_18to40.csv')
        data = pd.concat([olddf, newdf], ignore_index=True)
        data.to_csv('agedata_18to40.csv', index = False)
    else:
        olddf = pd.read_csv('agedata_40plus.csv')
        data = pd.concat([olddf, newdf], ignore_index=True)
        data.to_csv('agedata_40plus.csv', index = False)
except:
    if (yearsOld < 19 ):
        newdf.to_csv('agedata_18below.csv', index = False)
    elif (yearsOld < 41):
        newdf.to_csv('agedata_18to40.csv', index = False)
    elif (yearsOld > 40):
        newdf.to_csv('agedata_40plus.csv', index = False)
    else:
        print("Cannot be classified.")