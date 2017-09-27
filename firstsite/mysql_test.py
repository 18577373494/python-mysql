# -*- coding: UTF-8 -*-
from MysqlConn import doSqlRes
# sql = "update python set name=%s,sex=%s where id = 3"
sql = "select * from python where name=%s and sex=%s"
# sql = "insert into python (name,sex) values(%s,%s)"
# sql = "delete from python where name=%s and sex=%s"

tup = ("lili","女")
res = doSqlRes(sql,tup)
print res