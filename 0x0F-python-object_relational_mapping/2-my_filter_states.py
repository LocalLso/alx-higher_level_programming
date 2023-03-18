#!/usr/bin/python3
"""Filter states by user input."""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(sys.argv[4]))
    results = cur.fetchall()
    for result in results:
        print(result)
