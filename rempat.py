import subprocess as sp
import random
from datetime import datetime

from exec import qexec

def delins(pid):

    query = "select Insurance_Id from Insured_Patients where Patient_Id = %d" % (pid)
    if(qexec(query)):
        return -1
    ins = cur.fetchall()

    query = """delete from Insured_Patients where Patient_Id = %d""" % (pid)
    if(qexec(query)):
        return -1;

    for x in ins:
        query = """delete from Insured_Details where Insurance_Id = %d""" % (x["Insurance_Id"])
        if(qexec(query)):
            return -1;

    return 0

def delpat():

    try:
        tmp = sp.call('clear', shell = True)
        pid = int(input("Enter Patient Id of patient to be removed: "))

        query = """select * from Patient where Patient_Id = %d""" % (pid)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid id. No such patient.")
            return -1

        if(delins(pid)):
            return -1

        query = """delete from Patient where Patient_Id = %d""" % (pid)
        if(qexec(query)):
            return -1;
        
        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
