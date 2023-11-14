#!/usr/bin/python3
""" takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa with with dependency
    injection management"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db_conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        password=argv[2],
        db=argv[3]
    )
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * FROM states WHERE\
                    BINARY name = %(name)s", {'name': sys.argv[4]})
    rows_selected = db_cursor.fetchall()
    for r in rows_selected:
        print(r)
    db_cursor.close()
    db_conn.close()
