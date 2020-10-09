import subprocess as sp
import random
from datetime import datetime
from prettytable import PrettyTable
from exec import qexec

def analy(optio):

    try:
        if(optio == 1):
            startdate = input("Input Start date (YYYY-MM-DD): ")
            enddate = input("Input End date (YYYY-MM-DD): ")
            query = """SELECT avg(Amount), max(Amount), min(Amount) FROM Bill WHERE Date >= "%s" and Date <= "%s" and Payment_Status = "Y" """ % (startdate,enddate)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Average Bill Amount', 'Maximum', 'Minimum']
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['avg(Amount)'], row['max(Amount)'], row['min(Amount)']])
            print(x)

        elif(optio == 2):
            startdate = input("Input Start date (YYYY-MM-DD): ")
            enddate = input("Input End date (YYYY-MM-DD): ")
            query = """SELECT sum(Amount) FROM Bill WHERE Date >= "%s" and Date <= "%s" and Payment_Status = "Y" """ % (startdate,enddate)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Total Income of Hospital']
            x = PrettyTable(field_names)

            for row in res:
            	x.add_row([row['sum(Amount)']])
            print(x)

        elif(optio == 3):
            query = "SELECT avg(Salary), max(Salary), min(Salary) FROM Staff"
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Average Salary', 'Maximum', 'Minimum']
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['avg(Salary)'], row['max(Salary)'], row['min(Salary)']])
            print(x)

        elif(optio == 4):
            patno = int(input("Patient_Id: "))
            query = "SELECT sum(Amount) FROM Bill inner join Pays ON Bill.Bill_No=Pays.Bill_No WHERE Patient_Id = %d " % (patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Total Bill of the patient']
            x = PrettyTable(field_names)

            for row in res:
            	x.add_row([row['sum(Amount)']])
            print(x)

        elif(optio == 5):
            query = "SELECT avg(Hourly_Tariff), max(Hourly_Tariff), min(Hourly_Tariff) FROM Room_Pricing "
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Average Hourly Tariff', 'Maximum', 'Minimum']
            x = PrettyTable(field_names)

            for row in res:
            	x.add_row([row['avg(Hourly_Tariff)'], row['max(Hourly_Tariff)'], row['min(Hourly_Tariff)']])
            print(x)

        elif(optio == 6):
            patno = int(input("Patient_Id: "))
            query = "SELECT Patient_Id, Date, Time FROM Schedules WHERE Patient_Id = %d and Date >= curdate()" % (patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Patient_Id', 'Date', 'Time']
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Patient_Id'], row['Date'], row['Time']])
            print(x)

        elif(optio == 7):
            staffno = int(input("Staff_Id: "))
            query = "SELECT Staff_Id, Date, Time FROM Schedules WHERE Staff_Id = %d and Date >= curdate()" % (staffno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Staff_Id', 'Date', 'Time']
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Staff_Id'], row['Date'], row['Time']])
            print(x)

        elif(optio == 8):
            patno = int(input("Patient_Id: "))
            query = """SELECT Bill.Bill_No, Amount FROM Bill inner join Pays ON Bill.Bill_No=Pays.Bill_No WHERE Patient_Id = %d and Payment_Status = "N" """ % (patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Bill Number', 'Amount']
            x = PrettyTable(field_names)
            
            for row in res:
                x.add_row([row['Bill_No'], row['Amount']])
            print(x)

        elif(optio == 9):
            date = input("Input Date (YYYY-MM-DD): ")
            time = input("Input Time (HH:MM:SS): ")
            patno = int(input("Patient_Id: "))
            query = """SELECT Pno FROM Schedules WHERE Date = "%s" and Time <= "%s" and Patient_Id = %d """ % (date,time,patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names1 = ['Prescription No', 'Medication Name']
            x = PrettyTable(field_names1)

            field_names2 = ['Prescription No', 'Test Type']
            y = PrettyTable(field_names2)

            for row in res:
                num=int(row['Pno'])

                q1 = "SELECT Pno, Med_Name FROM Recommends WHERE Pno = %d " % (num)
                if(qexec(q1)):
                    return -1

                q1 =cur.fetchall()

                for r1 in q1:
                    x.add_row([r1['Pno'], r1['Med_Name']])

                q2 = "SELECT Entails.Pno, Type FROM Test_or_Surgery INNER JOIN Entails ON Test_or_Surgery.Time = Entails.Time AND Test_or_Surgery.Date = Entails.Date WHERE Entails.Pno = %d " % (num)
                if(qexec(q2)):
                    return -1

                q2 =cur.fetchall()

                for r2 in q2:
                    x.add_row([r2['Pno'], r2['Type']])
            
            print(x)
            print(y)

        elif(optio == 10):
            query = "SELECT Med_Name, count(Med_Name) FROM Recommends GROUP BY Med_Name ORDER BY count(*) DESC"
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Med_Name', 'No. of times recommended']
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Med_Name'], row['count(Med_Name)']])
            print(x)

        elif(optio == 11):
            query = "SELECT Staff_Id, count(Patient_Id) FROM Schedules GROUP BY Staff_Id ORDER BY count(*) DESC"
            if(qexec(query)):
                return -1

            res = cur.fetchall()

            field_names = ['Staff_Id', 'No. of patients treated']
            x = PrettyTable(field_names)

            for row in res:
                x.add_row([row['Staff_Id'], row['count(Patient_Id)']])
            print(x)

        else:
            print("Error: Invalid Option")

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
