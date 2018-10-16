import psycopg2 #Like connecting to SQLite with sqlite3
connObj=psycopg2.connect("dbname=dq user=dq")
print(connObj)
connObj.close()
