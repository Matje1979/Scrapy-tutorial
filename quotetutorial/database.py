import sqlite3

print ("Hello")

conn = sqlite3.connect("myquotes.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE quotes_tb(
                title text,
                author text,
                tag text
                ) """)
conn.commit()
conn.close()