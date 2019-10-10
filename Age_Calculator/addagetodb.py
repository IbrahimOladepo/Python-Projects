# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:24:21 2016

@author: IbrahimOladepo
"""

import sqlite3

def addagetodb(data):
    # Saving data in sqlite3 database  
    try:
        con = sqlite3.connect('realdatabase.sqlite')
        cur = con.cursor()
        
        global log
        if (data[0][1] < 19 ):
            cur.execute("SELECT name FROM agetable_18below")
            names = cur.fetchall()

            global log
            log = 0
            for i in names:
                if (i[0] == data[0][0]):
                    log = 1; break
                else:
                    log = 0
            
            if (log == 0):
                # name does not already exist
                cur.executemany("INSERT INTO agetable_18below VALUES(?, ?, ?)", data)
            else:
                # name already exists
                cur.executemany("UPDATE agetable_18below SET years = ?, days = ? WHERE name = ?", 
                                [(data[0][1], data[0][2], data[0][0])])
        elif (data[0][1] < 41):
            cur.execute("SELECT name FROM agetable_18to40")
            names = cur.fetchall()

            global log2
            log2 = 0
            for i in names:
                if (i[0] == data[0][0]):
                    log2 = 1; break
                else:
                    log2 = 0
            
            if (log2 == 0):
                # name does not already exist
                cur.executemany("INSERT INTO agetable_18to40 VALUES(?, ?, ?)", data)
            else:
                # name already exists
                cur.executemany("UPDATE agetable_18to40 SET years = ?, days = ? WHERE name = ?", 
                                [(data[0][1], data[0][2], data[0][0])])
        else:
            cur.execute("SELECT name FROM agetable_40plus")
            names = cur.fetchall()
            
            global log3
            log3 = 0
            for i in names:
                if (i[0] == data[0][0]):
                    log3 = 1; break
                else:
                    log3 = 0
            
            if (log3 == 0):
                # name does not already exist
                cur.executemany("INSERT INTO agetable_40plus VALUES(?, ?, ?)", data)
            else:
                # name already exists
                cur.executemany("UPDATE agetable_40plus SET years = ?, days = ? WHERE name = ?", 
                                [(data[0][1], data[0][2], data[0][0])])
            
        con.commit()
        cur.close()
        con.close()
    except IOError as Err:
        print("Error somewhere: " + str(Err))