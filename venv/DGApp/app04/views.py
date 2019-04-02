# -*- coding:utf-8 -*-
# @Time 2019/4/1 14:53
# @Author Ma Guichang

"""
 4.格式校验，检验列，格式要求
    a) 输入列名，检验该列的数据的格式是否符合要求（以邮箱格式为例）
    ?) 格式的校验结果返回什么，不符合邮箱格式的数量与索引？
    b) 数据格式:邮箱，身份证，手机号
"""
import pymysql
import pandas as pd
from flask import Blueprint,jsonify
from DGApp.Configlist import dbConfig
# 校验值域，长度，邮件
from validators import between,length,email
# 导入手机号与身份证校验
from DGApp.app04.phoneAndCardsCheck import *

app04=Blueprint('app04',__name__)
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

@app04.route('/')
def checkFormat():

    sql = "SELECT * from datagovernance.testdata"
    dfData = pd.read_sql(sql, conn, chunksize=2000)
    email_num = 0
    # 检验该列所有数据的格式
    for df in dfData:
        for d in df['emailinfo']:
            if email(d):
                email_num = email_num+1
    return str(email_num)

# @app03.route('/')
# def show():
#     return 'app03.hello'