#!/usr/bin/python2
import sys
import MySQLdb
if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    db =  MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY 'N%' ORDER BY states.id ASC")
    for state in cur.fetchall():
        print(state)
