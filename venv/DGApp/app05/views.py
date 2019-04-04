# -*- coding:utf-8 -*-
# @Time 2019/4/1 15:11
# @Author Ma Guichang

"""
 5.重复数据校验（暂时输入的检验列为一个字段，后期需要对输入参数进行调整）
 重复数据检查用于检查表内是否有重复数据。
 选定实体表并添加需检查的字段，如果仅需检查部分数据，可在过滤条件中输入过滤表达式。
 例如：选择实体表USER并添加重复依据字段name、phone，其他设置默认。
 代表：如果数据中存在name字段和phone字段值都相同的多条数据，则被认定为重复数据，该规则算错 。
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

@app05.route('/checkDuplicate/<database>/<table>/<field>',methods = ['GET','POST'])
def checkFormat(database,table,field):
    """
    重复数据校验
    :param database: 校验数据库
    :param table: 校验数据表
    :param field: 校验列
    :return: 包含的重复数据记录数
    """
    db = database
    tb = table
    fd = field
    sql = "SELECT " + fd + " FROM " + db + "." + tb
    dfData = pd.read_sql(sql, conn) # 一次性读取，测试性能时可分批读取
    checkData = dfData.duplicated().value_counts()
    # 重复数据记录数
    duplicateNum = checkData[True]
    # 唯一数据记录数
    uniqueNum = checkData[False]
    return jsonify({"duplicateNum":str(duplicateNum),"uniqueNum":str(uniqueNum)})

@app05.route('/')
def show():
    return 'app05.hello'