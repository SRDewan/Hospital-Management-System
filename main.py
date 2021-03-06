import subprocess as sp
import pymysql
import pymysql.cursors
import random
from datetime import datetime
from getpass import getpass

import exec
import addstaff
import addpat
import addroom
import remshift
import remappt
import info
import analy
import modstaff
import modpat
import modroom
import modhead
import modtest
import misc

inf = 1000000


def remove(opt):

    if(opt == 1):
        if(delshift()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 2):
        if(delappt()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    else:
        print("Error: Invalid Option")


def modify(opt):

    if(opt == 1):
        if(modstaff()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 2):
        if(modpat()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0
    
    elif(opt == 3):
        if(updateAppointment()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 4):
        if(updateTestPricing()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 5):
        if(updateMedicationPricing()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 6):
        if(modtest()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 7):
        if(modroom()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 8):
        if(modhead()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 9):
        if(updatePaymentStatus()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 10):
        if(bookroom()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 11):
        if(freeroom()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    else:
        print("Error: Invalid Option")


def add(opt):

    if(opt == 1):
        if(addstaff()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 2):
        if(addpat()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 3):
        if(addroom()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 4):
        if(addAppointment()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 5):
        if(addMedication()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 6):
        if(addTestPricing()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 7):
        if(addPrescription()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 8):
    
        try:
            tmp = sp.call('clear', shell = True)
            staff_id = int(input("Enter staff id whose shift is to be added: "))
            if(addshift(staff_id)):
                con.rollback
                return -1
            else:
                con.commit()
                print("Success!")
                return 0

        except Exception as e:
            print("Error: ", e)
            return -1

    else:
        print("Error: Invalid Option")


def dispatch(ch):

    if(ch == 1):
        try:
            print("1. Add Staff Member")
            print("2. Add Patient")
            print("3. Add Room")
            print("4. Add Appointment")
            print("5. Add Medication")
            print("6. Add Test/Surgery")
            print("7. Add Prescription")
            print("8. Add Staff Member Shift")
            print("")
            print("Press ENTER to go back")
            opt = int(input("Enter choice: "))
            tmp = sp.call('clear', shell=True)
            add(opt)
        
        except Exception as e:
            print("Error: ", e)
            return -1

    elif(ch == 2):
        try:
            print("1. Edit Staff Member Details")
            print("2. Edit Patient Details")
            print("3. Edit Appointment Details")
            print("4. Edit Test/Surgery Pricing")
            print("5. Edit Medication Pricing")
            print("6. Edit Test/Surgery Result")
            print("7. Edit Room Tariff")
            print("8. Edit Department Head")
            print("9. Edit Bill Payment Status")
            print("10. Book a Room")
            print("11. Free a Room")
            print("")
            print("Press ENTER to go back")
            opt = int(input("Enter choice: "))
            tmp = sp.call('clear', shell=True)
            modify(opt)

        except Exception as e:
            print("Error: ", e)
            return -1

    elif(ch == 3):
        try:
            print("1. Delete Staff Member Shift")
            print("2. Delete Appointment")
            print("")
            print("Press ENTER to go back")
            opt = int(input("Enter choice: "))
            tmp = sp.call('clear', shell=True)
            remove(opt)

        except Exception as e:
            print("Error: ", e)
            return -1

    elif(ch == 4):
        try:
            print("1. Show details of available rooms")
            print("2. Show details of staff with particular shiftday")
            print("3. Show all doctor of particular specialisation")
            print("4. Show all insured patients with particular insurance company")
            print("5. Show contact of particular patient")
            print("6. Show complaint and diagonosis of particular prescription")
            print("7. Show bill amount for particular bill")
            print("8. Show details of particular department")
            print("9. Show details of particular patient using patient's name")
            print("10. Show details of particular staff using staff's name")
            print("11. Show details of particular medicine using medicine's name")
            print("12. Show details of particular medicine using supplier's name")
            print("13. Show details of all patient")
            print("14. Show details of all staff")
            print("")
            print("Press ENTER to go back")
            opti = int(input("Enter choice: "))
            tmp = sp.call('clear', shell=True)
            info(opti)

        except Exception as e:
            print("Error: ", e)
            return -1

    elif(ch == 5):
        try:
            print("1. Show the average, maximum and minimum bill amount in certain period of time")
            print("2. Show the total income of Hospital in certain period of time")
            print("3. Show the average, maximum and minimum salary of staff members")
            print("4. Show the total bill of a particular patient")
            print("5. Show the average, maximum and minimum hourly tariff of rooms")
            print("6. Show the schedules of a particular patient")
            print("7. Show the schedules of a particular staff")
            print("8. Show the pending bills of a particular patient")
            print("9. Show the details of treatment recommended by doctor during a particular appointment of a particular patient")
            print("10. Show the medication listed in descending order of most recommeded")
            print("11. Show the doctors listed in descending order of most treated patients")
            print("")
            print("Press ENTER to go back")
            optio = int(input("Enter choice: "))
            tmp = sp.call('clear', shell=True)
            analy(optio)

        except Exception as e:
            print("Error: ", e)
            return -1

    elif(ch == 6):
        print("Goodbye! Have a nice day!")

    elif(ch == 7):
        print("Goodbye! Have a nice day!")
        exit()

    else:
        print("Error: Invalid Option")

    tmp = input("Press ENTER to CONTINUE:")
    return 0


def options():
    try:
        print("1. Add entity")
        print("2. Modify entity")
        print("3. Delete entity")
        print("4. Information Retrieval")
        print("5. Analysis Information")
        print("6. Logout")
        print("7. Exit")
        ch = int(input("Enter choice: "))
        tmp = sp.call('clear', shell=True)
        dispatch(ch)
        return ch

    except Exception as e:
        print("Error: ", e)
        return -1

while(1):

    tmp = sp.call('clear', shell=True)

    username = input("Username: ")
    password = getpass()

    host = input("*Host: ")
    if(host == ""):
        host = "localhost"

    iport = input("*Port: ")
    if(iport == ""):
        port = 3306
    else:
        port = int(iport)

    try:
        con = pymysql.connect(host=host,
                              user=username,
                              password=password,
                              port=port,
                              db='Hospital',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected\n")
        else:
            print("Failed to connect\n")

        with con.cursor() as cur:
            ret = 0

            exec.con = con
            exec.cur = cur
            from exec import qexec

            info.cur = cur
            from info import info

            analy.cur = cur
            from analy import analy

            remshift.cur = cur
            from remshift import delshift
            remappt.cur = cur
            from remappt import delappt

            addstaff.cur = cur
            from addstaff import addstaff, addedu, adddoc, adddept, addshift
            addpat.cur = cur
            from addpat import addpat, addins
            addroom.cur = cur
            from addroom import addroom 

            modstaff.cur = cur    
            from modstaff import modstaff
            modpat.cur = cur    
            from modpat import modpat
            modroom.cur = cur    
            from modroom import bookroom, freeroom, modroom
            modhead.cur = cur    
            from modhead import modhead
            modtest.cur = cur    
            from modtest import modtest

            misc.cur = cur
            from misc import addAppointment, addMedication, addMedDetails, addBatchDetails, addSupplierDetails, addTestorSurgery, addTestPricing, addPrescription, createBill, entails, recommends, performs, schedules, updateAppointment, updateTestPricing, updateMedicationPricing, updatePaymentStatus

            while(ret != 6):
                tmp = sp.call('clear', shell=True)
                ret = options()

    except pymysql.Error as e:
        tmp = sp.call('clear', shell=True)
        print(
            "Could not establish connection! Error pymysql %d: %s" %
            (e.args[0], e.args[1]))
        tmp = input("Enter any key to CONTINUE:")
