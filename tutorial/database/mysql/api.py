# -*- coding: utf-8 -*-

import pymysql

"""
注意操作MySQL时先确保MySQL是开启状态，否则连接不上数据库

"""


def get_connection():
    """
    获得数据库连接对象
    :return:
    """
    conn = pymysql.connect("localhost", "root", "cucumber", "lightning_storm", charset='utf8')
    return conn


def create_table():
    """
    创建数据库表
    :return:
    """
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS books")
    sql = """create table books (
         id int not null auto_increment primary key,
         book_name char(20) not null,
         reading_state  int );
         """
    cursor.execute(sql)
    cursor.close()
    db.close()


def add():
    """
    添加一条数据
    :return:
    """
    conn = get_connection()
    cursor = conn.cursor()
    data = [
        ['The Ocean', 2], ['How to talk', 1]
    ]
    sql = "insert into books (book_name, reading_state) values (%s, %s)"
    # cursor.execute(sql, ['The Ocean', 2])
    cursor.executemany(sql, data)
    conn.commit()
    cursor.close()
    conn.close()


def delete():
    """
    删除一条数据
    :return:
    """
    conn = get_connection()
    cursor = conn.cursor()
    sql = "delete from books where id=%s;"
    cursor.execute(sql, [2])
    conn.commit()
    cursor.close()
    conn.close()


def update():
    """
    查找一条数据
    :return:
    """
    conn = get_connection()
    cursor = conn.cursor()
    sql = "update books set reading_state=%s where id=%s;"
    cursor.execute(sql, [1, 2])
    conn.commit()
    cursor.close()
    conn.close()


def query():
    """
    查询数据
    :return:
    """
    conn = get_connection()
    cursor = conn.cursor()
    sql = "select * from books"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()
