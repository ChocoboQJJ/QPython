'''
Date: 2022-02-22 09:48:53
LastEditors: ChocoboQJJ
LastEditTime: 2022-02-24 16:59:06
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
    :param return:连接对象
    '''
    conn = psycopg2.connect(database=dbName, user=user, password=pwd, host=host, port=port)
    print("PGSQL连接成功")
    return conn

def DisconnectPG(pgConn):
    '''
    :param 函数描述:断开数据库连接
    :param dbName:数据库名称(默认为postgres)
    :param user:用户名(默认为postgres)
    :param pwd:密码(默认为postgres)
    :param host:连接地址(默认为127.0.0.1)
    :param port:连接端口(默认为5432)
    :param return:连接对象
    '''
    pgConn.close()
    print("关闭PGSQL连接")

def SelectPG(pgConn,sql):
    '''
    :param 函数描述:执行自定义Select拼接语句
    :param pgConn:连接对象(pgConn对象通过ConnectPG函数来获取)
    :param sql:自定义Select拼接语句(语句省略开头Select语法)
    '''
    cur = pgConn.cursor()
    cur.execute(" SELECT "+str(sql))
    rows = cur.fetchall()
    print(rows)
    return rows

def UpdatePG(pgConn,sql):
    '''
    :param 函数描述:执行自定义Update拼接语句
    :param pgConn:连接对象(pgConn对象通过ConnectPG函数来获取)
    :param sql:自定义Update拼接语句(语句省略开头Update语法)
    '''
    cur = pgConn.cursor()
    cur.execute(" Update "+str(sql))
    pgConn.commit()
    print("成功修改: "+str(cur.rowcount)+" 条数据")

def DeletePG(pgConn,sql):
    '''
    :param 函数描述:执行自定义Delete拼接语句
    :param pgConn:连接对象(pgConn对象通过ConnectPG函数来获取)
    :param sql:自定义Delete拼接语句(语句省略开头Delete语法)
    '''
    cur = pgConn.cursor()
    cur.execute(" Delete "+str(sql))
    pgConn.commit()
    print("成功删除: "+str(cur.rowcount)+" 条数据")