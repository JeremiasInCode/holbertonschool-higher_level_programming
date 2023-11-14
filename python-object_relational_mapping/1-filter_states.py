#!/usr/bin/python3
"""
    lists all states
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db_conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        password=argv[2],
        database=argv[3]
    )
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT state.id, state.name FROM states")
    rows_selected = db_cursor.fetchall()
    for item in rows_selected:
        if item[1].startswith('N'):
            print(item)
    db_cursor.close()
    db_conn.close()
