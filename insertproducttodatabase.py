#!C:\xampp\htdocs\python-website\venv\Scripts\python.exe

import cgi
import pymysql
from databaselibrary import connect_db


def insert_to_database(product_data):
    with connect_db() as conn:
        try:
            sql_command = """INSERT INTO products
            (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued) 
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})""".format(product_data['ProductName'],
                                                                                 product_data['SupplierID'],
                                                                                 product_data['CategoryID'],
                                                                                 product_data['QuantityPerUnit'],
                                                                                 product_data['UnitPrice'],
                                                                                 product_data['UnitsInStock'],
                                                                                 product_data['UnitOnOrder'],
                                                                                 product_data['ReorderLevel'],
                                                                                 product_data['Discontinued'])
            conn.execute(sql_command)
            print("Success!")
            print("<script>window.location = \"products.py\";</script>")

        except Exception as e:
            print("Error = {}".format(e))


def get_discontinued_status(value):
    if value == '1':
        return 1
    else:
        return 0


if __name__ == '__main__':
    form = cgi.FieldStorage()

    product_set = {"ProductName": form.getvalue("productname"),
                   "SupplierID": form.getvalue("suppliersid"),
                   "CategoryID": form.getvalue("categoryid"),
                   "QuantityPerUnit": form.getvalue("quantity"),
                   "UnitPrice": form.getvalue("unitprice"),
                   "UnitsInStock": form.getvalue("unitstock"),
                   "UnitOnOrder": form.getvalue("unitorder"),
                   "ReorderLevel": form.getvalue("reorderlevel"),
                   "Discontinued": get_discontinued_status(form.getvalue("discontinued"))}

    print("Content-Type:text/html")
    print()
    print("<html>")
    print("<body>")
    insert_to_database(product_set)
    print("</body>")
    print("</html>")
