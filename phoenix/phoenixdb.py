'''
connect to secured phoenix server (kerberized)
'''
import phoenixdb
import phoenixdb.cursor
import sys
database_url = 'http://xx.xxx.xxx.xx:8765/'


conn = phoenixdb.connect(database_url, autocommit=True, auth="SPNEGO")
cursor = conn.cursor()
cursor.execute("select * from XXX.XXXX")
result =  cursor.fetchall()
print (result)
