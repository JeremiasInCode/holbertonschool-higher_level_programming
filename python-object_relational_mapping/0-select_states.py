#!/usr/bin/python3
''' 0-select_states module '''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

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
    for item in statesList:
        print(item)
    db.close()
