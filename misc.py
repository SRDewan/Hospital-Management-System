import subprocess as sp
import random
from datetime import datetime

from exec import qexec
inf = 1000000

medprice = 0
testprice = 0
billno = 0
dosage = 0

def addSupplierDetails(supplier_id):
    row = {}

    row["Supplier_Id"] = supplier_id;
    row["Supplier_Name"] = input("Supplier_Name: ")

    query = "INSERT INTO Supplier_Details VALUES ('%s', '%s')" % (row["Supplier_Id"], row["Supplier_Name"])

    if qexec(query):
        return -1

    return 0

def addBatchDetails(batch_no):
    row = {}

    row["Batch_No"] = batch_no;
    row["Qty"] = int(input("Quantity: "))

    query = "INSERT INTO Batch_Details VALUES ('%d', '%d')" % (row["Batch_No"], row["Qty"])

    if qexec(query):
        return -1

    return 0

def addMedDetails(med_name):
    row = {}

    row["Med_Name"] = med_name;
    row["Manufacturer"] = input("Manufacturer: ")
    row["Price"] = int(input("Price: "))

    query = "INSERT INTO Med_Details VALUES ('%s', '%s', '%d')" % (row["Med_Name"], row["Manufacturer"], row["Price"])

    if qexec(query):
        return -1

    return 0

def addMedication():
    tmp = sp.call('clear', shell=True)
    row = {}
    
    print("Enter Medication details: ")
    
    row["Med_Name"] = input("Medicine name: ")
    row["Batch_No"] = int(input("Batch No: "))
    row["Expiry_Date"] = input("Expiry Date (YYYY-MM-DD): ")
    row["Supplier_Id"] = int(input("Supplier Id: "))

    query = "INSERT INTO Medication VALUES ('%s', '%d', '%s', '%d')" % (row["Med_Name"], row["Batch_No"], row["Expiry_Date"], row["Supplier_Id"])

    if addSupplierDetails(row["Supplier_Id"]):
        return -1

    if qexec(query):
        return -1
    
    if addMedDetails(row["Med_Name"]):
        return -1

    if addBatchDetails(row["Batch_No"]):
        return -1

    print("The medication was added successfully!")

    return 0

def addTestPricing():
    row = {}

    row["Type"] = input("Test: ")
    row["Cost"] = int(input("Cost: "))

    query = "INSERT INTO Test_Pricing VALUES ('%s', '%d')" % (row["Type"], row["Cost"])

    if qexec(query):
        return -1

    print("The Test/Surgery was added successfully!")

    return 0

def performs(tdate, ttime):
    row = {}

    row["Date"] = tdate
    row["Time"] = ttime
    row["Staff_Id"] = int(input("Staff Id (of staff performing the test): "))
    row["Room_No"] = int(input("Test Room No: "))

    query = "INSERT INTO Performs VALUES ('%s', '%s', '%d', '%d')" % (row["Date"], row["Time"], row["Staff_Id"], row["Room_No"])

    if qexec(query):
        return -1

    return 0

def addTestorSurgery(edate, etime):
    row = {}

    row["Date"] = edate
    row["Time"] = etime
    row["Duration"] = input("Test Duration (in minutes): ")
    row["Type"] = input("Test Type: ")
    row["Result"] = input("Test Result: ")

    query = "SELECT Cost FROM Test_Pricing WHERE Type= '%s'" % (row["Type"])

    if qexec(query):
        return -1

    ids = cur.fetchall()

    global testprice
    for test in ids:
        testprice = test["Cost"]

    query = "INSERT INTO Test_or_Surgery VALUES ('%s', '%s', '%s', '%s', '%s')" % (row["Date"], row["Time"], row["Duration"], row["Type"], row["Result"])

    if qexec(query):
        return -1

    if performs(row["Date"], row["Time"]):
        return -1

    return 0

def schedules(appdate, apptime):
    row = {}

    flag = 1
    query = "SELECT Pno FROM Schedules"
    if(qexec(query)):
        return -1;
    ids = cur.fetchall()

    while(flag):
        temp = random.randint(0, inf)
        row["Pno"] = temp
        flag = 0
        for oid in ids:
            if(oid == temp):
                flag = 1
                break

    row["Staff_Id"] = int(input("Staff Id: "))
    row["Patient_Id"] = int(input("Patient Id: "))
    row["Time"] = apptime
    row["Date"] = appdate
    row["Duration"] = input("Duration (in minutes): ")

    query = "INSERT INTO Schedules VALUES ('%d', '%s', '%s', '%d', '%d', '%s')" % (row["Staff_Id"], row["Time"], row["Date"], row["Pno"], row["Patient_Id"], row["Duration"])

    if qexec(query):
        return -1

    return row["Pno"]

