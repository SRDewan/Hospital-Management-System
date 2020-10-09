import subprocess as sp
import random
from datetime import datetime

from exec import qexec
shifts = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def delshift():

    try:
        tmp = sp.call('clear', shell = True)
        sid = int(input("Enter Staff Id whose shift is to be removed: "))
        shst = (input("Enter Shift Start Time (HH:MM:Ss): "))
        shet = (input("Enter Shift End Time (HH:MM:Ss): "))

        sd = "Holiday"
        while sd not in shifts:
            sd = (input("Shift Day: "))
        
        query = """SELECT * FROM Shift WHERE Staff_Id = %d and Shift_Start_Time = "%s" and Shift_End_Time = "%s" and Shift_Day = "%s" """ % (sid, shst, shet, sd)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid entry. No such shift entry.")
            return -1

        query = """DELETE FROM Shift WHERE Staff_Id = %d and Shift_Start_Time = "%s" and Shift_End_Time = "%s" and Shift_Day = "%s" """ % (sid, shst, shet, sd)
        if(qexec(query)): 
            return -1; 

        query = """SELECT * FROM Shift WHERE Staff_Id = %d""" % (sid)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Staff member must have atleast one shift. Please enter more shifts and then DELETE.")
            return -1

        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
