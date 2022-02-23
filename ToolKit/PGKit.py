'''
Date: 2022-02-22 09:48:53
LastEditors: ChocoboQJJ
LastEditTime: 2022-02-23 14:58:40
FilePath: \QPython\ToolKit\PGKit.py
'''
import psycopg2

def ConnectPG(dbName="postgres",user="postgres",pwd="postgres",host="127.0.0.1",port="5432"):
    '''
    :param 函数描述:连接指定的PostgreSql数据库
    :param dbName:数据库名称(默认为postgres)
    :param user:用户名(默认为postgres)
    :param pwd:密码(默认为postgres)
    :param host:连接地址(默认为127.0.0.1)
    :param port:连接端口(默认为5432)
    :param return:PG连接指针
    '''
    conn = psycopg2.connect(database=dbName, user=user, password=pwd, host=host, port=port)
    print("PGSQL连接成功")
    return conn.cursor()

def SelectPG(cursor,sql):
    '''
    :param 函数描述:执行自定义select拼接语句
    :param cursor:PG连接指针(cursor对象通过ConnectPG函数来获取)
    :param sql:自定义select拼接语句(语句省略开头SELECT语法)
    '''
    cur.execute(" SELECT "+str(sql))
    rows = cur.fetchall()
    print(rows)
    return rows