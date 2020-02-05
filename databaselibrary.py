import pymysql


def connect_db():
    con = pymysql.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='',
                          db='py_northwind',
                          cursorclass=pymysql.cursors.DictCursor,
                          autocommit=True)

    return con
