#!/usr/bin/python3
"""the name of a state as an argument and lists all cities"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name=%s\
    ORDER BY cities.id"
    num = cur.execute(sql, (sys.argv[4],))
    rows = cur.fetchall()
    result = []
    i = 0
    for row in rows:
        result.append(rows[i][0])
        i += 1
    joined = ", ".join(result)
    print(joined)
    cur.close()
    db.close()
