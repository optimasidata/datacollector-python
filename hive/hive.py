from pyhive import hive

conn = hive.Connection(host="master-1", port=10000, username="root", auth="NONE")
cursor = conn.cursor()
cursor.execute("select * from db.table limit 10")
print(cursor.fetchall())
