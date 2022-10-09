#!/usr/bin/python3
# 1-flter_states.py

""" Lists all states with a name starting with N """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
