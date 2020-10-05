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

        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
