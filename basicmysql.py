import pymysql

con = pymysql.connect(host='localhost',
                      port=3306,
                      user='root',
                      password='',
                      db='py_northwind',
                      cursorclass=pymysql.cursors.DictCursor,
                      autocommit=True)

curr = con.cursor()
sql_command ="""SELECT * FROM products"""
curr.execute(sql_command)
for row in curr:
    print("Product ID = {}".format(row['ProductID']))
    print("Product Name = {}".format(row['ProductName']))
