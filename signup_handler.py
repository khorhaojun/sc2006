from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import sqlite3
import os
import hashlib

print("Content-Type: text/html")
print()
# Get form data
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/signup.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('signup.html', 'r') as file:
                self.wfile.write(bytes(file.read(), 'utf-8'))
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('signup.html', 'r') as file:
                self.wfile.write(bytes(file.read(), 'utf-8'))
        else:
            self.send_response(405)
            self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            form = urllib.parse.parse_qs(post_data.decode('utf-8'))
            username = form.get('username')[0]
            email = form.get('email')[0]
            password = form.get('password')[0]

            # Hash the password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Connect to SQLite database
            with sqlite3.connect('user_info.db') as conn:
                cursor = conn.cursor()

                print(f"Inserting user: {username}, {email}, {hashed_password}")
                cursor.execute('''
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
                ''', (username, email, hashed_password))
                print("User inserted successfully.")

                # Commit the changes and close the connection
                conn.commit()

            # Redirect to login page
            self.send_response(301)
            self.send_header('Location', '/login.html')
            self.end_headers()
        except sqlite3.IntegrityError as e:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(f"Database error: {str(e)}", "utf-8"))
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(f"Error: {str(e)}", "utf-8"))

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running server...')
    httpd.serve_forever()
