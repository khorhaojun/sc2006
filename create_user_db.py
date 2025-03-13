import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_info.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for storing user information
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
