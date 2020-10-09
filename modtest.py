import subprocess as sp
from datetime import datetime

from exec import qexec
inf = 1000000

def modtest():

    try:
        
        td = (input("Enter Test Date (YYYY-MM-DD): "))
        tt = (input("Enter Test Time (HH:MM:SS): "))

        query = """SELECT * FROM Test_or_Surgery WHERE Date = "%s" and Time = "%s" """ % (td, tt)
        if(qexec(query)): 
            return -1; 
        res = cur.fetchall()
        if(res == ()):
            print("Invalid entry. No such test or surgery.")
            return -1

        print("Current Test/Surgery Result = ", res[0]["Result"])
        tres = (input("Enter New Test/Surgery Result: "))
        query = """UPDATE Test_or_Surgery set Result = "%s" WHERE Date = "%s" and Time = "%s" """ % (tres, td, tt)
        if(qexec(query)): 
            return -1; 

        print("Success!")
        return 0

    except Exception as e:
        print("Error: ", e)
        return -1
