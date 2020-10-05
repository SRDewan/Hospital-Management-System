import subprocess as sp
import pymysql
import pymysql.cursors
import random
from datetime import datetime

import exec
import addstaff
import addpat
import remstaff
import rempat
import info

inf = 1000000


def remove(opt):

    if(opt == 1):
        if(delstaff()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(opt == 2):
        if(delpat()):
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
    else:
        print("Error: Invalid Option")


def dispatch(ch):

    if(ch == 1):
        print("1. Add staff member")
        print("2. Add patient")
        opt = int(input("Enter choice: "))
        tmp = sp.call('clear', shell=True)
        add(opt)

    # elif(ch == 2):

    elif(ch == 3):
        print("1. Remove staff member")
        print("2. Remove patient")
        opt = int(input("Enter choice: "))
        tmp = sp.call('clear', shell=True)
        remove(opt)

    elif(ch == 4):
        print("1. Show details of available rooms")
        print("2. Show details of staff with particular shiftday")
        print("3. Show all doctor of particular specialisation")
        print("4. Show all insured patients with particular insurance company")
        print("5. Show contact of particular patient")
        print("6. Show complaint and diagonosis of particular prescription")
        print("7. Show bill amount for particular bill")
        print("8. Show details of particular department")
        print("9. Show quantity of particular medicine")
        print("10. Show details of particular patient using patient name")
        print("11. Show details of particular staff using staff name")
        print("12. Show details of particular department using department name")
        print("13. Show details of particular medicine using medicine name")
        print("14. Show details of particular medicine using supplier name")
        opti = int(input("Enter choice: "))
        tmp = sp.call('clear', shell=True)
        info(opti)

    elif(ch == 6):
        print("Goodbye! Have a nice day!")
    else:
        print("Error: Invalid Option")

    tmp = input("Enter any key to CONTINUE:")
    return 0


def options():

    print("1. Add entity")
    print("2. Modify entity")
    print("3. Delete entity")
    print("4. Information retrieval")
    print("5. Analysis information")
    print("6. Logout")
    ch = int(input("Enter choice: "))
    tmp = sp.call('clear', shell=True)
    dispatch(ch)
    return ch


while(1):

    tmp = sp.call('clear', shell=True)

    username = input("Username: ")
    password = input("Password: ")

    host = input("*Host: ")
    if(host == ""):
        host = "localhost"

    iport = input("*Port: ")
    if(iport == ""):
        port = 3306
    else:
        port = int(iport)
    # username = "srd"
    # password = "rris0711"
    # host = "localhost"
    # port = 3306

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
            remstaff.cur = cur
            from remstaff import delstaff, deldoc, deldept
            rempat.cur = cur
            from rempat import delpat, delins
            addstaff.cur = cur
            from addstaff import addstaff, addedu, adddoc, adddept, addshift
            addpat.cur = cur
            from addpat import addpat, addins

            while(ret != 6):
                tmp = sp.call('clear', shell=True)
                ret = options()

    except pymysql.Error as e:
        tmp = sp.call('clear', shell=True)
        print(
            "Could not establish connection! Error pymysql %d: %s" %
            (e.args[0], e.args[1]))
        tmp = input("Enter any key to CONTINUE:")
