import subprocess as sp
from datetime import datetime

from exec import qexec

def addroom():

    try:
        tmp = sp.call('clear', shell = True)
        room = {}
        roompr = {}

        print("Enter new room's details: ")
        room["Room_No"] = int(input("Room Number: "))
        room["Location_Floor"] = int(input("Floor Number: "))
        room["Location_Block"] = (input("Block: "))
        room["Room_Type"] = (input("Room Type: "))
        room["Available"] = 1

        roompr["Room_Type"] = room["Room_Type"]
        tariff = (input("Hourly Tariff: "))

        if(tariff != ""):
            roompr["Hourly_Tariff"] = int(tariff)
        else:
            roompr["Hourly_Tariff"] = "NULL"

        query = """insert into Room_Pricing values("%s", %s)""" % (roompr["Room_Type"], roompr["Hourly_Tariff"])
        if(qexec(query)):
            return -1

        query = """insert into Room values(%d, %d, "%s", "%s", %d)""" % (room["Room_No"], room["Location_Floor"], room["Location_Block"], room["Room_Type"], room["Available"])
        if(qexec(query)):
            return -1

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
