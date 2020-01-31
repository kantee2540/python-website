#!C:\wamp64\www\website\venv\Scripts\python.exe
import cgi
import hashlib

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

password_encode = hashlib.md5(password.encode()).hexdigest()
