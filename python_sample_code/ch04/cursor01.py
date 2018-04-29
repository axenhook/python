import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立数据库联接
cursor = conn.cursor() # 建立 cursor 对象

#新建一个数据表
sqlstr='CREATE TABLE IF NOT EXISTS table01 \
("num" INTEGER PRIMARY KEY NOT NULL ,"tel" TEXT)'
cursor.execute(sqlstr)

# 新增一条记录
sqlstr='insert into table01 values(1,"02-1234567")'
cursor.execute(sqlstr)

conn.commit() # 主动更新
conn.close()  # 关闭数据库连接
