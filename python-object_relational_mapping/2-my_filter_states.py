#!/usr/bin/python3
"script that lists all states"
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
    sn_searched = sys.argv[4]

    db_cursor.execute("SELECT id, name FROM states WHERE name LIKE '{}'\
                        ORDER BY id ASC".format(sys.argv[4]))

    q_rows = db_cursor.fetchall()
    for i in q_rows:
        print(i)

    db_cursor.close()
    db.close()
