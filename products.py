#!C:\xampp\htdocs\python-website\venv\Scripts\python.exe
#!C:\wamp64\www\website\venv\Scripts\python.exe

from databaselibrary import connect_db

def show_data():
    connect = connect_db()
    cur = connect.cursor()
    sql_command = """SELECT * FROM products p, suppliers s, categories c
                    WHERE p.SupplierID = s.SupplierID AND p.CategoryID = c.CategoryID
                    ORDER BY ProductID"""
    cur.execute(sql_command)
    print("<p>{} Records found</p>".format(cur.rowcount))
    for i, row in enumerate(cur):
        if i % 2 == 0:
            print("<tr style=\"background-color: powderblue;\">")
        else:
            print("<tr style=\"background-color: skyblue;\">")
        print("<td>{}</td>".format(row['ProductID']))
        print("<td>{}</td>".format(row['ProductName']))
        print("<td>{}</td>".format(row['CompanyName']))
        print("<td>{}</td>".format(row['CategoryName']))
        print("<td>{}</td>".format(row['UnitPrice']))
        print("</tr>")

print("Content-Type:text/html")
print()
print("<html>")
print("<body>")
print("<h1>Products</h1>")
print("<a href=\"insertproduct.py\">Insert data</a>")
print("<table border=1>")
print("<tr style=\"background-color: deepskyblue;\">")
print("<th>ProductID</th>")
print("<th>ProductName</th>")
print("<th>SupplierName</th>")
print("<th>Category</th>")
print("<th>UnitPrice</th>")
print("</tr>")
show_data()
print("</table>")
print("</body>")
print("</html>")
