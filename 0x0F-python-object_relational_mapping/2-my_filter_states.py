#!/usr/bin/python3
"""Filter states by user input."""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLbd.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], state=sys.argv[4])
    cur = db.cursor()
    sqlQuery = "SELECT * FROM `states` WHERE `name` > '%s'", % format(sys.argv[4])
    cur.execute(sqlQuery)
    results = cur.fetchall()
    for result in results:
        print(result)
