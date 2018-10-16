import psycopg2
connObj=psycopg2.connect("dbname=dq user=dq")
cur=connObj.cursor()
cur.execute("SELECT * from notes")
notes=cur.fetchall()
#print(notes)
cur.close()
