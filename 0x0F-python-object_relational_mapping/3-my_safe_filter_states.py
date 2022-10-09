#!/usr/bin/python3
# 3-my_safe_filter_states.py

"""
A script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connection
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    if ';' not in argv[4]:
        value = argv[4]
    else:
        idx = argv[4].index(";")
        value = argv[4][1: idx - 1]

    # Query
    cur.execute(
            "SELECT * FROM states WHERE name='{name}' ORDER BY states.id"
            .format(name=value)
            )
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # Close connection
    cur.close()
    db.close()
