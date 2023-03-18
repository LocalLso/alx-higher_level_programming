#!/usr/bin/python3
"""Filter states by user input."""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLbd.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], state=sys.argv[4])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    results = cur.fetchall()
    for result in results:
        if (result == sys.argv[4]):
            format"
