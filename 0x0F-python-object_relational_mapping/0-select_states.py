#!/usr/bin/python3
"""
0-select_states.py
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """initializes a db with MySQLdb"""
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])


    """prints all states from input DB"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
