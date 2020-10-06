import subprocess as sp
import random
from datetime import datetime

from exec import qexec

def analy(optio):

    try:
        if(optio == 1):
            startdate = input("Input Start date (YYYY-MM-DD): ")
            enddate = input("Input End date (YYYY-MM-DD): ")
            query = """select avg(Amount), max(Amount), min(Amount) from Bill where Date >= "%s" and Date <= "%s" and Payment_Status = "Y" """ % (startdate,enddate)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Average Bill Amount:",row['avg(Amount)']," Maximum:", row['max(Amount)']," Minimum:",row['min(Amount)'])

        elif(optio == 2):
            startdate = input("Input Start date (YYYY-MM-DD): ")
            enddate = input("Input End date (YYYY-MM-DD): ")
            query = """select sum(Amount) from Bill where Date >= "%s" and Date <= "%s" and Payment_Status = "Y" """ % (startdate,enddate)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Total Income of Hospital:",row['sum(Amount)'])

        elif(optio == 3):
            query = "select max(Salary), min(Salary) from Staff "
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Maximum:", row['max(Salary)']," Minimum:",row['min(Salary)'])
                

        elif(optio == 4):
            patno = int(input("Patient_Id: "))
            query = "select sum(Amount) from Bill inner join Pays on Bill.Bill_No=Pays.Bill_No where Patient_Id = %d " % (patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Total Bill of the Patient:",row['sum(Amount)'])

        elif(optio == 5):
            query = "select avg(Hourly_Tariff), max(Hourly_Tariff), min(Hourly_Tariff) from Room_Pricing "
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
            	print("Average Hourly Tariff:",row['avg(Hourly_Tariff)']," Maximum:", row['max(Hourly_Tariff)']," Minimum:",row['min(Hourly_Tariff)'])

        elif(optio == 6):
            patno = int(input("Patient_Id: "))
            query = "select Patient_Id, Date, Time from Schedules where Patient_Id = %d and Date >= curdate()" % (patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Patient_Id:",row['Patient_Id']," Date:", row['Date']," Time:",row['Time'])

        elif(optio == 7):
            staffno = int(input("Staff_Id: "))
            query = "select Staff_Id, Date, Time from Schedules where Staff_Id = %d and Date >= curdate()" % (staffno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Staff_Id:",row['Staff_Id']," Date:", row['Date']," Time:",row['Time'])

        elif(optio == 8):
            patno = int(input("Patient_Id: "))
            query = """select Bill.Bill_No, Amount from Bill inner join Pays on Bill.Bill_No=Pays.Bill_No where Patient_Id = %d and Payment_Status = "N" """ % (patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Bill No:", row['Bill.Bill_No']," Amount:",row['Amount'])

        elif(optio == 9):
            date = input("Input Date (YYYY-MM-DD): ")
            time = input("Input Time (HH:MM:SS): ")
            patno = int(input("Patient_Id: "))
            query = """select Pno from Schedules where Date = "%s" and Time <= "%s" and Patient_Id = %d """ % (date,time,patno)
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                num=int(row['Pno'])
                q1 = "SELECT Pno, Med_Name FROM Recommends WHERE Pno = %d " % (num)
                if(qexec(q1)):
                    return -1
                q1 =cur.fetchall()
                for r1 in q1:
                    print("Pno:",r1['Pno']," Med_Name:",r1['Med_Name'])

                q2 = "SELECT Entails.Pno, Type FROM Test_or_Surgery INNER JOIN Entails on Test_or_Surgery.Time = Entails.Time AND Test_or_Surgery.Date = Entails.Date WHERE Entails.Pno = %d " % (num)
                if(qexec(q2)):
                    return -1
                q2 =cur.fetchall()
                for r2 in q2:
                    print("Pno:",r2['Pno']," Type:",r2['Type'])

        elif(optio == 10):
            query = "select Med_Name, count(Med_Name) from Recommends group by Med_Name order by count(*) desc   "
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Med_Name:", row['Med_Name']," Count:",row['count(Med_Name)'])

        elif(optio == 11):
            query = "select Staff_Id, count(Patient_Id) from Schedules group by Staff_Id order by count(*) desc   "
            if(qexec(query)):
                return -1

            res = cur.fetchall()
            for row in res:
                print("Staff_Id:", row['Staff_Id']," Count:",row['count(Patient_Id)'])
        
        else:
            print("Error: Invalid Option")

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
