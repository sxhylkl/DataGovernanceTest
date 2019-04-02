# -*- coding:utf-8 -*-
# @Time 2019/3/28 18:54
# @Author Ma Guichang

from flashtext import KeywordProcessor
# import re
# c = re.compile(r'^\w+@(\w+\.)+(com|cn|net)$')
# email =input("请输入一个邮箱：")
# s = c.search(email)
# if s:
#     print(email)
# else:
#     print('邮箱格式不正确')
#
# from email_validator import validate_email
# v = validate_email('mgc530@163.com')
# email = v['email']
# print(email)

# 数值验证
from validators import between
from validators import email,length
# 验证数值取值范围
print(between(5,min=2))
print(between(13.2, min=13, max=14))
print(between(40, max=400))
# 验证邮箱
print(email('mgc5320@163.com'))
# 验证给定的字符串长度是否在指定范围内。
print(length('153',min=3))