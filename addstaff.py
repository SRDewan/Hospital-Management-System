import subprocess as sp
import random
from datetime import datetime

from exec import qexec
inf = 1000000
shifts = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
jobs = ["Doctor", "Nurse", "Receptionist", "Other"]

def adddept(dno, staff_id):
        
    tmp = sp.call('clear', shell = True)
    dept = {}
    
    dept["Dno"] = dno
    dept["Dname"] = input("Department name: ")
    dept["Location_Floor"] = int(input("Floor number: "))
    dept["Location_Block"] = input("Block: ")
    query = """insert into Department values(%d, "%s", %d, "%s")""" % (dept["Dno"], dept["Dname"], dept["Location_Floor"], dept["Location_Block"])
    if(qexec(query)):
        return -1;

    return 0

def adddoc(staff_id):

    tmp = sp.call('clear', shell = True)
    doctor = {}
    special = {}
    works = {}
    heads = {}

    doctor["Staff_Id"] = staff_id
    doctor["Consultation_Fee"] = int(input("Consultation Fee: "))
    query = "insert into Doctor values(%d, %d)" % (doctor["Staff_Id"], doctor["Consultation_Fee"])
    if(qexec(query)):
        return -1;

    more = "Y"
    while(more == "Y"):
        special["Staff_Id"] = staff_id
        special["Expertise_Area"] = input("Expertise Area: ")
        query = """insert into Specialisation values(%d, "%s")""" % (special["Staff_Id"], special["Expertise_Area"])
        if(qexec(query)):
            continue
        more = input("Do you wish to enter more expertise areas (Y/N): ")

    works["Staff_Id"] = staff_id
    row = ()
    dnew = "N"

    while(row == () and dnew != "Y"):
        works["Dno"] = int(input("Department Number: "))
        query = "select Dno from Works_In where Dno = %d" % (works["Dno"])
        if(qexec(query)):
            return -1;
        row = cur.fetchall()

        if(row == ()):
            dnew = input("Department does not exist. Would you like to create a new department (Y/N): ")
            if(dnew == "Y"):
                if(adddept(works["Dno"], staff_id)):
                    return -1;

    query = "insert into Works_In values(%d, %d)" % (works["Staff_Id"], works["Dno"])
    if(qexec(query)):
        return -1;

    if(row == ()):
        heads["Staff_Id"] = staff_id
        heads["Dno"] = works["Dno"]
        query = "insert into Heads values(%d, %d)" % (heads["Dno"], heads["Staff_Id"]) 
        if(qexec(query)):
            return -1;

    return 0

def addedu(staff_id):

    tmp = sp.call('clear', shell = True)
    more = "Y"
    education = {}
    while(more == "Y"):
        education["Staff_Id"] = staff_id
        education["Degree"] = input("Degree: ")
        query = """insert into Education values(%d, "%s")""" % (education["Staff_Id"], education["Degree"])
        if(qexec(query)):
            continue 
        more = input("Do you wish to enter more degrees (Y/N): ")

    return 0

def addshift(staff_id):
    
    try:
        tmp = sp.call('clear', shell = True)
        more = "Y"
        shift = {}
        while(more == "Y"):
            shift["Staff_Id"] = staff_id

            shift["Shift_Day"] = "Holiday"
            while shift["Shift_Day"] not in shifts:
                shift["Shift_Day"] = (input("Shift Day: "))

            shift["Shift_Start_Time"] = (input("Shift Start Time (HH:MM:SS): "))
            shift["Shift_End_Time"] = (input("Shift End Time (HH:MM:SS): "))
            query = """insert into Shift values(%d, "%s", "%s", "%s")""" % (shift["Staff_Id"], shift["Shift_Start_Time"], shift["Shift_End_Time"], shift["Shift_Day"])
            if(qexec(query)):
                continue
            more = input("Do you wish to enter more shifts (Y/N): ")

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1

def addstaff():

    try:
        tmp = sp.call('clear', shell = True)
        staff = {}

        flag = 1
        query = "select Staff_Id from Staff"
        if(qexec(query)):
            return -1;
        ids = cur.fetchall()

        while(flag):
            temp = random.randint(0, inf)
            staff["Staff_Id"] = temp
            flag = 0
            for oid in ids:
                if(oid["Staff_Id"] == temp):
                    flag = 1
                    break

        print("Enter new staff member's details: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        staff["First_Name"] = name[0]
        staff["Last_Name"] = name[1]

        staff["Sex"] = "K"
        while staff["Sex"] != "F" and staff["Sex"] != "M":
            staff["Sex"] = input("Sex (F/M): ")
        
        staff["Salary"] = int(input("Salary: "))
        
        staff["Contact_No"] = "12"
        while len(staff["Contact_No"]) != 10:
            staff["Contact_No"] = input("Contact Number(10 digit): ")

        staff["Contact_No"] = int(staff["Contact_No"])
        
        staff["Date_of_Birth"] = (input("Birth Date (YYYY-MM-DD): "))

        hno = (input("*House Number: "))
        if(hno == ""):
            staff["H_No"] = "NULL"
        else:
            staff["H_No"] = int(hno)
        
        staff["Street"] = (input("*Street: "))
        zip = (input("*Zipcode: "))
        if(zip == ""):
            staff["Zipcode"] = "NULL"
        else:
            staff["Zipcode"] = int(zip)
        
        staff["City"] = (input("*City: "))

        staff["Job"] = "Cleaner"
        while staff["Job"] not in jobs:
            staff["Job"] = (input("Job(Doctor / Nurse / Receptionist / Other): "))
            
        sid = input("*Supervisor Id: ")
        if(sid != ""):
            staff["Supervisor_Id"] = int(sid)
        else:
            staff["Supervisor_Id"] = "NULL"

        query = """insert into Staff values(%d, "%s", "%s", "%s", %d, %s, "%s", %s, "%s", %s, "%s", "%s", %s)""" % (staff["Staff_Id"], staff["First_Name"], staff["Last_Name"], staff["Sex"], staff["Salary"], staff["Contact_No"], staff["Date_of_Birth"], staff["H_No"], staff["Street"], staff["Zipcode"], staff["City"], staff["Job"], staff["Supervisor_Id"])
        if(qexec(query)):
            return -1;

        if(addshift(staff["Staff_Id"])):
            return -1
        if(addedu(staff["Staff_Id"])):
            return -1

        if(staff["Job"] == "Doctor"):
            if(adddoc(staff["Staff_Id"])):
                return -1

        print("Success! Staff id of new member = ", staff["Staff_Id"])
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
