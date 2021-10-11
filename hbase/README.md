# connecting to HBase thrift Server


Install hbase driver package
```shell
pip install happybase
```


Sample Connection to Hbase thrift server
```python
import happybase
connection = happybase.Connection('xxx.xxx.xxx.xxx',9090)

connection.open()
print(connection.tables())

```

For kerberized Cluseter, make initialize
```shell
kinit -kt hbase_user
```
