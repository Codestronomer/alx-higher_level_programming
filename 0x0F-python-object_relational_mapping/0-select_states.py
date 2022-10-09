#!/usr/bin/python3
# 0-select_states.py

"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

print(argv[1], argv[2])
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
            db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
