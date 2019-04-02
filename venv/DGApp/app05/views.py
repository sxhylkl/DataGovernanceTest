# -*- coding:utf-8 -*-
# @Time 2019/4/1 15:11
# @Author Ma Guichang

"""
 5.长度校验，检验列，长度要求
    a) 输入列名，检验该列的数据的长度是否符合要求（以手机号/身份证长度为例）
    ?) 格式的校验结果返回什么，不符合邮箱格式的数量与索引？
"""
import pymysql
import pandas as pd
from flask import Blueprint,jsonify
from DGApp.Configlist import dbConfig
# 校验值域，长度，邮件
from validators import between,length,email

app05=Blueprint('app05',__name__)
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

@app05.route('/')
def checkFormat():

    sql = "SELECT * from datagovernance.testdata"
    dfData = pd.read_sql(sql, conn, chunksize=2000)
    length_num = 0
    # 检验该列所有数据的格式
    for df in dfData:
        for d in df['emailinfo']:
            # 校验手机号11位
            if length(d,min= 11,max=11):
                length_num = length_num+1
    return str(length_num)

# @app05.route('/')
# def show():
#     return 'app05.hello'