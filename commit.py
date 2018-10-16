import psycopg2
connObj=psycopg2.connect("dbname=dq user=dq")
cur=connObj.cursor()
query="CREATE TABLE users (id integer PRIMARY KEY,  email text, name text, address text)"
cur.execute(query)
connObj.commit()
connObj.close()
