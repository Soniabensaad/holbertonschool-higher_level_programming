#!/usr/bin/python3
"""takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument."""
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
    c.execute("SELECT * FROM states WHERE BINARY name = '{}'\
              ORDER BY states.id".format(db_s))
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
