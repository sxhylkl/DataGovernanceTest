# -*- coding:utf-8 -*-
# @Time 2019/3/18 9:01
# @Author Ma Guichang

from elasticsearch import Elasticsearch

ip = "10.0.44.114"
port = "9200"
# user = "admin"
# pwd = "admin"

es = Elasticsearch(hosts="10.0.44.114",port=9200)
result = es.indices.create(index='news', ignore=400)
print(result)