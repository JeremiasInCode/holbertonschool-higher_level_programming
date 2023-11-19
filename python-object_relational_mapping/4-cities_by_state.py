#!/usr/bin/python3
"script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)

    db_cursor = db.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    q_rows = db_cursor.fetchall()
    for i in q_rows:
        print(i)

    db_cursor.close()
    db.close()
