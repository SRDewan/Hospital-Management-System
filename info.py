import subprocess as sp
import random
from datetime import datetime

from exec import qexec

def info(opti):

    try:
        if(opti == 1):
            query = "select * from Room where available =1"
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("Room_No   Location_Block   Location_Floor   Room_Type");
            for row in res:
                print(
                    row['Room_No'],
                    row['Location_Block'],
                    row['Location_Floor'],
                    row['Room_Type'])

        elif(opti == 2):
            shift = input("Shift Day: ")
            query = """select First_Name, Last_Name from Staff inner join Shift on Staff.Staff_Id= Shift.Staff_Id where Shift_Day = "%s" """ % (
                shift)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("First_Name   Last_Name");
            for row in res:
                print(row['First_Name'], row['Last_Name'])

        elif(opti == 3):
            spec = input("Specialisation: ")
            query = """select First_Name, Last_Name from Staff inner join Specialisation on Staff.Staff_Id= Specialisation.Staff_Id where Expertise_Area = "%s" """ % (
                spec)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("First_Name   Last_Name");
            for row in res:
                print(row['First_Name'], row['Last_Name'])

        elif(opti == 4):
            comp = input("Companyname: ")
            query = """select First_Name, Last_Name from Patient inner join Insured_Details on Patient.Insurance_Id= Insured_Details.Insurance_Id where Company = "%s" """ % (
                comp)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("First_Name   Last_Name");
            for row in res:
                print(row['First_Name'], row['Last_Name'])

        elif(opti == 5):
            patno = int(input("Patient_Id: "))
            query = "select Patient_Id, First_Name, Last_Name, Contact_No from Patient where Patient_Id = %d " % (
                patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("Patient_Id   First_Name   Last_Name   Contact_No");
            for row in res:
                print(row['Patient_Id'], row['First_Name'], row['Last_Name'], row['Contact_No'])

        elif(opti == 6):
            pno = int(input("Pno: "))
            query = "select * from Prescription where Pno = %d " % (pno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("Pno   Complaint   Diagnosis");
            for row in res:
                print(row['Pno'], row['Complaint'], row['Diagnosis'])

        elif(opti == 7):
            billno = int(input("Bill_No: "))
            query = "select Amount from Bill where Bill_No = %d " % (billno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("Amount");
            for row in res:
                print(row['Amount'])

        elif(opti == 8):
            dno = int(input("Dno: "))
            query = "select * from Department where Dno = %d " % (dno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("DNo   Dname   Location_Block   Location_Floor");
            for row in res:
                print(
                    row['DNo'],
                    row['Dname'],
                    row['Location_Block'],
                    row['Location_Floor'])

        elif(opti == 9):
            medname = input("Medicine Name: ")
            query = """select Batch_No, Qty from Batch_Details inner join Medication on Batch_Details.Batch_No= Medication.Batch_No where Med_Name = "%s" """ % (
                medname)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            print("Batch_No   Qty");
            for row in res:
                print(row['Batch_No'], row['Qty'])

        else:
            print("Error: Invalid Option")

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
