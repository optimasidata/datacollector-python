from impala.dbapi import connect

conn = connect(host="xxx.xxx.xxx.xxxx", database='XXXXX', port=21050, auth_mechanism='GSSAPI', timeout=100000, use_ssl=False, ca_cert=None, ldap_user=None, ldap_password=None,  kerberos_service_name='impala',krb_host='impala.XXX.Xo.id')
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

print("SHOW TABEL")
for t in tables:
    print(t[0])
print("eol >>>")
