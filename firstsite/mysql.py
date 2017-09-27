import MySQLdb
conn = MySQLdb.Connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = '',
	db = 'test',
	charset = 'utf8'
	)
cursor = conn.cursor()
sql = "select * from python"
cursor.execute(sql)

# print cursor.rowcount
# re = cursor.fetchall()
# for row in re:
# 	print "userid=%s, username=%s" % row
# print re
sql_insert = "insert into python(id, name) values(10, 'name10')"
sql_update = "update python set name='name21' where id = 3"
sql_delete = "delete from python where id<3"
try:
	cursor.execute(sql_insert)
	print cursor.rowcount
	cursor.execute(sql_update)
	print cursor.rowcount
	cursor.execute(sql_delete)
	print cursor.rowcount

	conn.commit()
except Exception as e:
	print e
	conn.rollback()



cursor.close()
conn.close()
