import sqlite3

name = input("Enter name: ")
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()
cursor.execute("""
    SELECT "balance" FROM "Card" WHERE "holder"=?
    """, [name])
result = cursor.fetchall()[0][0]
conn.close()
print(result)

