'''
selenium读取数据库数据
1安装mysqlclient模块  pip install mysqlclient (第一次安装的时候可能提示要安装xcode客户端)
2获得数据库连接
mysql -uroot -p123456
show databases
create database test_db
use testing_db
create table user_tbl(id int primary key auto_increment, username varchar(20), pwd varchar(20));
desc user_tbl;
insert into user_tbl(username, pwd) values('tom', '123');
insert into user_tbl(username, pwd) values('kite', '456');
insert into user_tbl(username, pwd) values('rose', '789');
3查询数据

'''

import MySQLdb  #需要安装MySqlClient才能使用MySQLdb
import pytest

conn = MySQLdb.connect(
    user='root',
    passwd='123456',
    host='localhost',
    port='3306',
    db='test_db'
)

def get_data():
    query_sql = 'select id, username, pwd from user_tbl' #查询id, pwd from database
    lst = []
    try:
        cursor = conn.cursor()  #从连接里面获得cursor游标
        cursor.execute(query_sql)  #根据这个游标来执行SQL语句
        r = cursor.fetchall() #通过fetch all获取所有的数据
        for x in r: #每次拿到一行数据
            u = (x[0], x[1], x[2]) #x结合下标表示第一列，第二列，第三列，也就是id, username, pwd,作为一个元组，
            lst.append(u) #把获得的元组添加到list里面
        return lst
    finally:
        cursor.close()  #关闭游标
        conn.close()   #关闭数据库

@pytest.mark.parametrize('id, name, pwd', get_data()) #包含多个参数的情况，是一个字符串里面用多个逗号分隔的
def test1(id, name, pwd):
    print(id, name, pwd)

if __name__ == '__main__':
    pytest.main(['-sv'])

