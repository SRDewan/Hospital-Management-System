import subprocess as sp
from datetime import datetime

from exec import qexec
inf = 1000000

def fee(res):

    query = "select * from Doctor where Staff_Id = %d" % (res["Staff_Id"])
    if(qexec(query)):
        return -1
    doc = cur.fetchall()

    print("Current consultation fee = ", doc[0]["Consultation_Fee"])    
    num = int(input("Enter new fee: "))

    query = "update Doctor set Consultation_Fee = %d where Staff_Id = %d" % (num, res["Staff_Id"])
    if(qexec(query)):
        return -1

    print("Success!")
    return 0


def supid(res):

    print("Current supervisor id = ", res["Supervisor_Id"])    
    num = int(input("Enter new supervisor id: "))

    query = "update Staff set Supervisor_Id = %d where Staff_Id = %d" % (num, res["Staff_Id"])
    if(qexec(query)):
        return -1

    print("Success!")
    return 0


def sal(res):

    print("Current salary = ", res["Salary"])    
    num = int(input("Enter new salary: "))

    query = "update Staff set Salary = %d where Staff_Id = %d" % (num, res["Staff_Id"])
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

    query = """update Staff set H_No = %d, Street = "%s", Zipcode = %d, City = "%s"  where Staff_Id = %d""" % (hno, street, zipc, city, res["Staff_Id"])
    if(qexec(query)):
        return -1

    print("Success!")
    return 0


def contact(res):

    print("Current contact number = ", res["Contact_No"])    
    num = int(input("Enter new number: "))

    query = "update Staff set Contact_No = %d where Staff_Id = %d" % (num, res["Staff_Id"])
    if(qexec(query)):
        return -1

    print("Success!")
    return 0


def modstaff():

    try:
        
        sid = int(input("Enter staff id whose details are to be edited: "))

        query = """select * from Staff where Staff_Id = %d""" % (sid)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid id. No such member.")
            return -1

        print("Choose 1 field to edit: ")
        print("1. Contact")
        print("2. Address")
        print("3. Salary")
        print("4. Supervisor Id")

        if(res[0]["Job"] == "Doctor"):
            print("5. Consultation Fee")

        choice = int(input("Enter choice: "))
        tmp = sp.call('clear', shell=True)
        if(choice == 1):
            if(contact(res[0])):
                return -1
        elif(choice == 2):
            if(addr(res[0])):
                return -1
        elif(choice == 3):
            if(sal(res[0])):
                return -1
        elif(choice == 4):
            if(supid(res[0])):
                return -1
        elif(res[0]["Job"] == "Doctor" and choice == 5):
            if(fee(res[0])):
                return -1
        else:
            print("Error: Invalid option.")

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
