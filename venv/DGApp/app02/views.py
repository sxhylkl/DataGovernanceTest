# -*- coding:utf-8 -*-
# @Time 2019/4/1 13:38
# @Author Ma Guichang

"""
 2.1 类型校验，检验列，数据类型要求(类型校验中整合长度校验，返回mysql中数据的类型长度，例int(11)中的11)
    a) 输入列名，检验该列的数据在数据库中的存储类型
    *) ok

 2.2 单字段主键校验，检验列，判断该字段的是否为主键
 2.3 联合主键校验，检验该列是否是联合主键，列出所有主键信息，查看该列是否在其中
 2.4 精度校验，检验列、计量单位、小数位数
"""
import re
import pymysql
import pandas as pd
from flask import Blueprint,jsonify
from DGApp.Configlist import dbConfig

app02=Blueprint('app02',__name__)
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


@app02.route('/checkType/<database>/<table>/<field>',methods=['GET','POST'])
def checkType(database,table,field):
    """
    列类型校验
    :param database: 校验数据库
    :param table: 校验数据表
    :param field: 校验列
    :return: 校验列在mysql中的存储类型
    """
    db = database
    tb = table
    fd = field
    sql = "DESC "+db+"."+tb
    columnType = pd.read_sql(sql, conn)
    # 获取某个字段的数据类型
    ftype = columnType['Type'][columnType['Field'] == fd]
    res = str(ftype.values[0])
    typeStr,lenColumn = res.split('(')
    lenColumn,_ = lenColumn.split(')')
    return jsonify({typeStr:str(lenColumn)})


@app02.route('/checkPri/<database>/<table>/<field>',methods=['GET','POST'])
def checkPri(database,table,field):
    """
    单字段主键校验
    :param database: 校验数据库名称
    :param table: 校验数据表
    :param field: 校验列
    :return: 返回主键校验结果
    """
    db = database
    tb = table
    fd = field
    sql = "DESC "+db+"."+tb
    print(sql)
    columnInfo = pd.read_sql(sql, conn)
    # 获取某个字段的数据主键信息
    isPri, = columnInfo['Key'][columnInfo['Field'] == fd].values
    print(isPri)
    if isPri == 'PRI':
        return jsonify({fd:isPri})
    else:
        return jsonify({fd:"NOT PRI"})


@app02.route('/checkUnionPri/<database>/<table>/<field>',methods=['GET','POST'])
def checkUnionPri(database,table,field):
    """
    联合主键校验
    :param database: 校验数据库
    :param table: 校验数据表
    :param field: 校验列
    :return: 返回联合主键校验结果
    """
    db = database
    tb = table
    fd = field
    sql = "DESC "+db+"."+tb
    columnInfo = pd.read_sql(sql, conn)
    # 获取检验列联合主键信息
    uPriInfo = columnInfo[['Field','Type']][columnInfo['Key']=='PRI']
    uPriList = list(uPriInfo['Field'])
    # 是否需要返回联合主键列表
    if fd in uPriList and len(uPriList)>1:
        return jsonify({fd:"unionPri"})
    else:
        return jsonify({fd:"NOT unionPri"})


@app02.route('/checkPrecision/<database>/<table>/<field>',methods=['GET','POST'])
def checkPrecision(database,table,field):
    """
    精度校验，校验小数点位数(计量单位校验待定)
    :param database: 校验数据库
    :param table: 校验数据表
    :param field: 校验列
    :return: 校验列的小数点位数
    """
    db = database
    tb = table
    fd = field
    sql = "SHOW FULL COLUMNS FROM "+db+"."+tb
    columnInfo = pd.read_sql(sql, conn)
    # 获取校验列的精度信息，计量单位，小数位数
    precisionInfo = columnInfo[['Field','Type','Comment']]
    # data为校验字段
    xsws = precisionInfo['Type'][precisionInfo['Field']== fd]
    typeSplit = re.split(r"[',',')']", xsws.values[0])
    if len(typeSplit) > 2:
        # decimalDigits为小数位数
        _, decimalDigits, _ = typeSplit
        return jsonify({fd:decimalDigits})
    else:
        return "校验列没有小数位"
    #  获取计量单位unitOfMeasurement
    # unitOfMeasurement = precisionInfo['Comment'][precisionInfo['Field'] == fd].values[0]
    # if unitOfMeasurement == '':
    #     print('校验列没有计量单位')
    # else:
    #     print("校验列的计量单位为:"+unitOfMeasurement)
    # res = {"decimalDigits":decimalDigits}
    # return jsonify(res)


# @app02.route('/')
# def show():
#     return 'app02.hello'