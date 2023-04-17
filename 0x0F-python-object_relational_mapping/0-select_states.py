#!/usr/bin/python3
# lists all data from the table states

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Variables
    username = argv[1]  # Mysql username
    password = argv[2]   # Mysql password
    db_name = argv[3]   # Database Name

# Connection setup to mysqldb
    db = MySQLdb.connect(
                      host="localhost",
                      port=3306,
                      user=username,
                      passwd=password,
                      db=db_name,)
# port 3306 is the default port for classic mysql protocol

# getting a cursor in mysql python
mycursor = db.cursor()

# The commands to be executed in mysql
sql = "SELECT * FROM states ORDER by id;"

mycursor.execute(sql)

# to print result to screen
res = mycursor.fetchall()
# fetchall fetches all rows from last executed command

for res in res:  # res in res allows it to print on a new line
    print(res)

mycursor.close()
db.close()
