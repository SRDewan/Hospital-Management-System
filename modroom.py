import subprocess as sp
from datetime import datetime

from exec import qexec
inf = 1000000

def bookroom():

    try:

        rno = int(input("Enter room number: "))
        query = """select * from Room where Room_No = %d""" % (rno)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid room number. No such room.")
            return -1
        elif(res[0]["Available"] == 0):
            print("Room unavailable.")
            return -1

        bno = int(input("Enter bill number to which this room will be charged: "))
        query = """select * from Entails where Bill_No = %d""" % (bno)
        if(qexec(query)): 
            return -1; 
        ent = cur.fetchall()
        if(ent == ()):
            print("Invalid bill number. No such bill.")
            return -1
        query = """select * from Schedules where Pno = %d""" % (ent[0]["Pno"])
        if(qexec(query)): 
            return -1; 
        sched = cur.fetchall()

        dur = int(input("Enter stay duration (number of hours rounded up): "))

        query = """select * from Room_Pricing where Room_Type = "%s" """ % (res[0]["Room_Type"])
        if(qexec(query)): 
            return -1; 
        pri = cur.fetchall()
        query = """update Bill set Amount = Amount + %d, Payment_Status = "N" where Bill_No = %d""" % (pri[0]["Hourly_Tariff"] * dur, bno)
        if(qexec(query)): 
            return -1; 

        query = """insert into Stays_In values(%d, %d, %d, "%s")""" % (bno, sched[0]["Patient_Id"], rno, dur)
        if(qexec(query)):
            return -1

        query = "update Room set Available = 0 where Room_No = %d" % (rno)
        if(qexec(query)):
            return -1

        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1

def freeroom():

    try:

        rno = int(input("Enter room number: "))
        query = "update Room set Available = 1 where Room_No = %d" % (rno)
        if(qexec(query)):
            return -1

        query = "delete from Stays_In where Room_No = %d" % (rno)
        if(qexec(query)):
            return -1

        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1

def modroom():

    try:
        
        rtype = (input("Enter room type whose tariff is to be edited: "))

        query = """select * from Room_Pricing where Room_Type = "%s" """ % (rtype)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid type. No such room.")
            return -1

        print("Current room tariff = ", res[0]["Hourly_Tariff"])
        tar = float(input("Enter new tariff: "))
        query = """update Room_Pricing set Hourly_Tariff = %f where Room_Type = "%s" """ % (tar, rtype)
        if(qexec(query)): 
            return -1; 

        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
