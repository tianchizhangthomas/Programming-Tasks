# Create a table to store properties from issue reports.
import psycopg

# Get the database connection and a cursor to execute queries.
conn = psycopg.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port=5432)
cur = conn.cursor()

# Create the table.
cur.execute('''CREATE TABLE IF NOT EXISTS issue_reports (
            id SERIAL PRIMARY KEY,
            Type VARCHAR,
            Priority VARCHAR,
            Components VARCHAR,
            Status VARCHAR,
            Resolution VARCHAR,
            Assignee VARCHAR,
            Reporter VARCHAR,
            Votes INTEGER,
            Watchers INTEGER,
            Created VARCHAR,
            Updated VARCHAR,
            Resolved VARCHAR,
            Description VARCHAR,
            Comments TEXT[]
            );''')

conn.commit()
cur.close()
conn.close()
