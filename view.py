import pymysql

conn = pymysql.connect(host='', user='', passwd='', db='', port=3306)
# sql = "select * from test.bpinfo_user"
# sql = "insert into test.20191206011536 VALUES(NULL, 'FilePath_1', 'FilePathServer_2', 'size3', 'type4', 'name5', 'null', False, False);"
sql = "select * from test.20191206011536;"
# sql = ""
cur = conn.cursor()

try:
    cur.execute(sql)
    # conn.commit()
except:
    conn.rollback()
# cur.execute("select * from test.20191206011536;")

rows = cur.fetchall()
print(rows)
conn.close()