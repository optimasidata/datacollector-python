import happybase

connection = happybase.Connection('10.xx.xxx.xxx',9090)

connection.open()
print(connection.tables())
