# importing the module
import pymysql
# opening a database connection
db = pymysql.connect("host_address","db_name","user_name","pwd")

def execute_query(query):
    # define a cursor object
    cursor = db.cursor
    cursor.execute("Query")
    # execute query
    cursor.execute(sql)
    # close object
    cursor.close()
    db.close()

sql="CREATE TABLE CUSTOMER (CUSTOMER_CODE INT NOT NULL,FIRST_NAME CHAR(15), LAST_NAME CHAR(20))"
execute_query(sql)