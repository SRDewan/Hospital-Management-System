import subprocess as sp
import random
from datetime import datetime

from exec import qexec

def deldept(sid):

    query = """select Dno from Works_In where Staff_Id = %d""" % (sid)
    if(qexec(query)):
        return -1;
    dnos = cur.fetchall()

    query = """select Dno from Heads where Staff_Id = %d""" % (sid)
    if(qexec(query)):
        return -1;
    heads = cur.fetchall()

    query = """delete from Heads where Staff_Id = %d""" % (sid)
    if(qexec(query)):
        return -1;

    query = """delete from Works_In where Staff_Id = %d""" % (sid)
    if(qexec(query)):
        return -1;

    for dno in dnos:
        query = """select Dno from Works_In where Dno = %d""" % (dno["Dno"])
        if(qexec(query)):
            return -1;
        ents = cur.fetchall()
        if(ents == ()):
            query = """delete from Department where Dno = %d""" % (dno["Dno"])
            if(qexec(query)):
                return -1;

    for elem in heads:
        if(elem in dnos):
            continue
        flag = 1
        while(flag):
            hid = input("Enter staff id of new head of department %d: ", elem["Dno"])
            if(hid == sid):
                print("Error: Cannot use id of member being removed.")
                continue

            query = "insert into Heads values(%d, %d)" % (elem["Dno"], hid)
            if(qexec(query) == 0):
                flag = 0

    return 0

def deldoc(sid):

    query = """select * from Doctor where Staff_Id = %d""" % (sid)
    if(qexec(query)):
        return -1;
    row = cur.fetchall()

    if(row != ()):
        query = """delete from Specialisation where Staff_Id = %d""" % (sid)
        if(qexec(query)):
            return -1;

        if(deldept(sid)):
            return -1

        query = """delete from Doctor where Staff_Id = %d""" % (sid)
        if(qexec(query)):
            return -1;

    return 0

def delstaff():

    try:
        tmp = sp.call('clear', shell = True)
        sid = int(input("Enter Staff Id of staff member to be removed: "))

        query = """delete from Shift where Staff_Id = %d""" % (sid)
        if(qexec(query)): return -1; 
        query = """delete from Education where Staff_Id = %d""" % (sid)
        if(qexec(query)):
            return -1;

        if(deldoc(sid)):
            return -1

        query = """delete from Staff where Staff_Id = %d""" % (sid)
        if(qexec(query)):
            return -1;
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
