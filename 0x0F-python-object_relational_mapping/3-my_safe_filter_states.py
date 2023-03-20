#!/usr/bin/python3
""" Script safe from MySQL injection."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    sqlQ = ("SELECT * FROM `states`")
    c.execute(sqlQ)
    results = c.fetchall()
    for result in results:
        if (result[1] == sys.argv[4]):
            print(result)
    