def addAppointment():
    tmp = sp.call('clear', shell=True)
    row = {}
    
    print("Enter new appointment details: ")
    
    row["Date"] = input("Date (YYYY-MM-DD): ")
    row["Time"] = input("Time (HH:MM:SS): ")

    query = "INSERT INTO Appointment VALUES ('%s', '%s')" % (row["Time"], row["Date"])

    if qexec(query):
        return -1

    pno = schedules(row["Date"], row["Time"])

    print("The appointment was created successfully!")
    print("The prescription number (Pno) is: {}".format(pno))

    return 0

def recommends(pno):
    row = {}
    
    row["Pno"] = pno

    medornot = "K"
    while medornot != "Y" and medornot != "N":
        medornot = input("Has any medication been prescribed? (Y/N): ")

        if medornot == "Y":
            row["Med_Name"] = input("Medicine Name: ")
            row["Batch_No"] = int(input("Batch No: "))
            row["Dosage"] = int(input("Dosage: "))

            query = "SELECT Price FROM Med_Details WHERE Med_Name = '%s'" % (row["Med_Name"])

            if qexec(query):
                return -1

            ids = cur.fetchall()

            global medprice
            for med in ids:
                medprice = med["Price"]

            global dosage
            dosage = row["Dosage"]
            query = """UPDATE Batch_Details SET Qty = Qty - %d WHERE Batch_No = %d""" % (dosage, row["Batch_No"])
            if(qexec(query)):
                return -1

        else:
            row["Med_Name"] = "NULL"
            row["Batch_No"] = "NULL"
            row["Dosage"] = "NULL"

    global billno 
    billno = createBill()
    row["Bill_No"] = billno

    if medornot == "Y":
        query = "INSERT INTO Recommends VALUES ('%d', '%s', '%d', '%d', '%d')" % (row["Pno"], row["Med_Name"], row["Batch_No"], row["Bill_No"], row["Dosage"])

    else:
        query = "INSERT INTO Recommends VALUES ('%d', %s, %s, '%d', %s)" % (row["Pno"], row["Med_Name"], row["Batch_No"], row["Bill_No"], row["Dosage"])

    if qexec(query):
        return -1
    
    return 0

def addPrescription():
    tmp = sp.call('clear', shell=True)
    row = {}
    ids = {}
    pno = 0

    while(ids == {}):
        pno = int(input("Pno: "))
        query = "SELECT Pno from Schedules WHERE Pno = %d" % (pno)
        
        if qexec(query):
            return -1

        ids = cur.fetchall()

    row["Pno"] = pno

    # print("Enter Prescription details: ")

    row["Complaint"] = input("Complaint: ") 
    row["Diagnosis"] = input("Diagnosis: ")

    query = "INSERT INTO Prescription VALUES ('%d', '%s', '%s')" % (row["Pno"], row["Complaint"], row["Diagnosis"])

    if qexec(query):
        return -1

    if recommends(pno):
        return -1    

    if entails(pno):
        return -1

    print("The prescription was created successfully!")
    return 0

def entails(pno):
    row = {}

    row["Pno"] = pno
    row["Bill_No"] = billno

    testornot = "K"
    while testornot != "Y" and testornot != "N":
        testornot = input("Has any test/surgery been prescribed? (Y/N): ")

    if testornot == "Y":
        row["Date"] = input("Test Date (YYYY-MM-DD): ")
        row["Time"] = input("Test Time (HH:MM:SS): ")

    else:
        row["Date"] = "NULL"
        row["Time"] = "NULL"

    if testornot == "Y":
        if addTestorSurgery(row["Date"], row["Time"]):
            return -1

        query = "INSERT INTO Entails VALUES ('%d', '%s', '%s', '%d')" % (row["Pno"], row["Date"], row["Time"], row["Bill_No"])

    else:
        query = "INSERT INTO Entails VALUES ('%d', %s, %s, '%d')" % (row["Pno"], row["Date"], row["Time"], row["Bill_No"])

    if qexec(query):
        return -1

    query = "SELECT * FROM Schedules WHERE Pno = %d" % (pno)
    if qexec(query):
        return -1
    x = cur.fetchall()
    query = "SELECT * FROM Doctor WHERE Staff_Id = %d" % (x[0]["Staff_Id"])
    if qexec(query):
        return -1
    y = cur.fetchall()

    query = "UPDATE Bill SET Amount = Amount + %d WHERE Bill_No = %d" % (y[0]["Consultation_Fee"], billno)
    if qexec(query):
        return -1

    return 0

