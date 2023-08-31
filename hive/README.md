# connecting to HIVE Server


Install hbase driver package
```shell
pip install pyhive
pip install thrift
pip install sasl
pip install thrift_sasl

```


Sample Connection to Hbase thrift server
```python
from pyhive import hive

conn = hive.Connection(host="master-1", port=10000, username="root", auth="NONE")
cursor = conn.cursor()
cursor.execute("select * from db.table limit 10")
print(cursor.fetchall())

```

# HUE
pip3 install impyla==0.16.2
