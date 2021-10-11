# connecting to Impala Server


Install Impala package
```shell
pip install thrift
pip install thrift-sasl
pip install thriftpy2
pip install impyla
```

Sample Connection to non-Secured Impala server
```python
from impala.dbapi import connect
conn = connect(host='xxx.xxx.xxx.xxx', port=21050,database='XXXXXX')
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

print("show list TABEL")
for t in tables:
    print(t[0])
```    

Sample Connection to Secured Impala server
```python
from impala.dbapi import connect
conn = connect(host="xxx.xxx.xxx.xxx", database='XXXXX', port=21050, auth_mechanism='GSSAPI', timeout=100000, use_ssl=False, ca_cert=None, ldap_user=None, ldap_password=None,  kerberos_service_name='impala',krb_host='impala.fqdn')
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

print("SHOW TABEL")
for t in tables:
    print(t[0])
print("eol >>>")

```
