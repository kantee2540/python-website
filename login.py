#!C:\xampp\htdocs\python-website\venv\Scripts\python.exe
#!C:\wamp64\www\website\venv\Scripts\python.exe

import cgi
import hashlib
import sqlite3


def login_process(username, password):
    with sqlite3.connect("Database/practice.sqlite3") as con:
        con.row_factory = sqlite3.Row
        sql_command = "SELECT * FROM users WHERE username = '{}'".format(username)
        cursor = con.execute(sql_command)
        for i in cursor:
            if password == i['password']:
                print("Welcome, <b>{} {}</b>".format(i['name'], i['lastname']))
                return True

            else:
                return False


form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

password_encode = hashlib.md5(password.encode()).hexdigest()

print("Content-Type:text/html")
print()
print("<html>")
print("<body>")
if login_process(username, password_encode):
    print("OK")
else:
    print("Failed! Please try again")
print("</body>")
print("</html>")


