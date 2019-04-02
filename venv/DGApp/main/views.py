# -*- coding:utf-8 -*-
# @Time 2019/4/1 13:38
# @Author Ma Guichang

from flask import Blueprint

main=Blueprint('main',__name__)

@main.route('/')
def show():
    return 'main.hello'