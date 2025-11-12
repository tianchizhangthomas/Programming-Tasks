# Create a table and insert the board matrix into it
import psycopg

# Get the database connection and a cursor to execute queries
conn = psycopg.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port=5432)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS boards (
            id INT PRIMARY KEY,
            board TEXT[][]);''')

cur.execute('''INSERT INTO boards (id, board) VALUES (0,'{{A,B,C,E},{S,F,C,S},{A,D,E,E}}');''')

conn.commit()
cur.close()
conn.close()
