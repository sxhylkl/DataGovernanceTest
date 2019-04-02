# -*- coding:utf-8 -*-
# @Time 2019/3/28 11:12
# @Author Ma Guichang
""""
test SQL -> Dataframe
"""
import pymysql
import random
import pandas as pd
from Configlist import dbConfig
import datetime



if __name__ == '__main__':
    # 程序开始时间
    starttime = datetime.datetime.now()
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
    conn.autocommit(True)
    cur = conn.cursor()
    fname = ['金', '赵', '李', '陈', '许', '龙', '王', '高', '张', '侯', '艾', '钱', '孙', '周', '郑','马','孔','宇文','东方','单','和','毛',\
             '江','南宫','西门','北堂','刘']
    mname = ['玉', '明', '玲', '淑', '偑', '艳', '大', '小', '风', '雨', '雪', '天', '水', '奇', '鲸', '米', '晓', '泽', '恩', '葛', '玄',
             '道', '振', '隆', '奇','金','克','近','力']
    lname = ['', '玲', '', '芳', '明', '红', '国', '芬', '', '云', '娴', '隐', '', '花', '叶', '', '黄', '亮', '锦', '茑', '军', '',
             '印', '', '凯','名','辉','青','庆','力','江','旭','通','雨','涛','强','平','源']
    citylist = ['beijing','shanghai','guangzhou','shenzhen','tianjin','chongqing','chengdu','','diaoyudao','xianggang','aomen','taibei']

    for i in range(200000):
        # 生成随机数据
        name = random.choice(fname) + random.choice(mname) + random.choice(lname)
        age = random.randint(10, 90)
        data = random.randint(10, 1000)+random.random()
        address = random.choice(citylist)
        emailinfo = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890',6)) + '@' + \
                    str(random.choice('abcdefghijklmnopqrstuvwxyz0123456789')) + str(random.choice('0123abcdefghijklmnopqrstuvwxyz!@#$%^&*()')) + '.com'

        # 插入数据 （特别注意只能用%s  不能用%d,数值型数据不用引号
        cur.execute("insert into datagovernance.testdata(name,age,data,address,emailinfo) values(%s,%s,%s,%s,%s)", (name, age, data, address, emailinfo))
        # cur.execute("insert into datagovernance.testdata(name,age,data,emailinfo) values(%s,%s,%s,%s)", (name, age, data, emailinfo))

        conn.commit()  # 提交命令，否则数据库不执行插入操作

    endtime = datetime.datetime.now()

    print(("程序运行时间:")+str(endtime - starttime))