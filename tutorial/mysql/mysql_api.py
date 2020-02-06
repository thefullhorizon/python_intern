# -*- coding: utf-8 -*-

import pymysql


def get_connection():
    """
    获得数据库对象
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
    cursor.execute("DROP TABLE IF EXISTS BOOKS")
    sql = """CREATE TABLE BOOKS (
         name CHAR(20) NOT NULL,
         category  CHAR(20),
         reading_state  CHAR(20))
         """
    cursor.execute(sql)
    cursor.close()
    db.close()


def query(sql):
    """
    :param sql: 制定的查询语句
    :return:
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)

