import sqlite3 

connection = sqlite3.connect('mycooldb.db')
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
'''
cursor.execute(create_table)


create_table = '''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
'''
cursor.execute(create_table)


#in sqllite, need to use integer for auto incrementing id 
#only need to specify username and password

connection.commit()

connection.close()