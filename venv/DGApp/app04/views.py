# -*- coding:utf-8 -*-
# @Time 2019/4/1 14:53
# @Author Ma Guichang

"""
 4.格式校验，检验列，格式要求
    a) 输入列名，检验该列的数据的格式是否符合要求（以邮箱、手机号、身份证格式为例）
    b) 数据格式:邮箱，身份证，手机号
"""
import pymysql
import pandas as pd
from flask import Blueprint,jsonify
from DGApp.Configlist import dbConfig
# 校验值域，长度，邮件
from validators import between,length,email
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

@app04.route('/checkFormat/<typeFormat>/<database>/<table>/<field>',methods = ['GET','POST'])
def checkFormat(typeFormat,database,table,field):
    """
    邮箱、手机号码、身份证格式校验
    :param database: 校验数据库
    :param table: 校验数据表
    :param field: 校验列
    :return:
    """
    db = database
    tb = table
    fd = field
    sql = "SELECT "+fd+" from "+db+"."+tb
    dfData = pd.read_sql(sql, conn, chunksize=2000)
    email_num = phone_num = card_num = 0
    # 检验该列所有数据的格式
    if typeFormat == 'email':
        for df in dfData:
            for data in df[fd]:
                if email(data):
                    email_num = email_num+1
        return jsonify({fd + " format correct num":str(email_num)})
    elif typeFormat == 'phone':
        for df in dfData:
            for data in df[fd]:
                if checkPhone(str(data)):
                    phone_num = phone_num + 1
        return jsonify({fd + " format correct num": str(phone_num)})
    elif typeFormat == 'idCard':
        for df in dfData:
            for data in df[fd]:
                # checkRes = checkIdcard(data)
                # if checkRes != '':
                #     print(checkRes)
                if data is not None:
                    if checkIdcard(str(data)) == True:
                        card_num = card_num + 1
        return jsonify({fd + "format correct num": str(card_num)})
# 访问示例:127.0.0.1:5000/app04/checkFormat/idCard/datagovernance/testdata/idcard

# @app04.route('/')
# def show():
#     return 'app03.hello'