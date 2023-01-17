# (TEST) this file is used to test database

import sqlite3

# Connecting to sqlite
connection = sqlite3.connect("users2.db") # makes the connection

# cursor object
cursor_obj = connection.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS USER")

# Creating table
table = """ CREATE TABLE USER (
            id INTEGER NOT NULL,
            firstName CHAR(250) NOT NULL,
            lastName CHAR(250) NOT NULL,
            bio VARCHAR(255),
            PRIMARY KEY(id AUTOINCREMENT)
        ); """
cursor_obj.execute(table)

# release_list = [
#     (1997, "Grand Theft", "Auto", "state of New Guernsey"),
#     (1999, "Grand Theft", "Auto 2","Anywhere, USA"),
#     (2001, "Grand Theft", "Auto III","Liberty City"),
#     (2002, "Grand Theft", "Auto: Vice City","Vice City"),
#     (2004, "Grand Theft Auto", "San Andreas","state of San Andreas"),
#     (2008, "Grand Theft", "Auto IV","Liberty City"),
#     (2013, "Grand Theft", "Auto V","Los Santos")
# ]  
for i in range(0, len(release_list), 10000):
    chunck = release_list[i:i + 10000]
    print(i)
    for y in chunck:
        operation = 'insert into user values {}'.format(y)
        cursor_obj.execute(operation)

connection.commit()
# cursor.executemany("insert into user values(?, ?, ?, ? )", release_list)
# #print specific row
# cursor.execute("select * from user where firstName=:n", {"n": "Grand Theft"})
# search = cursor.fetchall()
# print(search)

connection.close()