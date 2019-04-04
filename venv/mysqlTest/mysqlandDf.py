# -*- coding:utf-8 -*-
# @Time 2019/3/28 11:12
# @Author Ma Guichang
""""
test SQL -> Dataframe
"""

from flask import jsonify,request
from enum import Enum
import json
import re
import pymysql
import datetime
import pandas as pd
from Configlist import dbConfig
# 校验值域，长度，邮件
from validators import between,length,email
from flask import Flask,render_template,request,url_for
# app = Flask(__name__)
# 引用数据库配置类
# app.config.from_object(dbConfig)
# # 数据库地址
# DATABASE_URI = app.config.get('MYSQL_URI')
# # 数据库名称
# DATABASE_NAME = app.config.get('MYSQL_DB')
# # 数据库端口
# DATABASE_PORT = app.config.get('MYSQL_PORT')
# # 数据库用户名
# DATABASE_USER = app.config.get('MYSQL_USER')
# # 数据库密码
# DATABASE_PASSWORD = app.config.get('MYSQL_PWD')
# # 数据库字符编码
# DATABASE_CHARSET = app.config.get('MYSQL_CHARSET')
class Address(Enum):
    beijing = 1
    shanghai = 2
    xianggang = 3
    tianjin = 4
    chongqing = 5
    aomen = 6
    taibei = 7
    shenzhen = 8
    guangzhou = 9
def get_df_from_db(sql,connection,chunksize):
    return pd.read_sql(sql,connection,chunksize)

if __name__ == '__main__':

    # app.run(host='0.0.0.0', port=6666)


    # starttime = datetime.datetime.now()
    # # 导入数据库配置参数
    para = dbConfig.Config()
    for ad in Address.__members__.keys():
        print(ad)
    # 创建数据库连接
    # conn = pymysql.Connect(
    #     host = para.MYSQL_URI,
    #     port = para.MYSQL_PORT,
    #     user = para.MYSQL_USER,
    #     passwd = para.MYSQL_PWD,
    #     db = para.MYSQL_DB,
    #     charset = para.MYSQL_CHARSET
    # )
    # cur = conn.cursor()
    # null_num = 0
    # sql = "select * from datagovernance.testdata"
    # # # 分片读取大数据量
    # # # dfData = pd.read_sql(sql,conn,chunksize = 2000)
    # #
    # # sql2 = "DESC datagovernance.testdata"
    # sql2 = "SHOW FULL COLUMNS FROM datagovernance.testdata"
    # precisionInfo = pd.read_sql(sql2,conn)
    # print(precisionInfo)
    #
    # # 小数位数
    # xsws = precisionInfo['Type'][precisionInfo['Field'] == 'data']
    # print(xsws.values[0])
    # print('小数位数')
    # print(re.split(r"[',',')']",xsws.values[0]))
    # _,d,_=re.split(r"[',',')']", xsws.values[0])
    # print(d)
    # _,ws = str(xsws.values[0]).split(',')
    # w,_= ws.split(')')
    # # unitOfMeasurement = precisionInfo['Comment'][precisionInfo['Field'] == 'data']
    # unitOfMeasurement = precisionInfo['Comment'][precisionInfo['Field'] == 'age'].values[0]
    # print("计量单位")
    # print(unitOfMeasurement)
    #
    # print(w)
    # # 获取某个字段的数据类型
    # #
    # # # print(columnType['Type'][columnType['Field']=='age'])
    # # cc = columnType['Key'][columnType['Field']=='age']
    # cc = pd.DataFrame(columnType)
    #
    # print(columnType[['Field','Type','Comment']][columnType['Field']=='data'])
    # c = columnType[['Field', 'Key']][columnType['Key'] == 'PRI']
    # print(list(c['Field']))
    # if "id" in list(c['Field']):
    #     print("联合主键")
    # else:
    #     print("不是联合主键")
    # print(dict({"upri":list(c['Field'])}))
    #
    #
    #
    # print(type(cc))
    # if cc.values[0] =='':
    #     print("非主键")
    # else:
    #     print(cc.values[0])

    # 值域检验



    # for df in dfData:
    #     """
    #     1.空值校验，检验列
    #         a) 空值定义，在mysql中存的数据是空值还是null值，需要确定(我这边暂时按null处理)
    #         b) 空值校验，校验结果是只给出包含空值的结论，还是同时需要给出包含空值的数量与空值的位置
    #     """
    #     # 空值校验，检验列,以 address 为例
    #     v_null = pd.DataFrame(df['address'].isnull())
    #     v_null_count= pd.value_counts(v_null['address'])
    #     null_num = null_num + v_null_count[True]
    #
    #     """
    #     2.类型检验，检验列，数据类型要求
    #         a) 输入列名，检验该列的数据在数据库中的存储类型
    #     """
    #
    #
    #
    #
    # print('空值数量:'+str(null_num))

    #     if True in address_res:
    #         null_num = null_num + 1
    # print("空值数量:"+ str(null_num))

    # print(test)
    # print(pd.isnull(test))

    # dfData = pd.read_sql(sql,conn)




    # 2.类型校验，desc mysql中的数据表



    # 3.值域验证


    # 4.格式校验


    # 5.长度校验


    # 6.双表count校验


    # 7.单表单行校验

    # 8.单表汇总校验

    # 9.双表汇总校验


    # 10.精度校验

    # 11.单字段主键校验

    # 12.联合主键校验


    # 13.主外键校验

    # 14.双表参照性校验


    # # 验证数值取值范围
    # print(between(5, min=2))
    res = between(13.2, min=13, max=14)
    print(res)
    print(type(res))
    # print(between(40, max=400))
    # # 验证邮箱
    # res = email('mgc5320@163.com')
    # print(res)
    # print(type(res))
    # # 验证给定的字符串长度是否在指定范围内。
    # print(length('153', min=3))


    # print(dfData)
    # print(setdfData.isnull())
    endtime = datetime.datetime.now()

