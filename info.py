import subprocess as sp
import random
from datetime import datetime
from prettytable import PrettyTable
from exec import qexec

shifts = ["Monday", "Tuesday", "Wednesday",
          "Thursday", "Friday", "Saturday", "Sunday"]

def info(opti):

    try:
        if(opti == 1):
            query = "SELECT * FROM Room WHERE Available = 1"
            if(qexec(query)):
                return -1

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            res = cur.fetchall()
            for row in res:
                x.add_row([row['Room_No'], row['Location_Block'],
                           row['Location_Floor'], row['Room_Type'], row['Available']])
            print(x)

        elif(opti == 2):

            shift = "Holiday"
            while shift not in shifts:
                shift = (input("Shift Day: "))

            query = """SELECT First_Name, Last_Name FROM Staff INNER JOIN Shift ON Staff.Staff_Id= Shift.Staff_Id WHERE Shift_Day = "%s" """ % (
                shift)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['First_Name'], row['Last_Name']])
            print(x)

        elif(opti == 3):
            spec = input("Specialisation: ")
            query = """SELECT First_Name, Last_Name FROM Staff INNER JOIN Specialisation ON Staff.Staff_Id= Specialisation.Staff_Id WHERE Expertise_Area = "%s" """ % (
                spec)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['First_Name'], row['Last_Name']])
            print(x)

        elif(opti == 4):
            comp = input("Company Name: ")
            query = """SELECT Insurance_Id FROM Insured_Details WHERE Company = "%s" """ % (
                comp)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['First_Name', 'Last_Name']
            x = PrettyTable(field_names)

            for row in res:
                num = int(row['Insurance_Id'])
                que = """SELECT First_Name, Last_Name FROM Patient INNER JOIN Insured_Patients ON Patient.Patient_Id= Insured_Patients.Patient_Id WHERE Insurance_Id = %d """ % (
                    num)

                if qexec(que):
                    return -1

                qes = cur.fetchall()

                for rum in qes:
                    x.add_row([rum['First_Name'], rum['Last_Name']])

            print(x)

        elif(opti == 5):
            patno = int(input("Patient_Id: "))
            query = "SELECT Patient_Id, First_Name, Last_Name, Contact_No FROM Patient WHERE Patient_Id = %d " % (
                patno)

            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Patient_Id'], row['First_Name'],
                           row['Last_Name'], row['Contact_No']])
            print(x)

        elif(opti == 6):
            pno = int(input("Pno: "))
            query = "SELECT * FROM Prescription WHERE Pno = %d " % (pno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Pno'], row['Complaint'], row['Diagnosis']])
            print(x)

        elif(opti == 7):
            billno = int(input("Bill_No: "))
            query = "SELECT Bill_No, Amount FROM Bill WHERE Bill_No = %d " % (
                billno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Bill_No'], row['Amount']])
            print(x)

        elif(opti == 8):
            dno = int(input("Dno: "))
            query = "SELECT * FROM Department WHERE Dno = %d " % (dno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Dno'], row['Dname'],
                           row['Location_Block'], row['Location_Floor']])
            print(x)

        elif(opti == 9):
            name = input("First_Name: ")
            query = """SELECT * FROM Patient WHERE First_Name = "%s" """ % (
                name)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Patient_Id'], row['First_Name'], row['Last_Name'], row['H_No'],
                           row['Street'], row['City'], row['Zipcode'], row['Contact_No'], row['Date_Of_Birth']])
            print(x)

        elif(opti == 10):
            name = input("First_Name: ")
            query = """SELECT * FROM Staff WHERE First_Name = "%s" """ % (name)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Staff_Id'], row['First_Name'], row['Last_Name'], row['Sex'], row['Salary'], row['Contact_No'],
                           row['Date_Of_Birth'], row['H_No'], row['Street'], row['Zipcode'], row['City'], row['Job'], row['Supervisor_Id']])
            print(x)

        elif(opti == 11):
            medname = input("Medicine Name: ")
            query = """SELECT Med_Name, Expiry_Date, Batch_Details.Batch_No, Qty FROM Batch_Details INNER JOIN Medication ON Batch_Details.Batch_No= Medication.Batch_No WHERE Med_Name = "%s" """ % (
                medname)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Med_Name'], row['Expiry_Date'],
                           row['Batch_No'], row['Qty']])
            print(x)

        elif(opti == 12):
            supname = input("Supplier Name: ")
            query = """SELECT Med_Name, Expiry_Date, Batch_No, Supplier_Details.Supplier_Id, Supplier_Name FROM Supplier_Details INNER JOIN Medication ON Supplier_Details.Supplier_Id= Medication.Supplier_Id WHERE Supplier_Name = "%s" """ % (
                supname)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Med_Name'], row['Expiry_Date'],
                           row['Batch_No'], row['Supplier_Id'], row['Supplier_Name']])
            print(x)

        elif(opti == 13):
            query = "SELECT * FROM Patient"
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Patient_Id'], row['First_Name'], row['Last_Name'], row['H_No'],
                           row['Street'], row['City'], row['Zipcode'], row['Contact_No'], row['Date_Of_Birth']])
            print(x)

        elif(opti == 14):
            query = "SELECT * FROM Staff"
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = [i[0] for i in cur.description]
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Staff_Id'], row['First_Name'], row['Last_Name'], row['Sex'], row['Salary'], row['Contact_No'],
                           row['Date_Of_Birth'], row['H_No'], row['Street'], row['Zipcode'], row['City'], row['Job'], row['Supervisor_Id']])
            print(x)

        else:
            print("Error: Invalid Option")

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
