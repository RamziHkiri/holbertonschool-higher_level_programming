#!/usr/bin/python3
""" lists all states starting with N from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 3306
    MY_USER = argv[1]
    MY_PSWD = argv[2]
    MY_DB = argv[3]
    db = MySQLdb.connect(host=HOST, user=MY_USER, password=MY_PSWD,
                         db=MY_DB, port=PORT)
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    cursor.close()
    db.close()
