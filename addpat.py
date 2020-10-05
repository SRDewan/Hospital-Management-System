import subprocess as sp
import random
from datetime import datetime

from exec import qexec
inf = 1000000

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

        print("Success! Patient id of new patient = %d", patient["Patient_Id"])
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
