#!/usr/bin/python3
"""write one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        print("Error: no user provided.")
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    db_s = sys.argv[4]
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE %s\
              ORDER BY states.id", (db_s, ))
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
