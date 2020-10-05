import subprocess as sp
from datetime import datetime

from exec import qexec
inf = 1000000

def modhead():

    try:
        
        dno = int(input("Enter department number whose head is to be changed: "))

        query = """select * from Heads where Dno = %d""" % (dno)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid department number. No such department.")
            return -1

        query = """select * from Staff where Staff_Id = %d""" % (res[0]["Staff_Id"])
        if(qexec(query)): 
            return -1; 
        head = cur.fetchall()

        print("Current head id = ", head[0]["Staff_Id"])
        print("Current head name = ", head[0]["First_Name"], head[0]["Last_Name"])
        hid = int(input("Enter new head's staff id: "))
        query = """update Heads set Staff_Id = %d where Dno = %d""" % (hid, dno)
        if(qexec(query)): 
            return -1; 

        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
