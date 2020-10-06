import subprocess as sp
import random
from datetime import datetime

from exec import qexec

def delappt():

    try:
        tmp = sp.call('clear', shell = True)
        pid = int(input("Enter Patient Id whose appointment is to be removed: "))
        at = (input("Enter Appointment Time (HH:MM:SS): "))
        ad = (input("Enter Appointment Date (YYYY-MM-DD): "))
        
        query = """select * from Schedules where Patient_Id = %d and Time = "%s" and Date = "%s" """ % (pid, at, ad)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid entry. No such appointment.")
            return -1

        query = """select * from Prescription where Pno = %d""" % (res[0]["Pno"])
        if(qexec(query)): 
            return -1; 
        pre = cur.fetchall()
        if(pre != ()):
            print("Error. Cannot cancel a completed appointment.")
            return -1

        query = "delete from Schedules where Pno = %d" % (res[0]["Pno"])
        if(qexec(query)): 
            return -1; 
        query = """delete from Appointment where Time = "%s" and Date = "%s" """ % (res[0]["Time"], res[0]["Date"])
        if(qexec(query)): 
            return -1; 

        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
