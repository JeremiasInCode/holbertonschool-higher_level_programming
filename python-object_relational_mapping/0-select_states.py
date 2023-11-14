#!/usr/bin/python3
"""lists all states"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    #./0-select_states.py root root hbtn_0e_0_usa
    db_conn = MySQLdb.connect(host="localhost", port=3306,
        user=argv[1], password=argv[2], database=argv[3])
    db_cursor = db_conn.cursor()
    query = "SELECT * FROM states ORDER BY id"
    db_cursor.execute(query)
    states = db_cursor.fetchall()
    for state in states:
        print(state)
    db_cursor.close()
    db_conn.close()
