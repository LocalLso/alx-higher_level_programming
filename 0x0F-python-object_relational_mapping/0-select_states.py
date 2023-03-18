#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
db = MySQLdb.connect(host = "localhost", user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM `states` ORDER BY `id` ASC")
results = cur.fetchall()
for result in results:
    [print (state)]
db.close()

