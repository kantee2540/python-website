#!C:\wamp64\www\website\venv\Scripts\python.exe
#!C:\xampp\htdocs\python-website\venv\Scripts\python.exe


import cgi
import datetime
import hashlib
import sqlite3


def register_process(username, password, firstname, lastname):
    try:
        with sqlite3.connect('Database/practice.sqlite3') as c:
            register_date = datetime.datetime.now()
            formatted_date = register_date.strftime("%D-%H:%M:%S")
            sql_command = """INSERT INTO users(username, password, name, lastname, registerDate) 
            VALUES('{}', '{}', '{}', '{}', '{}')""".format(username,
                                                           password,
                                                           firstname,
                                                           lastname,
                                                           formatted_date)
            c.execute(sql_command)

    except Exception as e:
        print("Error = {}".format(e))

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')
name = form.getvalue('name')
lastname = form.getvalue('lastname')
# Secure password text=
password_encode = hashlib.md5(password.encode()).hexdigest()
register_process(username, password_encode, name, lastname)

print("Content-Type:text/html")
print()
print("<html>")
print("<body>")
print("<p>Congrat! <b>{} {}</b> You registered</p>".format(name, lastname))
print("<p>Go back to previous page</p>")
print("<p><a href=\"login.html\">Return</a></p>")
print("</body>")
print("</html>")


