#!/usr/bin/python3
"This script lists all states starting with an 'N' from the db 'hbtn_0e_usa'"
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()


    cur.execute('''SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON state_id = states.id
                ORDER BY cities.id''')
    fetchs = cur.fetchall()
    for x in fetchs:
        print(x)
    db.close()
