#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """./4-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'"""

    db_conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        password=argv[2],
        db=argv[3]
    )

    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT id, cities.name, states.name FROM cities "
                        + "INNER JOIN states ON states.id = cities.state_id")

    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
