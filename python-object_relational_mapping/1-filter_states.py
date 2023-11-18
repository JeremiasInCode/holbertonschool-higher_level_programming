#!/usr/bin/python3
"script that lists all states from the database hbtn_0e_0_usa"

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", 
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    db_cursor = db.cursor()
    db_cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    q_rows = db_cursor.fetchall()

    for i in q_rows:
        print(i)

    db_cursor.close()
    db.close()
