# -*- coding:utf-8 -*-
# @Time 2019/4/2 8:57
# @Author Ma Guichang

"""
 6.离群值检查
    a) 离群值检查用于检查数据中是否有一个或几个数值与其他数值相比差异较大。
    b) 通过计算出指标的算术平均值和标准差后，根据拉依达法或者格鲁布斯法检查数据中与其他数值相比差异较大的数。
    ?) 临界值表中的T的获取（待处理）
"""
import pymysql
import numpy as np
import pandas as pd
from flask import Blueprint,jsonify
from DGApp.Configlist import dbConfig

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


@app06.route('/checkOutlier/<funType>/<database>/<table>/<field>',methods = ['GET','POST'])
def checkOutlier(funType,database,table,field):
    """
    离群值检查
    :param database: 校验数据库
    :param table: 校验数据表
    :param field: 校验列
    :return:
    """
    db = database
    tb = table
    fd = field
    sql = "SELECT "+fd+ " FROM "+db+"."+tb
    dfData = pd.read_sql(sql, conn)
    dataMean = dfData.mean()[fd]
    dataStd = dfData.std()[fd]
    if funType == "S3":
        # S3法则计算：当某一测量数据与其测量结果的算术平均值之差大于3倍标准偏差时，则该检查数据不符合规则。
        res = np.abs(np.array(dfData.get(fd))-dataMean)-3*dataStd
        # 尝试使用numpy优化
        outlierNum = len([d for d in res if d > 0])
        return jsonify({"outlierNum": str(outlierNum)})
    elif funType == "glbs":
        # 格鲁布斯法：计算公式为T = | X质疑—X平均 | / S，其中，S为这组数据的标准差(?需要对比临界值表中的T)
        Tdata = np.abs(np.array(dfData.get(fd)) - dataMean)/dataStd
        # 表达式中的T为临界值表中的T
        outlierNum = len([d for d in Tdata if d-T > 0])
        pass


# @app06.route('/')
# def show():
#     return 'app06.hello'