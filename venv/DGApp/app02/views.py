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


# 列类型校验
@app02.route('/type')
def checkType():

    sql = "DESC datagovernance.testdata"
    columnType = pd.read_sql(sql, conn)
    # 获取某个字段的数据类型
    ftype = columnType['Key'][columnType['Field'] == 'age']
    res = str(ftype.values[0])
    typeStr,lenColumn = res.split('(')
    lenColumn,_ = lenColumn.split(')')
    return jsonify({typeStr:str(lenColumn)})

# 单字段主键校验
@app02.route('/pri')
def checkPri():

    sql = "DESC datagovernance.testdata"
    columnInfo = pd.read_sql(sql, conn)
    # 获取某个字段的数据主键信息
    isPri = columnInfo['Key'][columnType['Field'] == 'id']
    if isPri == '':
        print('校验列为非主键列')
    else:
        print("校验列为主键列")
    return jsonify({'id':isPri})


# 联合主键校验
@app02.route('/unionPri')
def checkUnionPri():

    sql = "DESC datagovernance.testdata"
    columnInfo = pd.read_sql(sql, conn)
    # 获取检验列联合主键信息
    uPriInfo = columnInfo[['Field','Type']][columnInfo['Key']=='PRI']
    uPriList = list(uPriInfo['Field'])
    # 假定age为检验列
    if "age" in uPriList:
        print("age 是联合主键")
    else:
        print("非联合主键")
    # 联合主键信息
    res = dict({"uPri":uPriList})
    return jsonify(res)


# 精度校验
@app02.route('/precision/{db}/{tb}')
def checkPrecision():

    sql = "SHOW FULL COLUMNS FROM datagovernance.testdata"
    columnInfo = pd.read_sql(sql, conn)
    # 获取校验列的精度信息，计量单位，小数位数
    precisionInfo = columnInfo[['Field','Type','Comment']]
    # data为校验字段
    xsws = precisionInfo['Type'][precisionInfo['Field']=='data']
    typeSplit = re.split(r"[',',')']", xsws.values[0])
    if len(typeSplit) > 2:
        # decimalDigits为小数位数
        _, decimalDigits, _ = typeSplit
    else:
        print("校验列没有小数位")
    # 获取计量单位unitOfMeasurement
    unitOfMeasurement = precisionInfo['Comment'][precisionInfo['Field'] == 'data'].values[0]
    if unitOfMeasurement == '':
        print('校验列没有计量单位')
    else:
        print("校验列的计量单位为:"+unitOfMeasurement)
    res = {"decimalDigits":decimalDigits}
    return jsonify(res)
# @app02.route('/')
# def show():
#     return 'app02.hello'