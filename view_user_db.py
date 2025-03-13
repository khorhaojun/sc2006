import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('user_info.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to retrieve all rows from the users table
cursor.execute('SELECT * FROM users')

# Fetch all rows from the result of the query
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection
conn.close()
