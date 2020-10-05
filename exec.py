import subprocess as sp
import pymysql
import pymysql.cursors

def qexec(query):

    try:
        cur.execute(query)
        return 0

    except pymysql.Error as e:
        con.rollback()
        tmp = sp.call('clear', shell=True)
        print("Error pymysql %d: %s" % (e.args[0], e.args[1]))
        return -1
