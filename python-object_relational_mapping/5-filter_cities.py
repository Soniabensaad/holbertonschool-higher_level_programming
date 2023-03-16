#!/usr/bin/python3
"""the name of a state as an argument and lists all cities"""
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
    cmd = "SELECT cities.name FROM cities JOIN states ON\
             cities.state_id = states.id\
              AND states.name = %s ORDER BY cities.id ASC"
    c.execute(cmd, (db_s, ))
    ls = []
    i = 0
    rows = c.fetchall()
    for row in rows:
        ls.append(rows[i][0])
        i += 1
    city = " ,".join(ls)
    print(city)
    c.close()
    db.close()
