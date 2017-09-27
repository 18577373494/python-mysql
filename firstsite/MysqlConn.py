# -*- coding: UTF-8 -*-
import MySQLdb

class ConnMysql():
  #对象初始化
  def __init__(self, host, port, user, passwd, db, charset):
    self.__host = host
    self.__port = port
    self.__user = user
    self.__passwd = passwd
    self.__db = db
    self.__charset = charset
  #定义链接数据库函数
  def Conn(self):
    try:
      return MySQLdb.Connect(
				host = self.__host,
				port = self.__port,
				user = self.__user,
				passwd = self.__passwd,
				db = self.__db,
				charset = self.__charset
			)
      conn.commit()
    except Exception as e:
      print e
      conn.rollback()
  #定义执行操作
  def doSql(self, sql, tup):
    try:
      conn = self.Conn()
      cursor = conn.cursor()
      cursor.execute(sql, tup)
      res = cursor.fetchall()
      conn.commit()
      cursor.close()
      conn.close()
      return res
    except Exception as e:
      print e
      conn.rollback()

def doSqlRes(sql, tup):
  #配置数据库信息
  host = 'localhost'
  port = 3306
  user = 'root'
  passwd = ''
  db = 'test'
  charset = 'utf8'
  #实例化对象
  cm = ConnMysql(host,port,user,passwd,db,charset)
  #执行操作
  re = cm.doSql(sql, tup)
  print re
