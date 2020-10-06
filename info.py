import subprocess as sp
import random
from datetime import datetime

from exec import qexec

def info(opti):

    try:
        if(opti == 1):
            query = "SELECT * FROM Room WHERE Available = 1"
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Room_No:",row['Room_No']," Location_Block:",row['Location_Block']," Location_Floor:", row['Location_Floor']," Room_Type:", row['Room_Type'])

        elif(opti == 2):
            shift = input("Shift Day: ")
            query = """SELECT First_Name, Last_Name FROM Staff INNER JOIN Shift on Staff.Staff_Id= Shift.Staff_Id WHERE Shift_Day = "%s" """ % (
                shift)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("First_Name:",row['First_Name']," Last_Name:", row['Last_Name'])

        elif(opti == 3):
            spec = input("Specialisation: ")
            query = """SELECT First_Name, Last_Name FROM Staff INNER JOIN Specialisation on Staff.Staff_Id= Specialisation.Staff_Id WHERE Expertise_Area = "%s" """ % (
                spec)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("First_Name:",row['First_Name']," Last_Name:", row['Last_Name'])

        elif(opti == 4):
            comp = input("Companyname: ")
            query = """SELECT Insurance_Id FROM Insured_Details WHERE Company = "%s" """ % (comp)
            if(qexec(query)):
                return -1
            res = cur.fetchall()

            for row in res:
            	num=row['Insurance_Id']
            	que = """SELECT First_Name, Last_Name FROM Patient INNER JOIN Insured_Patients on Patient.Patient_Id= Insured_Patients.Patient_Id WHERE Insurance_Id = %d """ % (
                num)
            	if(qexec(que)):
            		return -1
            	qes =cur.fetchall()
            	for rum in qes:
            		print("First_Name:",rum['First_Name']," Last_Name:",rum['Last_Name'])

        elif(opti == 5):
            patno = int(input("Patient_Id: "))
            query = "SELECT Patient_Id, First_Name, Last_Name, Contact_No FROM Patient WHERE Patient_Id = %d " % (
                patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Patient_Id:",row['Patient_Id']," First_Name:",row['First_Name']," Last_Name:", row['Last_Name']," Contact_No:", row['Contact_No'])

        elif(opti == 6):
            pno = int(input("Pno: "))
            query = "SELECT * FROM Prescription WHERE Pno = %d " % (pno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Pno:",row['Pno']," Complaint:", row['Complaint']," Diagnosis:",row['Diagnosis'])

        elif(opti == 7):
            billno = int(input("Bill_No: "))
            query = "SELECT Bill_No, Amount FROM Bill WHERE Bill_No = %d " % (billno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Bill_No:",row['Bill_No']," Amount:", row['Amount'])

        elif(opti == 8):
            dno = int(input("Dno: "))
            query = "SELECT * FROM Department WHERE Dno = %d " % (dno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("DNo:",row['Dno']," Dname:", row['Dname']," Location_Block:",row['Location_Block']," Location_Floor:", row['Location_Floor'])

        elif(opti == 9):
            name = input("First_Name: ")
            query = """SELECT * FROM Patient WHERE First_Name = "%s" """ % (name)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Patient_Id:",row['Patient_Id']," First_Name:", row['First_Name']," Last_Name:", row['Last_Name']," H_No:", row['H_No']," Street:", row['Street']," City:", row['City']," Zipcode:", row['Zipcode']," Contact_No:", row['Contact_No']," Date_Of_Birth:", row['Date_Of_Birth'])

        elif(opti == 10):
            name = input("First_Name: ")
            query = """SELECT * FROM Staff WHERE First_Name = "%s" """ % (name)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Staff_Id:",row['Staff_Id']," First_Name:", row['First_Name']," Last_Name:", row['Last_Name']," Sex:", row['Sex']," Salary:", row['Salary']," Contact_No:", row['Contact_No']," Date_Of_Birth:", row['Date_Of_Birth']," H_No:", row['H_No']," Street:", row['Street']," Zipcode:", row['Zipcode']," City:", row['City']," Job:", row['Job']," Supervisor_Id:", row['Supervisor_Id'])

        elif(opti == 11):
            medname = input("Medicine Name: ")
            query = """SELECT Med_Name, Expiry_Date, Batch_Details.Batch_No, Qty FROM Batch_Details INNER JOIN Medication on Batch_Details.Batch_No= Medication.Batch_No WHERE Med_Name = "%s" """ % (
                medname)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Med_Name:",row['Med_Name'],"Expiry_Date:",row['Expiry_Date'],"Batch_No:",row['Batch_No']," Qty:", row['Qty'])

        elif(opti == 12):
            supname = input("Supplier Name: ")
            query = """SELECT Med_Name, Expiry_Date, Batch_No, Supplier_Details.Supplier_Id, Supplier_Name FROM Supplier_Details INNER JOIN Medication on Supplier_Details.Supplier_Id= Medication.Supplier_Id WHERE Supplier_Name = "%s" """ % (
                supname)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Med_Name:",row['Med_Name']," Expiry_Date:",row['Expiry_Date'],"Batch_No:",row['Batch_No']," Supplier_Id:", row['Supplier_Id']," Supplier_Name:", row['Supplier_Name'])

        elif(opti == 13):
            query = "SELECT * FROM Patient"
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Patient_Id:",row['Patient_Id']," First_Name:", row['First_Name']," Last_Name:", row['Last_Name']," H_No:", row['H_No']," Street:", row['Street']," City:", row['City']," Zipcode:", row['Zipcode']," Contact_No:", row['Contact_No']," Date_Of_Birth:", row['Date_Of_Birth'])

        elif(opti == 14):
            name = input("First_Name: ")
            query = "SELECT * FROM Staff " 
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Staff_Id:",row['Staff_Id']," First_Name:", row['First_Name']," Last_Name:", row['Last_Name']," Sex:", row['Sex']," Salary:", row['Salary']," Contact_No:", row['Contact_No']," Date_Of_Birth:", row['Date_Of_Birth']," H_No:", row['H_No']," Street:", row['Street']," Zipcode:", row['Zipcode']," City:", row['City']," Job:", row['Job']," Supervisor_Id:", row['Supervisor_Id'])

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
