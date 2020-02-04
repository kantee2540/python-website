#!C:\wamp64\www\website\venv\Scripts\python.exe

from databaselibrary import connect_db

def get_option_supplier():
    connect = connect_db()
    cur = connect.cursor()
    sql_command = """SELECT * FROM suppliers"""
    cur.execute(sql_command)
    for i, row in enumerate(cur):
        print("<option value=\"{}\">{}</options>".format(row["SupplierID"]
                                                         , row["CompanyName"]))


def get_option_category():
    connect = connect_db()
    cur = connect.cursor()
    sql_command = """SELECT * FROM categories"""
    cur.execute(sql_command)
    for row in cur:
        print("<option value=\"{}\">{}</option>".format(row["CategoryID"],
                                                        row["CategoryName"]))

if __name__ == '__main__':
    print("Content-Type:text/html")
    print()
    print("<html>")
    print("<body>")
    print("<h1>Insert Product</h1>")
    print("<form>")
    print("<table>")

    # Product name
    print("<tr>")
    print("<td>ProductName</td>")
    print("<td><input type=\"text\"></td>")
    print("</tr>")

    # Supplier
    print("<tr>")
    print("<td>Supplier Name</td>")
    print("<td>")
    print("<select name=\"suppliers\">")
    get_option_supplier()
    print("</select>")
    print("<td>")
    print("</tr>")

    # category
    print("<tr>")
    print("<td>Category</td>")
    print("<td>")
    print("<select>")
    get_option_category()
    print("</select>")
    print("</td>")
    print("</tr>")

    print("<tr>")
    print("<td>QuantityPerUnit</td>")
    print("<td><input name=\"quantity\" type=\"text\"></td>")
    print("</tr>")

    print("<tr>")
    print("<td>UnitPrice</td>")
    print("<td><input name=\"unitprice\" type=\"number\"></td>")
    print("</tr>")

    print("<tr>")
    print("<td>UnitsInStock</td>")
    print("<td><input name=\"unitstock\" type=\"number\"></td>")
    print("</tr>")

    print("<tr>")
    print("<td>UnitsOnOrder</td>")
    print("<td><input name=\"unitorder\" type=\"number\"></td>")
    print("</tr>")

    print("<tr>")
    print("<td>ReorderLevel</td>")
    print("<td><input name=\"reorderlevel\ type=\"number\"></td>")
    print("</tr>")

    print("<tr>")
    print("<td>Discontinued</td>")
    print("<td><input type=\"checkbox\" name=\"discontinued\" value=1></td>")
    print("</tr>")

    print("<tr>")
    print("<td colspan=3><input type=\"submit\" value=\"Submit\" style=\"width: 100%; height: 40px;\"></td>")
    print("</tr>")
    print("</table>")
    print("</form>")
    print("</body>")
    print("</html>")
