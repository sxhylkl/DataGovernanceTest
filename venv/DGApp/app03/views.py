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
from datetime import datetime
import numpy as np
import pandas as pd
from enum import Enum,IntEnum,unique
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

@app03.route('/checkValueRange/<rangeType>/<minValue>/<maxValue>/<database>/<table>/<field>',methods = ['GET','POST'])
def checkValueRange(rangeType,minValue,maxValue,database,table,field):
    """
    值域校验: 数值区间，字符in，日期范围，
    :param database: 校验数据库
    :param table: 校验数据表
    :param field: 校验列
    :return:
    """
    db = database
    tb = table
    fd = field
    accordValueRangeNum = 0
    sql = "SELECT "+fd+" from "+db+"."+tb
    dfData = pd.read_sql(sql, conn, chunksize=2000)
    # print(minValue,maxValue)

    # 检验该列数据的值域
    if rangeType == 'valueRange':
        for df in dfData:
            for d in df[fd]:
                if between(d, min = np.float(minValue), max = np.float(maxValue)):
                    accordValueRangeNum = accordValueRangeNum +1
        return str(accordValueRangeNum)
    # 字符枚举
    elif rangeType == 'charIn':
        for df in dfData:
            for d in df[fd]:
                if d in [minValue,maxValue]:
                    accordValueRangeNum = accordValueRangeNum + 1
        return str(accordValueRangeNum)
    # 时间区间
    elif rangeType == 'dateIn':
        mindate = datetime.strptime(minValue,'%Y-%m-%d %H:%M:%S')
        maxdate = datetime.strptime(maxValue,'%Y-%m-%d %H:%M:%S')
        for df in dfData:
            for d in df[fd]:
                if mindate<d<maxdate:
                    accordValueRangeNum = accordValueRangeNum + 1
        return  str(accordValueRangeNum)

# 访问示例127.0.0.1:5000/app03/checkValueRange/charIn/beijing/shanghai/datagovernance/testdata/address
# 访问示例127.0.0.1:5000/app03/checkValueRange/dateIn/2019-03-01 11:13:58/2019-04-04 11:13:58/datagovernance/testdata/dtime
# @app03.route('/')
# def show():
#     return 'app03.hello'