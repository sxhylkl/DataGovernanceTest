# -*- coding:utf-8 -*-
# @Time 2019/4/1 14:35
# @Author Ma Guichang

"""
 3.值域检验，检验列，约束类型，值域要求
    a) 输入列名，上下限约束值，或多值约束条件，检验该列的数据的值域是否符合要求
    ?) 值域检验，是检验这一列数据的取值范围，还是给定一个范围，看该列数据有多少或是全部在这个范围内
    b) 枚举，区间，字符 in，日期,需要四个方法
"""
import pymysql
import pandas as pd
from flask import Blueprint,jsonify
from DGApp.Configlist import dbConfig
# 校验值域，长度，邮件
from validators import between,length,email

app03=Blueprint('app03',__name__)
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

@app03.route('/')
def checkValueRange():

    # 数值区间
    def valueRange(data,minData,maxData):
        if between(data,min = minData,max = maxData):
            pass
        return "valueRange"
    # 字符 in
    def charIn(des,src):
        if src in des:
            pass
        return  "charIn"

    # 日期 in
    def dateIn(startDate,endDate):
        pass

    sql = "SELECT * from datagovernance.testdata"
    dfData = pd.read_sql(sql, conn, chunksize=2000)

    accordValueRangeNum = 0
    # 检验该列数据的值域
    for df in dfData:
        for d in df:
            if between(d,min=13, max=50):
                accordValueRangeNum = accordValueRangeNum +1

    return str(ftype.values[0])

# @app03.route('/')
# def show():
#     return 'app03.hello'