from impala.dbapi import connect


conn = connect(host='10.xx.xx.xx', port=21050,database='XXXXX')
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

print("show list TABEL")
for t in tables:
    print(t[0])
