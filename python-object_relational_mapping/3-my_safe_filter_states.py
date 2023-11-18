#!/usr/bin/python3
"script that lists all states with a name"
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)

    db_cursor = db.cursor()
    sn_searched = sys.argv[4]

    s_name = sys.argv[4]
    my_query = ("SELECT * FROM states WHERE name = %s ORDER BY id")

    db_cursor.execute(my_query, (s_name,))

    q_rows = db_cursor.fetchall()
    for i in q_rows:
        print(i)

    db_cursor.close()
    db.close()
