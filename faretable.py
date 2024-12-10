import sqlite3


def fare_table():
    conn=sqlite3.connect('parking.db')
    cursor=conn.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS faretable(
            id INTEGER,
            totalprice INTEGER,
            fare_price INTEGER
            
        )
        
        """
    )
    conn.commit()
    
    conn.close()
    
    
