from firebird.driver import connect

con = connect(
    '192.168.100.119/3050:/db/db.fdb',
    user='SYSDBA',
    password='masterkey',
)

cur = con.cursor()
cur.execute('select * from LANGUAGES')
print(cur.fetchall())
con.close()