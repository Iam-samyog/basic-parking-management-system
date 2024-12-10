#Database for the entire parking system


import sqlite3 


def database_initializer():
    connection=sqlite3.connect("parking.db")

    cursor=connection.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS parking(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        phone_no TEXT NOT NULL,
        vehicle_no   VARCHAR NOT NULL,
        entry_time TEXT,
        exist_time TEXT,
        total_price INTEGER,
        vehicle_type VARCHAR
        
    )
    """
    )
    connection.commit()

    connection.close()
    
    
    
    
