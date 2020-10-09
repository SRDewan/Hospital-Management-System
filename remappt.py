import subprocess as sp
import random
from datetime import datetime

from exec import qexec

def delappt():

    try:
        tmp = sp.call('clear', shell = True)
        pid = int(input("Enter Patient Id whose appointment is to be removed: "))
        ad = (input("Enter Appointment Date (YYYY-MM-DD): "))
        at = (input("Enter Appointment Time (HH:MM:SS): "))
        
        query = """SELECT * FROM Schedules WHERE Patient_Id = %d and Time = "%s" and Date = "%s" """ % (pid, at, ad)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid entry. No such appointment.")
            return -1

        query = """SELECT * FROM Prescription WHERE Pno = %d""" % (res[0]["Pno"])
        if(qexec(query)): 
            return -1; 
        pre = cur.fetchall()
        if(pre != ()):
            print("Error. Cannot cancel a completed appointment.")
            return -1

        query = "DELETE FROM Schedules WHERE Pno = %d" % (res[0]["Pno"])
        if(qexec(query)): 
            return -1; 
        query = """DELETE FROM Appointment WHERE Time = "%s" and Date = "%s" """ % (res[0]["Time"], res[0]["Date"])
        if(qexec(query)): 
            return -1; 

        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
