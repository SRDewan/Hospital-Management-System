import subprocess as sp
import pymysql
import pymysql.cursors
import random
from datetime import datetime

inf = 1000000
def qexec(query):

    try:
        cur.execute(query)
        return 0;

    except pymysql.Error as e:
        con.rollback()
        tmp = sp.call('clear', shell = True)
        print("Could not insert into database! Error pymysql %d: %s" %(e.args[0], e.args[1]))
        return -1;

def adddept(dno, staff_id):
        
    dept = {}
    heads = {}
    
    dept["Dno"] = dno
    dept["Dname"] = input("Department name: ")
    dept["Location_Floor"] = int(input("Floor number: "))
    dept["Location_Block"] = input("Block: ")
    query = """insert into Department values(%d, "%s", %d, "%s")""" % (dept["Dno"], dept["Dname"], dept["Location_Floor"], dept["Location_Block"])
    if(qexec(query)):
        return -1;

    heads["Staff_Id"] = staff_id
    heads["Dno"] = dno
    query = "insert into Heads values(%d, %d)" % (heads["Dno"], heads["Staff_Id"]) 
    if(qexec(query)):
        return -1;

    return 0

def adddoc(staff_id):

    doctor = {}
    special = {}
    works = {}

    doctor["Staff_Id"] = staff_id
    doctor["Consultation_Fee"] = int(input("Consultation Fee: "))
    query = "insert into Doctor values(%d, %d)" % (doctor["Staff_Id"], doctor["Consultation_Fee"])
    if(qexec(query)):
        return -1;

    more = "y"
    while(more == "y"):
        special["Staff_Id"] = staff_id
        special["Expertise_Area"] = input("Expertise Area: ")
        query = """insert into Specialisation values(%d, "%s")""" % (special["Staff_Id"], special["Expertise_Area"])
        if(qexec(query)):
            return -1;
        more = input("Do you wish to enter more expertise areas(y / n): ")

    works["Staff_Id"] = staff_id
    row = {}
    dnew = "n"

    while(row == {} and dnew != "y"):
        works["Dno"] = int(input("Department Number: "))
        query = "select Dno from Works_In where Dno = %d" % (works["Dno"])
        if(qexec(query)):
            return -1;
        row = cur.fetchall()

        if(row == {}):
            dnew = input("Department does not exist. Would you like to create a new department(y / n): ")
            if(dnew == "y"):
                if(adddept(works["Dno"], staff_id)):
                    return -1;

    query = "insert into Works_In values(%d, %d)" % (works["Staff_Id"], works["Dno"])
    if(qexec(query)):
        return -1;

    return 0

def addedu(staff_id):

    more = "y"
    education = {}
    while(more == "y"):
        education["Staff_Id"] = staff_id
        education["Degree"] = input("Degree: ")
        query = """insert into Education values(%d, "%s")""" % (education["Staff_Id"], education["Degree"])
        if(qexec(query)):
            return -1;
        more = input("Do you wish to enter more degrees(y / n): ")

    return 0

def addshift(staff_id):
    
    tmp = sp.call('clear', shell = True)
    more = "y"
    shift = {}
    while(more == "y"):
        shift["Staff_Id"] = staff_id
        shift["Shift_Day"] = (input("Shift Day: "))
        shift["Shift_Time"] = (input("Shift Time (HH:MM:SS): "))
        query = """insert into Shift values(%d, "%s", "%s")""" % (shift["Staff_Id"], shift["Shift_Time"], shift["Shift_Day"])
        if(qexec(query)):
            return -1;
        more = input("Do you wish to enter more shifts(y / n): ")

    return 0

def addstaff():

    try:
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
                if(oid == temp):
                    flag = 1
                    break

        print("Enter new staff member's details: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        staff["First_Name"] = name[0]
        staff["Last_Name"] = name[1]
        staff["Sex"] = input("Sex (F/M): ")
        staff["Salary"] = int(input("Salary: "))
        staff["Contact_No"] = (input("Contact Number(10 digit): "))
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
        staff["Job"] = (input("Job(Doctor / Nurse / Receptionist / Other): "))
        sid = input("*Supervisor Id: ")
        if(sid != ""):
            staff["Supervisor_Id"] = int(sid)
        else:
            staff["Supervisor_Id"] = "NULL"

        query = """insert into Staff values(%d, "%s", "%s", "%s", %d, "%s", "%s", %s, "%s", %s, "%s", "%s", %s)""" % (staff["Staff_Id"], staff["First_Name"], staff["Last_Name"], staff["Sex"], staff["Salary"], staff["Contact_No"], staff["Date_of_Birth"], staff["H_No"], staff["Street"], staff["Zipcode"], staff["City"], staff["Job"], staff["Supervisor_Id"])
        if(qexec(query)):
            return -1;

        if(addshift(staff["Staff_Id"])):
            return -1
        if(addedu(staff["Staff_Id"])):
            return -1

        if(staff["Job"] == "Doctor"):
            if(adddoc(staff["Staff_Id"])):
                return -1

        tmp = input("Enter any key to CONTINUE:")
        return 0

    except Exception as e:
        con.rollback()
        print("Error: ", e)
        return -1

def dispatch(ch):

    if(ch == 1):
        if(addstaff()):
            con.rollback
            return -1
        else:
            con.commit()
            return 0

    elif(ch == 2):
        addpat()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    else:
        print("Error: Invalid Option")

def options():

    print("1. Add staff member")  # Hire an Employee
    print("2. Add patient")  # Fire an Employee
    print("3. Option 3")  # Promote Employee
    print("4. Option 4")  # Employee Statistics
    print("5. Logout")
    ch = int(input("Enter choice: "))
    # tmp = sp.call('clear', shell = True)
    dispatch(ch)
    return ch

while(1):

    tmp = sp.call('clear', shell = True)
    
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
        con = pymysql.connect(host = host,
                              user = username,
                              password = password,
                              port = port,
                              db = 'Hospital',
                              cursorclass = pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell = True)

        if(con.open):
            print("Connected\n")
        else:
            print("Failed to connect\n")

        with con.cursor() as cur:
            ret = 0
            while(ret != 7):
                # tmp = sp.call('clear', shell=True)
                ret = options()

    except pymysql.Error as e:
        tmp = sp.call('clear', shell = True)
        print("Could not establish connection! Error pymysql %d: %s" %(e.args[0], e.args[1]))
        tmp = input("Enter any key to CONTINUE:")
