# -*- coding:utf-8 -*-
# @Time 2019/4/2 8:57
# @Author Ma Guichang

"""
 6.单表单行校验
    a) 列关系
"""
import pymysql
import pandas as pd
from flask import Blueprint,jsonify
from DGApp.Configlist import dbConfig
from validators import between,length,email
from DGApp.app04.phoneAndCardsCheck import *

app06=Blueprint('app06',__name__)
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

@app06.route('/singleRow')
def checkSingleTableRow():

    sql = "SELECT * from datagovernance.testdata"
    dfData = pd.read_sql(sql, conn, chunksize=2000)
    email_num = 0
    for df in dfData:
        for d in df['emailinfo']:
            if email(d):
                email_num = email_num+1
    return str(email_num)

# @app06.route('/')
# def show():
#     return 'app06.hello'