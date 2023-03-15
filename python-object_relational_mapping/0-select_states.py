#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb
if __name__== "__main__":
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306,
                          user=mysql_user, passwd=mysql_pwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in cur.fetchall():
        print(state)
