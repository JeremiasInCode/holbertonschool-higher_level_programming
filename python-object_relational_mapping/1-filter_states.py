#!/usr/bin/python3
"""lists all states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """./1-filter_states.py"""

    db_conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        password=argv[2],
        database=argv[3]
    )

    db_cursor = db_conn.cursor()
    db_cursor.execute(
        "SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' \
        ORDER BY states.id ASC"
    )
    rows_selected = db_cursor.fetchall()

    db_conn.close()

    for item in rows_selected:
        print(item)
