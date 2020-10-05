import subprocess as sp
from datetime import datetime

from exec import qexec
inf = 1000000

def ins(inspat):

    query = "select * from Insured_Details where Insurance_Id = %d" % (inspat["Insurance_Id"])
    if(qexec(query)):
        return -1
    insdet = cur.fetchall()

    print("Current latest renewal date = ", insdet[0]["Latest_Renewal_Date"])    
    num = (input("Enter new date (YYYY-MM-DD): "))

    query = """update Insured_Details set Latest_Renewal_Date = "%s" where Insurance_Id = %d""" % (num, inspat["Insurance_Id"])
    if(qexec(query)):
        return -1

    print("Success!")
    return 0


def addr(res):

    print("Current address:- ")
    print("House number = ", res["H_No"])
    print("Street = ", res["Street"])
    print("Zipcode = ", res["Zipcode"])
    print("City = ", res["City"])
    
    print("Enter new address:- ")
    hno = int(input("House number: "))
    street = input("Street: ")
    zipc = int(input("Zipcode: "))
    city = input("City: ")

    query = """update Patient set H_No = %d, Street = "%s", Zipcode = %d, City = "%s"  where Patient_Id = %d""" % (hno, street, zipc, city, res["Patient_Id"])
    if(qexec(query)):
        return -1

    print("Success!")
    return 0


def contact(res):

    print("Current contact number = ", res["Contact_No"])    
    num = int(input("Enter new number: "))

    query = "update Patient set Contact_No = %d where Patient_Id = %d" % (num, res["Patient_Id"])
    if(qexec(query)):
        return -1

    print("Success!")
    return 0


def modpat():

    try:
        
        pid = int(input("Enter patient id whose details are to be edited: "))

        query = """select * from Patient where Patient_Id = %d""" % (pid)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid id. No such patient.")
            return -1

        print("Choose 1 field to edit: ")
        print("1. Contact")
        print("2. Address")

        query = """select * from Insured_Patients where Patient_Id = %d""" % (pid)
        if(qexec(query)): 
            return -1; 
        inspat = cur.fetchall()
        if(inspat != ()):
            print("3. Insurance latest renewal date")

        choice = int(input("Enter choice: "))
        tmp = sp.call('clear', shell=True)
        if(choice == 1):
            if(contact(res[0])):
                return -1
        elif(choice == 2):
            if(addr(res[0])):
                return -1
        elif(inspat != () and choice == 3):
            if(ins(inspat[0])):
                return -1
        else:
            print("Error: Invalid option.")

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
