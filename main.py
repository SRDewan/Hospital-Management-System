import subprocess as sp
import pymysql
import pymysql.cursors
import random
from datetime import datetime

inf = 1000000
def qexec(query):

    try:
        cur.execute(query)
        con.commit()

    except pymysql.Error as e:
        con.rollback()
        tmp = sp.call('clear', shell = True)
        print("Could not insert into database! Error pymysql %d: %s" %(e.args[0], e.args[1]))

def adddept(dno, staff_id):
        
    dept = {}
    heads = {}
    
    dept["Dno"] = dno
    dept["Dname"] = input("Department name: ")
    dept["Location_Floor"] = int(input("Floor number: "))
    dept["Location_Block"] = input("Block: ")
    query = """insert into Department values(%d, "%s", %d, "%s")""" % (dept["Dno"], dept["Dname"], dept["Location_Floor"], dept["Location_Block"])
    qexec(query)

    heads["Staff_Id"] = staff_id
    heads["Dno"] = dno
    query = "insert into Heads values(%d, %d)" % (heads["Dno"], heads["Staff_Id"]) 
    qexec(query)

def adddoc(staff_id):

    doctor = {}
    special = {}
    works = {}

    doctor["Staff_Id"] = staff_id
    doctor["Consultation_Fee"] = int(input("Consultation Fee: "))
    query = "insert into Doctor values(%d, %d)" % (doctor["Staff_Id"], doctor["Consultation_Fee"])
    qexec(query)

    more = "y"
    while(more == "y"):
        special["Staff_Id"] = staff_id
        special["Expertise_Area"] = input("Expertise Area: ")
        query = """insert into Specialisation values(%d, "%s")""" % (special["Staff_Id"], special["Expertise_Area"])
        qexec(query)
        more = input("Do you wish to enter more expertise areas(y / n): ")

    works["Staff_Id"] = staff_id
    row = {}
    dnew = "n"

    while(row == {} and dnew != "y"):
        works["Dno"] = int(input("Department Number: "))
        query = "select Dno from Works_In where Dno = %d" % (works["Dno"])
        qexec(query)
        row = cur.fetchall()

        if(row == {}):
            dnew = input("Department does not exist. Would you like to create a new department(y / n): ")
            if(dnew == "y"):
                adddept(works["Dno"], staff_id)

    query = "insert into Works_In values(%d, %d)" % (works["Staff_Id"], works["Dno"])
    qexec(query)

def addedu(staff_id):

    more = "y"
    education = {}
    while(more == "y"):
        education["Staff_Id"] = staff_id
        education["Degree"] = input("Degree: ")
        query = """insert into Education values(%d, "%s")""" % (education["Staff_Id"], education["Degree"])
        qexec(query)
        more = input("Do you wish to enter more degrees(y / n): ")

def addshift(staff_id):
    
    tmp = sp.call('clear', shell = True)
    more = "y"
    shift = {}
    while(more == "y"):
        shift["Staff_Id"] = staff_id
        shift["Shift_Day"] = (input("Shift Day: "))
        shift["Shift_Time"] = (input("Shift Time (HH:MM:SS): "))
        query = """insert into Shift values(%d, "%s", "%s")""" % (shift["Staff_Id"], shift["Shift_Time"], shift["Shift_Day"])
        qexec(query)
        more = input("Do you wish to enter more shifts(y / n): ")

def addstaff():

    try:
        staff = {}

        flag = 1
        query = "select Staff_Id from Staff"
        qexec(query)
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
        qexec(query)

        addshift(staff["Staff_Id"])
        addedu(staff["Staff_Id"])

        if(staff["Job"] == "Doctor"):
            adddoc(staff["Staff_Id"])

        tmp = input("Enter any key to CONTINUE:")

    except Exception as e:
        con.rollback()
        print("Error: ", e)

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    print("heya")
    if(ch == 1):
        addstaff()
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

# Global
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
