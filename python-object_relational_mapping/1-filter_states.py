#!/usr/bin/python3
""" Script that lists all 'states' with a 'name' starting with 'N' from the
    database 'hbtn_0e_usa' """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Scrip that list all states with a name starting with 'N' """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()

    cur.execute("""SELECT * FROM states
                WHERE name like BINARY 'N%'
                ORDER BY id ASC;""")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()