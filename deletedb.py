import sqlite3

connection=sqlite3.connect('parking.db')

cursor=connection.cursor()

delete_id=input("Enter the id of the vehcile you want to delete:")

cursor.execute(
    "DELETE FROM parking WHERE id=?",(delete_id,)
)

connection.commit()
connection.close()

print("Data has been delete successfully..")