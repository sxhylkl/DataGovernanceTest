# -*- coding:utf-8 -*-
# @Time 2019/4/1 13:38
# @Author Ma Guichang
"""
1.空值校验，检验列
    a) 空值定义，在mysql中除String类型数据存的数据为空字符串值，其余数据类型的空值为null值
    b) 空值校验，校验结果写到三张表，记录表，错误表，统计表
    *) 需要丰富，写入数据库的内容
"""
import pymysql
import pandas as pd
from flask import Blueprint,jsonify
from DGApp.Configlist import dbConfig
# 批量写入mysql
# from sqlalchemy import create_engine
# yconnect = create_engine('mysql+mysqldb://root:Mgc5320@localhost:3306/datagovernance?charset=utf8')
# pd.io.sql.to_sql(thedataframe,'tablename', yconnect, schema='databasename', if_exists='append')


app01=Blueprint('app01',__name__)
# 导入数据库配置参数
para = dbConfig.Config()
# 创建数据库连接
conn = pymysql.Connect(
    host = para.MYSQL_URI,
    port = para.MYSQL_PORT,
    user = para.MYSQL_USER,
    passwd = para.MYSQL_PWD,
    db = para.MYSQL_DB,
    charset = para.MYSQL_CHARSET
)
cur = conn.cursor()

@app01.route('/fieldNull')
def checkNull():
    null_num = 0
    sql = "select * from datagovernance.testdata"
    dfData = pd.read_sql(sql, conn, chunksize=2000)
    for df in dfData:
        v_null = pd.DataFrame(df['address'].isnull())
        v_null_count = pd.value_counts(v_null['address'])
        null_num = null_num + v_null_count[True]
    v_null_data = {'null data num:':str(null_num)}
    print(v_null_data)
    return jsonify(v_null_data)




# @app01.route('/')
# def show():
#     return 'app01.hello'