#!/usr/bin/python3
"This script lists all states starting with an 'N' from the db 'hbtn_0e_usa'"
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute('''SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name = '{}'
                ORDER BY cities.id'''.format(sys.argv[4]))
    fetchs = cur.fetchall()
    if fetchs is not None:
        print(", ".join([x[0] for x in fetchs]))
    db.close()
