# -*- coding:utf-8 -*-
# @Time 2019/4/1 13:38
# @Author Ma Guichang

from flask import Flask
from DGApp.main.views import *
from DGApp.app01.views import *
from DGApp.app02.views import *
from DGApp.app03.views import *
from DGApp.app04.views import *
from DGApp.app05.views import *
from DGApp.app06.views import *


app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(main,url_prefix='/index')
app.register_blueprint(app01,url_prefix='/app01')
app.register_blueprint(app02,url_prefix='/app02')
app.register_blueprint(app03,url_prefix='/app03')
app.register_blueprint(app04,url_prefix='/app04')
app.register_blueprint(app05,url_prefix='/app05')
app.register_blueprint(app06,url_prefix='/app06')

# app.register_blueprint(app02,url_prefix='/app04')
# app.register_blueprint(app02)


if __name__=='__main__':
  app.run()