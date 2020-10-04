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
        print("Error pymysql %d: %s" %(e.args[0], e.args[1]))
        return -1;

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

        if(delins(pid)):
            return -1

        query = """delete from Patient where Patient_Id = %d""" % (pid)
        if(qexec(query)):
            return -1;
        return 0

    except Exception as e:
        con.rollback()
        print("Error: ", e)
        return -1

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
        con.rollback()
        print("Error: ", e)
        return -1

def addins(patid):

    tmp = sp.call('clear', shell = True)
    inspat = {}
    insdet = {}
    
    inspat["Patient_Id"] = patid
    inspat["Insurance_Id"] = int(input("Insurance Id: "))

    insdet["Insurance_Id"] = inspat["Insurance_Id"]
    insdet["Company"] = (input("Company: "))
    insdet["Latest_Renewal_Date"] = input("Latest Renewal Date (YYYY-MM-DD): ")
    query = """insert into Insured_Details values(%d, "%s", "%s")""" % (insdet["Insurance_Id"], insdet["Company"], insdet["Latest_Renewal_Date"])
    if(qexec(query)):
        return -1;

    query = """insert into Insured_Patients values(%d, %d)""" % (inspat["Patient_Id"], inspat["Insurance_Id"])
    if(qexec(query)):
        return -1;

    return 0

def addpat():

    try:
        tmp = sp.call('clear', shell = True)
        patient = {}

        flag = 1
        query = "select Patient_Id from Patient"
        if(qexec(query)):
            return -1;
        ids = cur.fetchall()

        while(flag):
            temp = random.randint(0, inf)
            patient["Patient_Id"] = temp
            flag = 0
            for oid in ids:
                if(oid["Patient_Id"] == temp):
                    flag = 1
                    break

        print("Enter new patient's details: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        patient["First_Name"] = name[0]
        patient["Last_Name"] = name[1]
        patient["Contact_No"] = int(input("Contact Number(10 digit): "))
        patient["Date_of_Birth"] = (input("Birth Date (YYYY-MM-DD): "))

        hno = (input("*House Number: "))
        if(hno == ""):
            patient["H_No"] = "NULL"
        else:
            patient["H_No"] = int(hno)
        
        patient["Street"] = (input("*Street: "))
        zip = (input("*Zipcode: "))
        if(zip == ""):
            patient["Zipcode"] = "NULL"
        else:
            patient["Zipcode"] = int(zip)
        
        patient["City"] = (input("*City: "))

        query = """insert into Patient values(%d, "%s", "%s", %s, "%s", "%s", %s, %d, "%s")""" % (patient["Patient_Id"], patient["First_Name"], patient["Last_Name"], patient["H_No"], patient["Street"], patient["City"], patient["Zipcode"], patient["Contact_No"], patient["Date_of_Birth"])
        if(qexec(query)):
            return -1

        insure = input("Is the patient insured(y / n): ")
        if(insure == "y"):
            if(addins(patient["Patient_Id"])):
                return -1

        tmp = input("Enter any key to CONTINUE:")
        return 0

    except Exception as e:
        con.rollback()
        print("Error: ", e)
        return -1

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

    more = "y"
    while(more == "y"):
        special["Staff_Id"] = staff_id
        special["Expertise_Area"] = input("Expertise Area: ")
        query = """insert into Specialisation values(%d, "%s")""" % (special["Staff_Id"], special["Expertise_Area"])
        if(qexec(query)):
            continue
        more = input("Do you wish to enter more expertise areas(y / n): ")

    works["Staff_Id"] = staff_id
    row = ()
    dnew = "n"

    while(row == () and dnew != "y"):
        works["Dno"] = int(input("Department Number: "))
        query = "select Dno from Works_In where Dno = %d" % (works["Dno"])
        if(qexec(query)):
            return -1;
        row = cur.fetchall()

        if(row == ()):
            dnew = input("Department does not exist. Would you like to create a new department(y / n): ")
            if(dnew == "y"):
                if(adddept(works["Dno"], staff_id)):
                    return -1;

    query = "insert into Works_In values(%d, %d)" % (works["Staff_Id"], works["Dno"])
    if(qexec(query)):
        return -1;

    heads["Staff_Id"] = staff_id
    heads["Dno"] = works["Dno"]
    query = "insert into Heads values(%d, %d)" % (heads["Dno"], heads["Staff_Id"]) 
    if(qexec(query)):
        return -1;

    return 0

def addedu(staff_id):

    tmp = sp.call('clear', shell = True)
    more = "y"
    education = {}
    while(more == "y"):
        education["Staff_Id"] = staff_id
        education["Degree"] = input("Degree: ")
        query = """insert into Education values(%d, "%s")""" % (education["Staff_Id"], education["Degree"])
        if(qexec(query)):
            continue 
        more = input("Do you wish to enter more degrees(y / n): ")

    return 0

def addshift(staff_id):
    
    tmp = sp.call('clear', shell = True)
    more = "y"
    shift = {}
    while(more == "y"):
        shift["Staff_Id"] = staff_id
        shift["Shift_Day"] = (input("Shift Day: "))
        shift["Shift_Start_Time"] = (input("Shift Start Time (HH:MM:SS): "))
        shift["Shift_End_Time"] = (input("Shift End Time (HH:MM:SS): "))
        query = """insert into Shift values(%d, "%s", "%s", "%s")""" % (shift["Staff_Id"], shift["Shift_Start_Time"], shift["Shift_End_Time"], shift["Shift_Day"])
        if(qexec(query)):
            continue
        more = input("Do you wish to enter more shifts(y / n): ")

    return 0

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
        staff["Sex"] = input("Sex (F/M): ")
        staff["Salary"] = int(input("Salary: "))
        staff["Contact_No"] = int(input("Contact Number(10 digit): "))
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

        return 0

    except Exception as e:
        con.rollback()
        print("Error: ", e)
        return -1

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
        tmp = sp.call('clear', shell = True)
        add(opt)

    # elif(ch == 2):

    elif(ch == 3):
        print("1. Remove staff member")
        print("2. Remove patient")
        opt = int(input("Enter choice: "))
        tmp = sp.call('clear', shell = True)
        remove(opt)

    # elif(ch == 4):

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
    tmp = sp.call('clear', shell = True)
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
            while(ret != 6):
                tmp = sp.call('clear', shell=True)
                ret = options()

    except pymysql.Error as e:
        tmp = sp.call('clear', shell = True)
        print("Could not establish connection! Error pymysql %d: %s" %(e.args[0], e.args[1]))
        tmp = input("Enter any key to CONTINUE:")
