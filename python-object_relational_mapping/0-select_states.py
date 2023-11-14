#!/usr/bin/python3
''' 0-select_states module '''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """./0-select_states.py root root hbtn_0e_0_usa"""

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states""")
    statesList = cursor.fetchall()
    db.close()
    for item in statesList:
        print(item)
