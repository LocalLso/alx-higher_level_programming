#!/usr/bin/python3
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
databasename = sys.argv[3]

db = MySQLdb.connect(host = "localhost", user = "root", passwd = "root", db = "hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
db.close()

