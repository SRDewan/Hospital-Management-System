import subprocess as sp
import random
from datetime import datetime

from exec import qexec

def info(opti):

    try:
        if(opti == 1):
            query = "select * from Room where Available =1"
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Room_No:",row['Room_No']," Location_Block:",row['Location_Block']," Location_Floor:", row['Location_Floor']," Room_Type:", row['Room_Type'])

        elif(opti == 2):
            shift = input("Shift Day: ")
            query = """select First_Name, Last_Name from Staff inner join Shift on Staff.Staff_Id= Shift.Staff_Id where Shift_Day = "%s" """ % (
                shift)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("First_Name:",row['First_Name']," Last_Name:", row['Last_Name'])

        elif(opti == 3):
            spec = input("Specialisation: ")
            query = """select First_Name, Last_Name from Staff inner join Specialisation on Staff.Staff_Id= Specialisation.Staff_Id where Expertise_Area = "%s" """ % (
                spec)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("First_Name:",row['First_Name']," Last_Name:", row['Last_Name'])

        elif(opti == 4):
            comp = input("Companyname: ")
            query = """select Insurance_Id from Insured_Details where Company = "%s" """ % (comp)
            if(qexec(query)):
                return -1
            res = cur.fetchall()

            for row in res:
            	num=row['Insurance_Id']
            	que = """select First_Name, Last_Name from Patient inner join Insured_Patients on Patient.Patient_Id= Insured_Patients.Patient_Id where Insurance_Id = %d """ % (
                num)
            	if(qexec(que)):
            		return -1
            	qes =cur.fetchall()
            	for rum in qes:
            		print("First_Name:",rum['First_Name']," Last_Name:",rum['Last_Name'])

        elif(opti == 5):
            patno = int(input("Patient_Id: "))
            query = "select Patient_Id, First_Name, Last_Name, Contact_No from Patient where Patient_Id = %d " % (
                patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Patient_Id:",row['Patient_Id']," First_Name:",row['First_Name']," Last_Name:", row['Last_Name']," Contact_No:", row['Contact_No'])

        elif(opti == 6):
            pno = int(input("Pno: "))
            query = "select * from Prescription where Pno = %d " % (pno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Pno:",row['Pno']," Complaint:", row['Complaint']," Diagnosis:",row['Diagnosis'])

        elif(opti == 7):
            billno = int(input("Bill_No: "))
            query = "select Bill_No, Amount from Bill where Bill_No = %d " % (billno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Bill_No:",row['Bill_No']," Amount:", row['Amount'])

        elif(opti == 8):
            dno = int(input("Dno: "))
            query = "select * from Department where Dno = %d " % (dno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("DNo:",row['Dno']," Dname:", row['Dname']," Location_Block:",row['Location_Block']," Location_Floor:", row['Location_Floor'])

        elif(opti == 9):
            medname = input("Medicine Name: ")
            query = """select Batch_No, Qty from Batch_Details inner join Medication on Batch_Details.Batch_No= Medication.Batch_No where Med_Name = "%s" """ % (
                medname)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Batch_No:",row['Batch_No']," Qty:", row['Qty'])

        else:
            print("Error: Invalid Option")

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
