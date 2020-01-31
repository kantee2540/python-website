#!C:\wamp64\www\website\venv\Scripts\python.exe
import random
import cgi
form = cgi.FieldStorage()
c = int(form.getvalue('cols'))
r = int(form.getvalue('rows'))

print("Content-Type:text/html")
print()
print("<html>")
print("<body>")
print("<table border=1>")
for i in range(r):
    print("<tr>")
    for q in range(c):
        file_num = random.randint(0, 4)
        if q == 0 or i == 0:
            print("<td><img src='image/{}.jpg' width=100 height=100></td>".format(file_num))
        elif q == c - 1 or i == r - 1:
            print("<td><img src='image/{}.jpg' width=100 height=100></td>".format(file_num))
        else:
            if i % 2 == 0:
                print("<td bgcolor=\"#66ccff\">KANTEE</td>")
            else:
                print("<td bgcolor=\"#008ae6\">KANTEE</td>")
    print("</tr>")

print("</table>")
print("</body>")
print("</html>")
