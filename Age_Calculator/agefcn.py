# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:18:24 2016

@author: IbrahimOladepo
"""

import time
import age_FUNCTION

def agefcn(name, birthYear, birthMonth, birthDay):
    currentYear = int(time.strftime("%Y"))
    
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
        yearsOld = currentYear - birthYear
    else:
        daysOld = 0
         
    print ("\nYou are {} years old and {} days old".format(yearsOld, daysOld))

    name = str(name)
    data = [(name.title(), yearsOld, daysOld)]    
    return data