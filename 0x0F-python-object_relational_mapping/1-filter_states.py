#!/usr/bin/python3
"""lists all states with a name starting with N from the database."""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")
    results = cur.fetchall()
    for result in results:
        print(result)
