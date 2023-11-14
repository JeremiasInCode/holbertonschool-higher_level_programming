#!/usr/bin/python3
""" takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'"""

    db_conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        password=argv[2],
        db=argv[3]
    )

    db_cursor = db_conn.cursor()
    db_cursor.execute(
        "SELECT * FROM states\
         WHERE name LIKE BINARY '{}'\
         ORDER BY states.id ASC".format(argv[4])
    )
    rows_selected = db_cursor.fetchall()

    db_conn.close()

    for r in rows_selected:
        print(r)