# -*- coding: utf-8 -*-

import sqlite3


def get_connection():
    """
    获得数据库连接对象
    :return:
    """
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('books.db')
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
         id int not null primary key,
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
    sql = "insert into books (id, book_name, reading_state) values (1, 'The Ocean', 2)"
    # cursor.execute(sql, ['The Ocean', 2])
    cursor.execute(sql)
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
    sql = "delete from books where id=1;"
    cursor.execute(sql)
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
    sql = "update books set reading_state=1 where id=1;"
    cursor.execute(sql)
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

