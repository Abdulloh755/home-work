# SQL - язык структор
# DATAbase
# Crud - crate, update,read,delete
# СУБД - система управленния баз данных

import sqlite3
with sqlite3.connect('holodilnik.db') as con:
    cursor = con.cursor()
    # cursor.execute('''DROP TABLE IF EXISTS eat''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    full_name VARCHAR(104) NOT NULL,
    age INT DEFAULT 8,
    hobby TEXT NOT NULL
    
    )''')
# # create
#     cursor.execute('''INSERT INTO users(full_name,age,hobby)
#     VALUES ('amir',14,'bassket')''')

    # update
    # cursor.execute('''UPDATE users SET full_name='bakai'
    # WHERE full_name='aimir'  ''')


    cursor.execute('''UPDATE users SET full_name='akel' 
    WHERE rowid=2''')

    cursor.execute('''SELECT rowid, * FROM users ''')
    for i in cursor.fetchall():
        print(i)

    # cursor.execute('''CREATE TABLE IF NOT EXISTS eat(
    # органические TEXT NOT NULL,
    # водные TEXT NOT NULL ,
    # консервы TEXT NOT NULL,
    # id INTEGER
    # ) ''')