def createBill():
    row = {}

    flag = 1
    query = "SELECT Bill_No FROM Bill"
    if qexec(query):
        return -1
    ids = cur.fetchall()

    while(flag):
        temp = random.randint(0, inf)
        row["Bill_No"] = temp
        flag = 0
        for oid in ids:
            if(oid == temp):
                flag = 1
                break

    row["Date"] = datetime.today().strftime("%Y-%m-%d")
    row["Time"] = datetime.now().strftime("%H:%M:%S")
    
    row["Payment_Status"] = "K"
    while row["Payment_Status"] != "Y" and row["Payment_Status"] != "N":
        row["Payment_Status"] = input("Payment Status (Y/N): ")
    
    row["Amount"] = (medprice*dosage) + testprice

    query = "INSERT INTO Bill VALUES ('%d', '%d', '%s', '%s', '%s')" % (row["Bill_No"], row["Amount"], row["Date"], row["Time"], row["Payment_Status"])

    if qexec(query):
        return -1
    
    return row["Bill_No"]

def updateTestPricing():
    tmp = sp.call('clear', shell=True)
    ttype = input("Enter test type you would like to update: ")
    query = "SELECT Cost FROM Test_Pricing WHERE Type = '%s'" % (ttype)

    if qexec(query):
        return -1
    
    ids = cur.fetchall()

    if ids == ():
        print("No such test type found")
        return -1

    for row in ids:
        print("The current cost for this test type is: {}".format(row["Cost"]))

    tcost = int(input("Enter the new cost: "))
    query = "UPDATE Test_Pricing SET Cost = '%d' WHERE Type = '%s'" % (tcost, ttype)

    if qexec(query):
        return -1

    print("The test price was updated successfully!")

    return 0

def updateMedicationPricing():
    tmp = sp.call('clear', shell=True)
    mname = input("Enter Medicine Name you would like to update: ")
    query = "SELECT Price FROM Med_Details WHERE Med_Name = '%s'" % (mname)

    if qexec(query):
        return -1
    
    ids = cur.fetchall()

    if ids == ():
        print("No such medication found")
        return -1

    for row in ids:
        print("The current price for this medicine is: {}".format(row["Price"]))

    mprice = int(input("Enter the new price: "))
    query = "UPDATE Med_Details SET Price = '%d' WHERE Med_Name = '%s'" % (mprice, mname)

    if qexec(query):
        return -1

    print("The medication price was updated successfully!")

    return 0

def updateAppointment():
    tmp = sp.call('clear', shell=True)
    adate = input("Enter date of the appointment: ")
    atime = input("Enter time of the appointment: ")

    query = "SELECT Date, Time FROM Appointment WHERE Date = '%s' AND Time = '%s'" % (adate, atime)

    if qexec(query):
        return -1
    
    ids = cur.fetchall()

    if ids == ():
        print("No appointment found on this date and time")
        return -1

    for row in ids:
        print("The patient has an appointment scheduled on {} at time {}".format(row["Date"], row["Time"]))

    newdate = input("Enter the new date of the appointment: ")
    newtime = input("Enter the new time of the appointment: ")

    query = "UPDATE Appointment SET Time = '%s', Date = '%s' WHERE Date = '%s' AND Time = '%s'" % (newtime, newdate, adate, atime)

    if qexec(query):
        return -1

    print("The appointment was updated successfully!")

    return 0

def updatePaymentStatus():
    tmp = sp.call('clear', shell=True)
    billnum = int(input("Enter Bill Number: "))

    query = "SELECT Payment_Status FROM Bill WHERE Bill_No = '%d'" % (billnum)

    if qexec(query):
        return -1
    
    ids = cur.fetchall()

    if ids == ():
        print("No such Bill Number found")
        return -1

    for row in ids:
        print("The current status of this bill is: {}".format(row["Payment_Status"]))

    status = "K"
    while status != "Y" and status != "N":
        status = input("Enter the new payment status for this bill (Y/N): ")
    
    query = "UPDATE Bill SET Payment_Status = '%s' WHERE Bill_No = '%d'" % (status, billnum)

    if qexec(query):
        return -1

    print("The payment status was updated successfully!")

    return 0
