'''
Descripttion: 
Author: Liuwen
Date: 2022-11-25 10:06:50
LastEditTime: 2022-12-02 15:59:30
'''
import pymysql
import pandas as pd 

db = pymysql.connect(host='1.13.91.168',port=4728,user='root',password='hyc7!4o%VlEK',db='lw_db')
cursor = db.cursor()
#创建数据库
def create_db():
    cursor.execute("CREATE DATABASE lw_db DEFAULT CHARACTER SET utf8")
    db.close()
#建表
def create_table():
    cursor.execute('DROP TABLE IF EXISTS lw_order')  
    sql = 'CREATE TABLE IF NOT EXISTS lw_order(id INT primary key NOT NULL AUTO_INCREMENT, workno VARCHAR(255), age INT)'
    cursor.execute(sql)
    db.close()
#插入数据
def insert_value(*value):
    # value为不定长参数，类型为元组
    sql = f"INSERT INTO test_table(name, age) values{value}"
    try:
        cursor.execute(sql)
        #数据插入必须做commit()操作
        db.commit()
        print('数据插入成功')
    except:
        db.rollback()
        print('数据插入失败')
    db.close()

# insert_value('lisi',19)
#查询数据
def find_value():
    df = pd.read_sql('select * from lw_food',con=db)
    print(type(df))
    db.close()

find_value()
