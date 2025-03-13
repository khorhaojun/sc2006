import sqlite3

try:
    conn = sqlite3.connect('user_info.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print("Users in the database:", users)
    conn.close()
except sqlite3.Error as e:
    print("Error connecting to database:", e)
